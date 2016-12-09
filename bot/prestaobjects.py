import requests
import xml.etree.ElementTree as ET
from utils import *


class Product():
    def __init__(self, reference, name, quantity):
        self.reference = reference
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return self.reference + ";" + str(self.quantity) + "=>" + self.name


class Order():
    def __init__(self, shop, order_id, customer, list_items, reference):
        self.order_id = order_id
        self.customer = customer
        self.list_items = list_items
        self.reference = reference
        self.shop = shop
        self.thread = 0

    def sendMSG(self, msg):
        threadXML = self.shop.getxml("customer_threads?display=full&filter[id_order]=%s" % self.order_id)
        if len(threadXML.find("customer_threads").findall("customer_thread")) < 1:
            xmlThread = self.shop.getNew("customer_threads")
            xmlThread.find("customer_thread").find("id_order").text = str(self.order_id)
            xmlThread.find("customer_thread").find("status").text = "closed"
            xmlThread.find("customer_thread").find("id_lang").text = "0"
            xmlThread.find("customer_thread").find("id_contact").text = "0"
            xmlThread.find("customer_thread").find("id_shop").text = "1"
            xmlThread.find("customer_thread").find("token").text = randomword(25)
            xmlThreadStr = str(self.shop.add("customer_threads", xmlThread).content, "utf8")
            self.thread = self.shop.stringToXML(xmlThreadStr).find("customer_thread").find("id").text
        else:
            self.thread = threadXML.find("customer_threads").find("customer_thread").find("id").text

        xmlMSG = self.shop.getNew("customer_messages")
        xmlMSG.find("customer_message").find("id_employee").text = "1"
        xmlMSG.find("customer_message").find("id_customer_thread").text = self.thread
        xmlMSG.find("customer_message").find("message").text = str(msg)
        xmlMSG.find("customer_message").find("private").text = 0
        _message_id = self.shop.stringToXML(str(self.shop.add("customer_messages", xmlMSG).content, "utf8")).find(
            "customer_message").find("id").text

        return _message_id, self.thread

    def setStatus(self, id):
        xmlOrder = self.shop.getAsXML("orders/%s" % self.order_id)
        xmlOrder.find("order").find("current_state").text = str(id)
        self.shop.update("orders", xmlOrder)


class Shop():
    def __init__(self, url, key, list_paystat, delivstat, name="unknown"):
        self.url = url
        self.key = key
        self.list_paystat = list_paystat
        self.delivstat = delivstat
        self.name = name
        self.list_orders = list()

    def canConnect(self):
        try:
            status = requests.get(self.url, auth=(self.key, ""), timeout=2).status_code
        except:
            return False

        if status == 200:
            return True
        else:
            return False

    def stringToXML(self, string):
        return ET.ElementTree(ET.fromstring(string)).getroot()

    def xmlToString(self, xml):
        return ET.tostring(xml).decode("utf8")

    def getNew(self, path):
        return self.getxml(path + "?schema=blank")

    def getxml(self, path=""):
        req = requests.get("%s/%s" % (self.url, path), auth=(self.key, ""))
        reqContent = str(req.content, "utf8")
        return ET.ElementTree(ET.fromstring(reqContent)).getroot()

    def add(self, resource, xml):
        return requests.post(self.url + resource, data=self.xmlToString(xml), headers={'Content-Type': 'text/xml'},
                             auth=(self.key, ""))

    def update(self, resource, xml):
        return requests.put(self.url + resource, data=self.xmlToString(xml), headers={'Content-Type': 'text/xml'},
                            auth=(self.key, ""))

    def getorders(self):
        for state in self.list_paystat:
            for order in self.getxml("orders?display=full&filter[current_state]=%s" % state).find("orders").findall(
                    "order"):
                id = order.find("id")
                id_customer = order.find("id_customer")
                order_reference = order.find("reference")
                list_items = list()
                for item in order.find("associations").find("order_rows").findall("order_row"):
                    reference = item.find("product_reference")
                    name = item.find("product_name")
                    quantity = item.find("product_quantity")
                    pro = Product(reference.text, name.text, int(quantity.text))
                    list_items.append(pro)
                self.list_orders.append(
                    Order(self, int(id.text), int(id_customer.text), list_items, order_reference.text))
        return self.list_orders
