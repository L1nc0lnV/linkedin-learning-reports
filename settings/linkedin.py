from datetime import datetime, timedelta
import requests

class LinkedInConfig:

    def GetLinkedinRefreshToken(self, CLIENT_SECRET, CLIENTID):
        API_URL = f'https://www.linkedin.com/oauth/v2/accessToken?grant_type=client_credentials&client_id={CLIENTID}&' \
                  f'client_secret={CLIENT_SECRET}'
        return requests.get(API_URL).json()['access_token']

    def __init__(self):
        with open('env/linkedin.txt') as fi:
            self.CLIENT_SECRET = fi.readline().rstrip('\n')
        self.CLIENTID = '77plycpp70x634'
        self.TOKEN = LinkedInConfig.GetLinkedinRefreshToken(self, self.CLIENT_SECRET, self.CLIENTID)
        self.MEASURE_PERIOD = 'WEEK'  # Day or Week
        self.MEASURE_PERIOD_LOOKAHEAD = 1  # In days, can be a max of 14 days whether using DAY (14) or WEEK (2)
        self.MEASURE_PERIOD_START = round((datetime.now() + timedelta(-7)).timestamp() * 1000)  # epoch datetime now
        self.PAGE_COUNT = 1000
        self.PAGE_START = 0
        self.ASSET_TYPE = ['COURSE', 'VIDEO', 'ARTICLE', 'BOOK', 'EVENT', 'LEARNING_COLLECTION', 'LEARNING_PATH',
                           'DOCUMENT']
        self.HEADERS = {'Authorization': 'Bearer ' + self.TOKEN,
                        'Connection': 'keep-alive'}
        self.DBTABLE = 'LinkedInLearning_ActivityReports'



