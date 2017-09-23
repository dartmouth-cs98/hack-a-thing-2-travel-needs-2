import requests
import json
from flask import Flask, request
import apiai

# FB messenger credentials
ACCESS_TOKEN = "EAAGv9JFkZBTcBAB6na5bujZAj8lIQkydKidoZCZBTXWh2gkXHoVSBhhWBwuYY8mtYey70K42ZBzxtdjvPcyvFAvHnrEC1njR0XZAzBwz3FiiOBWZBZBGZCr9CuPDtLZAjCLoQ6VbUJjCHUoenWFEhWyiBzsYmEEa6IuIvKlwfeVt55iwZDZD"

# api.ai credentials
CLIENT_ACCESS_TOKEN = "d4c891a53bf240bca8a90f7c9a8763a5"
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    # our endpoint echos back the 'hub.challenge' value specified when we setup the webhook
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == 'foo':
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return 'Hello World (from Flask!)', 200

def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)


@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']

    # prepare API.ai request
    req = ai.text_request()
    req.lang = 'en'  # optional, default value equal 'en'
    req.query = message

    # get response from API.ai
    api_response = req.getresponse()
    responsestr = api_response.read().decode('utf-8')
    response_obj = json.loads(responsestr)
    if 'result' in response_obj:
        response = response_obj["result"]["fulfillment"]["speech"]
        reply(sender, get_info(response))

    return "ok"

def get_info(response):
    info = response.split(",")
    if info[0] == "banana":
        citizenship, destination, start_date, end_date = info[1], info[2], info[3], info[4]

        if citizenship == "Korea" and destination == "Viet Nam":
            response = "Traveling to " + destination + " as a citizen of " + citizenship + " does not require a visa if you're staying for less than 15 days and if you haven't visited $destination in the last 6 months.\n\n" +"Standard voltage in " + destination + " is 110/220V.\n\n"+"Average high temperature in " + destination + " from " + start_date + " to " + end_date + " is 37.9 C / 91.04 F with an average low of 26.2 C / 79.16 F. Humidity will be over 80%, and there is a high chance of rain during your stay, so bring an umbrella!\n\n"+"The currency used in " + destination +" is the Vietnamese Dong (VND). 1 SKW is currently equal to 20.05 VND."
        elif citizenship == "China" and destination == "United Arab Emirates":
            response = "If you're traveling to  " + destination + " as a citizen of " + citizenship + ", you will be granted a visa on arrival.\n\n"+"Standard voltage in " + destination + " is 220-240V. You will need an adaptor as the plugs look different.\n\n"+"Average high temperature in " + destination + " from " + start_date + " to " + end_date + " is 100.3 C / 100.3 F with an average low of 27.2 C / 81 F. Humidity will be around 55%, and it will be sunny, so pack some sunscreen!\n\n"+"The currency used in " + destination +" is the United Arab Emirates dirham. 1 Yuan is currently equal to 0.56 dirham."

    return response


if __name__ == '__main__':
    app.run(debug=True)
