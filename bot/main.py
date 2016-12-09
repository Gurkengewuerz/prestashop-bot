from prestaobjects import *
from config import *
from db import *

db = DB()

if __name__ == "__main__":
    db.connect()
    shop = Shop(shop_url, api_key, [2, 4], None)
    if not shop.canConnect(): sys.exit("Can not connect to shop!")

    for order in shop.getorders():
        print(order.sendMSG("This is a test msg"))
        for item in order.list_items:
            if True and True:  # TODO: IF IN DB AND COUNT IS EQUAL OR HIGHER (db.query("SELECT * FROM ita_?")
                pass

    db.close()
