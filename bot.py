from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from config import twilio_password, twilio_username, airbnb_password, airbnb_username


password = twilio_password

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
    #webhook logic
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'joke' in incoming_msg:
        # return a joke
        r = requests.get('https://official-joke-api.appspot.com/random_joke')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["setup"]} {data["punchline"]}'
        else:
            quote = 'I could not retrieve a joke at this time, sorry.'
        msg.body(quote)
        responded = True
    if not responded:
        msg.body('I can currently only send jokes, sorry!')
    return str(resp)


