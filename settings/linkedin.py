from datetime import datetime, timedelta


class LinkedInConfig:
    def __init__(self):
        with open('env/linkedin.txt') as fi:
            self.TOKEN = fi.readline().rstrip('\n')
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
