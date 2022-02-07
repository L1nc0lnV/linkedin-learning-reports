from datetime import datetime
class LinkedInConfig:
    def __init__(self):
        self.MEASURE_PERIOD = 'DAY'  # Day or Week
        self.MEASURE_PERIOD_LOOKBACK = 7  # In days, can be a max of 14 days whether using DAY (14) or WEEK (2); Data takes 24 hours to show up
        self.MEASURE_PERIOD_START = round(datetime.now().timestamp() * 1000)  # epoch datetime now
        self.PAGE_COUNT = 1000
        self.PAGE_START = 0
        self.ASSET_TYPE = ['COURSE', 'VIDEO', 'ARTICLE', 'BOOK', 'EVENT', 'LEARNING_COLLECTION', 'LEARNING_PATH']
        self.HEADERS = {'Authorization': 'Bearer ',
                        'Connection': 'keep-alive'}
        self.DBTABLE = 'LinkedInLearning_ActivityReports'
