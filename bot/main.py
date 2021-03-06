from prestaobjects import *
from config import *
from db import *
from telegram import *
from twitterbot import *
import time
"""
    the Bot who looks for new payed orders and send if it needed the license keys if there enough in the database
"""
db = DB()

if __name__ == "__main__":
    db.connect() # connect to the database
    shopQuery = db.query("SELECT * FROM ita_shop;")
    for shop in shopQuery.fetchall():
        statQuery = db.query("SELECT * FROM ita_shop_stat WHERE shop_id=%s" % shop[0])
        statlist = list()
        for stat in statQuery.fetchall():
            statlist.append(stat[2])
        print(shop)
        shopObj = Shop(shop[1], shop[2], statlist, shop[4])
        if not shopObj.canConnect(): sys.exit("Can not connect to shop!")
        for order in shopObj.getorders():
            print("Going through Order %s" % order.reference)
            changedItems = 0
            for item in order.list_items:
                licenceQuery = db.query(
                    "SELECT * FROM ita_licencekey WHERE product_reference = '%s' AND rented_timestamp IS NULL" % item.reference)
                licenceFetch = licenceQuery.fetchall()
                if len(licenceFetch) >= item.quantity:
                    licenceList = list()
                    for i in range(item.quantity):
                        key = licenceFetch[i][1]
                        licenceList.append(key)
                        db.query("UPDATE ita_licencekey SET rented_timestamp = '%s' WHERE licence = '%s'" % (
                        int(time.time()), key))
                    print(
                        "Send to Order %s %sx licenses: %s" % (order.reference, item.quantity, "; ".join(licenceList)))
                    order.sendMSG("%s:\r\n%s" % (item.reference, "; ".join(licenceList)))
                    changedItems += 1
                else:
                    print("No Product Keys available for %s" % item.reference)
            if changedItems >= 1:
                order.setStatus(shopObj.delivstat)
                print("%s Set Order Status to deliverd" % order.reference)
                # Send the confirmation message that the license keys for the a order a send offer Twitter and Telegram
                if telegram_api is not None and telegram_api != "":
                    bot = TelegramBot(telegram_api)
                    bot.sendMSG(telegram_chat, "%s Delivered" % order.reference)
                if access_token is not None and access_token != "":
                    twitter = TwitterAPI()
                    twitter.tweet("%s Delivered" % order.reference)

            else:
                print("%s has no Items that has been changed" % order.reference)
        break
    db.close()
