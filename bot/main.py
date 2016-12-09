import requests
import xml.etree.ElementTree as ET
from config import *


class Product():
    def __init__(self, reference, name, quantity):
        self.reference = reference
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return self.reference + ";" + str(self.quantity) + "=>" + self.name


class Order():
    def __init__(self, shop, order_id, customer, list_items, reference):
        self.oder_id = order_id
        self.customer = customer
        self.list_items = list_items
        self.reference = reference
        self.shop = shop

    def sendMSG(self):
        threadExists = False
        thread = self.shop.getxml("customer_threads?display=full&filter[id_order]=" + str(self.oder_id)).find("customer_threads").findall("customer_thread")

        if len(thread) >= 1:
            threadExists = True



class Shop():
    def __init__(self, url, key, list_paystat, delivstat, name="unknown"):
        self.url = url
        self.key = key
        self.list_paystat = list_paystat
        self.delivstat = delivstat
        self.name = name
        self.list_orders = list()

    def getxml(self, path=""):
        req = requests.get(self.url + "/" + path, verify=False, auth=(self.key, ""))
        reqContent = str(req.content, "utf8")
        return ET.ElementTree(ET.fromstring(reqContent)).getroot()

    def stringToXML(self, string):
        return ET.ElementTree(ET.fromstring(string)).getroot()

    def xmlToString(self, xml):
        return ET.tostring(xml).decode("utf8")

    def add(self, resource, xml):
            return requests.post(self.url + resource, data=self.xmlToString(xml), headers={'Content-Type': 'text/xml'}, auth=(self.key, ""))

    def update(self, resource, xml):
            return requests.put(self.url + resource, data=self.xmlToString(xml), headers={'Content-Type': 'text/xml'}, auth=(self.key, ""))

    def getorders(self):
        for order in self.getxml("orders?display=full&filter[current_state]=2").find("orders").findall("order"):
            id = order.find("id")
            print("Bestellung", id.text)
            id_customer = order.find("id_customer")
            print("Kunde", id_customer.text)
            list_items = list()
            for item in order.find("associations").find("order_rows").findall("order_row"):
                reference = item.find("product_reference")
                name = item.find("product_name")
                quantity = item.find("product_quantity")
                pro = Product(reference.text, name.text, int(quantity.text))
                list_items.append(pro)
                print(pro)
            self.list_orders.append(Order(self, int(id.text), int(id_customer.text), list_items, reference))
        return self.list_orders


if __name__ == "__main__":
    shop = Shop(shop_url, api_key, None, None)
    for order in shop.getorders():
        order.sendMSG()
        for item in order.list_items:
            if True and True:  # TODO: IF IN DB AND COUNT IS EQUAL OR HIGHER
                pass