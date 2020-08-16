import configparser

conf = configparser.ConfigParser()
conf.read('setting.ini')

url = conf['line']['url']
access_token = conf['line']['access_token']