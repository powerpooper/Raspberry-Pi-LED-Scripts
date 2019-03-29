import RPi.GPIO as GPIO
from flask import Flask, jsonify
import time


# create the flask server app
app = Flask(__name__)

# set the mode on the GPIO pins to be based on counting the pins via
# the the layout:
"""
1 3 5 7 9  11 13 15 17 19 ... (and so on)
2 4 6 8 10 12 14 16 18 20 ... (and so on)
"""
GPIO.setmode(GPIO.BOARD)


# Configuration for devices, incoming via REST call as type/thingname/action
# The lookup is then mapped to GPIO output to carryout the task
things = {
          'door':   [{'name': 'door1', 'gpio': {'activate':11}},
                     {'name': 'door2', 'gpio': {'activate':12}}]
}


# Initialize pins
for k,val in things.items():
    for t in val:
        for k,g in t['gpio'].items():
            print(k,g)
            GPIO.setup(g,GPIO.OUT)
            GPIO.output(g,GPIO.LOW)

# Run the action via GPIO output
def thing_do(f,action):
    print('thing_do')
    print(action)
    if action in f['gpio']:
        GPIO.output(f['gpio'][action], GPIO.HIGH)
        time.sleep(1)
        GPIO.output(f['gpio'][action], GPIO.LOW)
        # response code
        return 200
    else:
        # response code
        return 400


@app.route("/status")
def status():
    print("answering /status request")
    # response code
    return 'online', 200


@app.route("/<ttype>/<thing>/<action>")
def action(ttype,thing, action):
    # response code
    res = 400
    if ttype in things:
        for f in things[ttype]:
            if thing == f['name'] or thing == "all":
                # run an action based on lookup
                res = thing_do(f,action)

    return jsonify({'res':res}), res


# start the flask app
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=82, debug=False)
