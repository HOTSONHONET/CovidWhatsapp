import requests
import time
import json
import random

# Show all the available region data


def showAllSupportedRegions():
    time.sleep(2)
    r = requests.get('https://api.quarantine.country/api/v1/regions')
    if r.status_code == 200:
        data = r.json()['data']
        msg = "Here is the List of all regions, which you can enquire...\n"
        for i, d in enumerate(data):
            msg += f"{i+1}) {d['name']}\n"
            if i > 10:
                msg+=f"And rest {len(data)-10} regions..."
                break
        return msg
    return "Server Down..."

# Show COVID latest data
def showLatestData(*args):
 
    time.sleep(2)
    r = requests.get("https://api.quarantine.country/api/v1/summary/latest")
    if r.status_code == 200:
        data = r.json()["data"]

        if "summary" in args:
            msg = "Summary...\n\n"
            summary = data["summary"]
            for k, v in summary.items():
                msg += f"{' '.join(list(map(lambda x: x.title(), k.split('_'))))}: {round(v, 3)}\n"

        elif "regions" in args:            
            country = args[1].lower()
            place = args[2].lower()
            r = requests.get(f"https://api.quarantine.country/api/v1/summary/region?region={country}&sub_areas=1")
            data = r.json()['data']
            details = data["regions"]
            if len(details) == 0:
                return "Database doesn't have information for this place..."
            poi = details[place]
            msg = f'Showing results for {place.upper()}...\n\n'
            for k, v in poi.items():
                if not k.startswith("iso"):
                    if k == "change":                        
                        for k_sub, v_sub in poi[k].items():
                            msg += f"{' '.join(list(map(lambda x: x.title(), k_sub.split('_'))))}: {round(v_sub, 3)}\n"
                    elif str(type(v)) == "<class 'str'>":
                        msg += f"{' '.join(list(map(lambda x: x.title(), k.split('_'))))}: {v}\n"
                    else:
                        msg += f"{' '.join(list(map(lambda x: x.title(), k.split('_'))))}: {round(v, 3)}\n"
        else:
            change = data["change"]
            msg = "Rate of Changes...\n\n"
            for k, v in change.items():
                msg += f"{' '.join(list(map(lambda x: x.title(), k.split('_'))))}: {round(v, 3)}\n"
        return msg

    return "Server Down..."


# Give List of Beds
def getBeds():
    with open("src//data_coor.json", "r") as data:
        data = json.load(data)
    random.shuffle(data)
    msg = "Here is the list of all avaiable beds for hospitalization...\n"
    for i, d in enumerate(data):
        if d['category'] == "BEDS":
            msg += f"Name : {d['name']}\nAddress : {d['address']}\nContact : {d['Contact']}\n\n"
        if i>20:
            break

    return msg

# Give List of Oxygen dealers
def getOxygen():
    with open("src//data_coor.json", "r") as data:
        data = json.load(data)
    random.shuffle(data)
    msg = "Here is the list of all avaiable Oxygen Suppliers...\n"
    for i, d in enumerate(data):
        if d['category'] == "OXY":
            msg += f"Name : {d['name']}\nAddress : {d['address']}\nContact : {d['Contact']}\n\n"
        if i>20:
            break
    return msg


# Replies for "hi"
hi_replies = [
    "Hello, I'm Bot Covid",
    "Hi, This is your friend Bot Covid",
]

# Options for clients
features = [
    "This are the available features...\n1. List of Supported regions\n2. Show me COVID Stats\n3. List of Oxygen Suppliers\n4. List of Hospitals with availability of oxygen beds \n\nJust reply with the index number e.g 'help_1' for list of available features"
]

# Default line
line = "Hi, I'm Bot Covid. My aim is to update all of my clients about the existing COVID-19 pandemic.\nUse me to keep yourself updated in this crisis.\nI can also give you the list of available medical services where you can treat yourself or any of your loved ones..."


