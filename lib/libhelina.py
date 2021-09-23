import requests
import json
import os
import base64

BASEURL = base64.b64decode("aHR0cDovL3JhZGlvLmdhcmRlbi9hcGkvYXJhL2NvbnRlbnQ=").decode("utf-8")

def getChannels():
    container, idcontainer = [], []
    URL = BASEURL + "/favorites"
    with open("lib/headers.json", "r") as f: data = json.load(f)
    response = requests.post(url=URL, data=data).json()
    for i in response["data"]:
        container.append((i["title"], i["place"]["title"], i["country"]["title"]))
        idcontainer.append(i["id"])
    return container, idcontainer

def getListenUrl(id):
    URL = f"{BASEURL}/listen/{id}/channel.mp3"
    return URL

