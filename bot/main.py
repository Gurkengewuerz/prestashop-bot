import requests
import xml.etree.ElementTree as ET
from config import *


class Product():
    def __init__(self, reference, name, quantity):
        self.reference = reference
        self.name = name
        self.quantity = quantity


class Orders():
    def __init__(self, order_id,customer, list_items, reference):
        self.oder_id = order_id
        self.customer = customer
        self.list_items = list_items
        self.reference = reference


class Shop():
    def __init__(self, url, key, list_paystat, delivstat, name="unknown"):
        self.url = url
        self.key = key
        self.list_paystat = list_paystat
        self.delivstat = delivstat
        self.name = name

    def getxml(self, path=""):
        req = requests.get(self.url+"/"+path, verify=False, auth=(self.key, ""))
        reqContent = str(req.content, "utf8")
        return ET.ElementTree(ET.fromstring(reqContent)).getroot()





if __name__ == "__main__":
    shop = Shop(shop_url, api_key, None, None)
    for order in shop.getxml("orders/2").find("order").find("associations").find("order_rows").findall("order_row"):
        reference = order.find("product_reference")
        print(reference.text)


