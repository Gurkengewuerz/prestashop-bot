import time
import requests


"""
    Create Bot:
    1. Message @botfather with /newbot
    2. Send him your bot Name
    3. Choose a username
    4. GET ApI Token with /token
    5. Add to comfig.py telegram_api = "your token"
    6. Add to config.py telegram_chat = "your chat id"
"""

class TelegramBot():
    def __init__(self, api_key):
        """
            :param api_key: API Key for the Telegram Bot
        """
        self.token = api_key

    def sendMSG(self, user, msg):
        """
            Send message via the Telegram API
            :param user: the telegram chat in which the message will send
            :param msg: the text of the message
            :return: HTTP Response
        """
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
