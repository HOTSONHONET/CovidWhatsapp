from flask import Flask, current_app as app, request
import requests
from datetime import datetime
from twilio.twiml.messaging_response import MessagingResponse
from src.utils import *
import random



# get list of supported regions


@app.route("/", methods=["POST"])
def main():
    incoming_msg = request.values.get('Body', "").lower()
    response = MessagingResponse()
    msg = response.message()
    responded = False

    if 'hi' in incoming_msg or 'hello' in incoming_msg:
        cur_msg = hi_replies[random.randint(0, len(hi_replies)-1)]
        msg.body(f"{cur_msg}")
        msg.body(f"{features[0]}")
        responded = True

    if 'help_1' in incoming_msg:
        d = showAllSupportedRegions()
        msg.body(d)
        responded = True

    if 'help_2' in incoming_msg:
        msg.body("Here is the list of Queries that you can perform...\n\n1. Summary \n2. Region based Stats \n3. Statiscal Changes \n\nGuidelines:\n'->helpsub_2_1' to get latest summary of Covid-19\n\n->helpsub_2_2_<name-of-the-Country>_<name_of_the_place>\ne.g. help_2_2_USA_california to get Covid stats of flourida\n\n->helpsub_2_3 to get overall rate of change statistics")
        responded = True

    if "helpsub_2_1" in incoming_msg:
        d = showLatestData('summary')
        msg.body(d)
        responded = True
    
    if "helpsub_2_2" in incoming_msg:
        d = showLatestData('regions', incoming_msg.split("_")[-2], incoming_msg.split("_")[-1])
        msg.body(d)
        responded = True
    
    if "helpsub_2_3" in incoming_msg:
        d = showLatestData("change")
        msg.body(d)
        responded = True

    if 'help_3' in incoming_msg:
        d = getOxygen()
        msg.body(d)
        responded = True
    
    if "help_4" in incoming_msg:
        d = getBeds()
        msg.body(d)
        responded = True

    if not responded:
        msg.body(f"{line}")

    return str(response)
