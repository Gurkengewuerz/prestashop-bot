# FIXME: REFACTOR/ CLEANUP CODE!!!!!!!

import json
import os
import time
import ast
import collections
from bottle import route, run, static_file, request, response
from db import *

db = DB()
PATH = os.path.dirname(os.path.realpath(__file__))
response.default_content_type = "application/json"


@route('/')
def index_hook():
    return static_file("index.html", root=PATH + "./static/")


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=PATH + "./static/")


"""
/api/add/licence/<key> ✔
/api/add/shop/<key>/<url>/<name>/<paystat>/<delivstat> ✔
/api/delete/licence/<key> ✔
/api/delete/shop/<key>/<url> ✔
/api/get/shop ✔
/api/get/licence ✔
/api/get/licence/<product> ✔
"""


@route("/api/get/licence")
@route("/api/get/licence/<product>")
def get_licence_hook(product=None):
    where = ""
    if product is not None:
        where = " WHERE product_reference = '%s'" % product
    data = db.query("SELECT * FROM ita_licencekey %s" % where)
    output = []
    for row in data.fetchall():
        r = collections.OrderedDict()
        r["id"] = row[0]
        r["licence"] = row[1]
        r["product_reference"] = row[2]
        r["created_timestamp"] = row[3]
        r["rendet_timestamp"] = row[4]
        output.append(r)
    return json.dumps(output)


@route("/api/get/shop")
def get_shop_hook():
    data = db.query("SELECT * FROM ita_shop")
    output = []
    for row in data.fetchall():
        r = collections.OrderedDict()
        r["id"] = row[0]
        r["url"] = row[1]
        r["api_key"] = row[2]
        r["shop_name"] = row[3]
        r["delivstat"] = row[4]
        r["paystat"] = list()
        for row2 in db.query("SELECT * FROM ita_shop_stat WHERE shop_id = %s" % row[0]).fetchall():
            r["paystat"].append(row2[2])
        output.append(r)
    return json.dumps(output)


@route("/api/add/licence/")
@route("/api/delete/licence/")
@route("/api/add/shop/")
@route("/api/delete/shop/")
def add_delete_hook():
    return {"error": "API Request not Valid!"}


@route("/api/delete/licence/<key>", method="GET")
def delete_licence(key=""):
    output = {"error": "No"}
    if key != "":
        output["info"] = ("Delete Key %s" % key)
        db.query("DELETE FROM ita_licencekey WHERE licence = '%s'" % key)
    else:
        output["error"] = "No Valid Key set!"
    return output


@route("/api/delete/shop/<key>", method="GET")
@route("/api/delete/shop/<key>/<url:re:.+>", method="GET")
def add_shop(key="", url=""):
    output = {"error": "No"}
    if key != "":
        if url != "":
            output["info"] = ("Delete Shop %s@%s" % (url, key))
            sql = "DELETE FROM ita_shop WHERE url = '%s' AND api_key = '%s'" % (url, key)
            db.query(sql)
        else:
            output["error"] = "No SHOP Url to API"
    else:
        output["error"] = "No Valid Key set!"
    return output


@route("/api/add/licence/<key>", method="GET")
@route("/api/add/licence/<key>/<reference>", method="GET")
def add_licence(key="", reference=""):
    output = {"error": "No"}
    if key != "":
        if reference != "":
            output["info"] = ("Import Key %s" % key)
            db.query(
                "INSERT INTO ita_licencekey (licence, product_reference, created_timestamp, rented_timestamp) VALUES ('%s','%s','%s', NULL)" % (
                    key, reference, int(time.time())))
        else:
            output["error"] = "No Product Reference"
    else:
        output["error"] = "No Valid Key set!"
    return output


@route("/api/add/shop/<key>", method="GET")
@route("/api/add/shop/<key>/<url:re:.+>", method="GET")
@route("/api/add/shop/<key>/<url:re:.+>/<name>", method="GET")
@route("/api/add/shop/<key>/<url:re:.+>/<name>/<paystat>", method="GET")
@route("/api/add/shop/<key>/<url:re:.+>/<name>/<paystat>/<delivstat>", method="GET")
def add_shop(key="", url="", name="", paystat="", delivstat=""):
    output = {"error": "No"}
    if key != "":
        if url != "":
            if name != "":
                if paystat != "":
                    if delivstat != "":
                        output["info"] = ("Import new Shop")
                        ai_val = db.query("SHOW TABLE STATUS LIKE 'ita_shop';").fetchone()[10]
                        db.query(
                            "INSERT INTO ita_shop (url, api_key, shop_name, delivstat) VALUES ('%s','%s','%s','%s')" % (
                                url, key, name, delivstat))
                        for stat in ast.literal_eval(paystat):
                            db.query("INSERT INTO ita_shop_stat (shop_id, stat) VALUES ('%s', '%s')" % (ai_val, stat))
                    else:
                        output["error"] = "No Deliver Status"
                else:
                    output["error"] = "No PayStats"
            else:
                output["error"] = "No Name set"
        else:
            output["error"] = "No SHOP Url to API"
    else:
        output["error"] = "No Valid Key set!"
    return output


run(host='localhost', port=8080, debug=True)
