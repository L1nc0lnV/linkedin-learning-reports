class BaseSettings:

    def __init__(self):
        with open('env/config.txt', 'r') as fi:
            self.DATABASE_DRIVER = fi.readline().rstrip('\n')
            self.DATABASE_HOST = fi.readline().rstrip('\n')
            self.DATABASE_USERNAME = fi.readline().rstrip('\n')
            self.DATABASE_PASSWORD = fi.readline().rstrip('\n')
            self.DATABASE_DATABASE = fi.readline().rstrip('\n')