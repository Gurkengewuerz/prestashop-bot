from prestaobjects import *
from config import *
from db import *
import time

db = DB()

if __name__ == "__main__":
    db.connect()
    #shop = Shop(shop_url, api_key, [2, 4], None)
    shopQuery = db.query("SELECT * FROM ita_shop;")
    for shop in shopQuery.fetchall():
        statQuery = db.query("SELECT * FROM ita_shop_stat WHERE shop_id=%s"%shop[0])
        statlist = list()
        for stat in statQuery.fetchall():
              statlist.append(stat[2])
        print(shop)
        shopObj = Shop(shop[1], shop[2], statlist, shop[4])
        if not shopObj.canConnect(): sys.exit("Can not connect to shop!")
        for order in shopObj.getorders():
            for item in order.list_items:
                licenceQuery = db.query("SELECT * FROM ita_licencekey WHERE product_reference = '%s' AND rented_timestamp IS NULL"%item.reference)
                licenceFetch = licenceQuery.fetchall()
                if len(licenceFetch) >= item.quantity:
                    # TODO: GET KEYS AND SEND THEM TO ORDER -> UPDATE
                    licenceList = list()
                    for i in range(item.quantity):
                        key = licenceFetch[i][1]
                        licenceList.append(key)
                        db.query("UPDATE ita_licencekey SET rented_timestamp = '%s' WHERE licence = '%s'"%(int(time.time()), key))
                    order.sendMSG("%s:\r\n%s"%(item.reference)) # TODO: TEST!!!!!!!!!!!!!!!!!!!
                else:
                    print("No Product Keys available")
        break
    db.close()
