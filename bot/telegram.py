import time
import requests


class TelegramBot():
    def __init__(self, api_key):
        self.token = api_key

    def sendMSG(self, user, msg):
        response = requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(self.token, "sendMessage"),
            data={'chat_id': user, 'text': msg}
        ).json()
        return response


if __name__ == "__main__":
    bot = TelegramBot("")
    while True:
        print(bot.sendMSG("", ""))
        time.sleep(1)
