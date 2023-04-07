import re
from image import noImage

def getID(input):
    res = re.findall('tvg-id="(.+?)" ', input)
    if len(res) > 0:
        return res[0]
    else:
        return "No ID"

def getTitle(input):
    res = re.findall('tvg-name="(.+?)" ', input)
    if len(res) > 0:
        return res[0]
    else:
        return "No Title"

def getLogo(input):
    res = re.findall('tvg-logo="(.+?)" ', input)
    if len(res) > 0:
        return res[0]
    else:
        return noImage()