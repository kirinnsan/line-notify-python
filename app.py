import requests
import setting


class LineNotify(object):
    def __init__(self, access_token, url):
        self.access_token = access_token
        self.url = url
        self.headers = {'Authorization': 'Bearer ' + self.access_token}

    def send_message(self, message):
        payload = {'message': message}
        requests.post(self.url, headers=self.headers, params=payload,)


if __name__ == "__main__":
    access_token = setting.access_token
    url = setting.url

    message = 'Hello World!'

    line = LineNotify(access_token, url)
    line.send_message(message)
