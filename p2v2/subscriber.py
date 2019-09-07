from flask import Flask, render_template, request, stream_with_context, Response
from time import sleep
import requests
# from pprint import pprint

import os
import sys

print("entered subscriber")

"""
Initializes the flask app
"""
app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))


messages = ["Subscriber Started"]
# messages = [2, 3, 4, 1,2,3,4,4,5,6,6,6]


@app.route('/')
def my_form():
    """
    :return: html file that provides the input box where the user can enter the topic that a particular
    subscriber has to subscribe to. Also the html includes an ajax call to get the messages a particular topic has.
    """

    return render_template("subscribers.html")


@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    This code gets the topic that the subscriber has to subscribe from the browser and makes an api call to broker
    to let it know that this particular subscriber is intsrested in this particular topic.

    :return: returns the success flag once the api is successful.
    """
    print("subscriber called hope this works")

    source = request.form['source']
    print("source is ", source)

    requests.post("http://localhost:5000/subscribe", data={'topic': source, 'url': "http://localhost:" + sys.argv[1] + "/receive"})

    return "sucesss!"


@app.route('/receive', methods=['POST'])
def receive():
    """
    this method provides the endpoint for the broker to send the message from the subscriber
    :return: returns the Received flag once the messages are appended to the internal memory.
    """
    print("received messages")
    print(request.form["topic"])
    print(request.form["message"])

    messages.append(str(request.form["message"]) + "  " + str(request.form["topic"]))

    return "Received!"


@app.route("/stream")
def stream():
    """
    This code is called by an ajax call in the browser's html to stream the messages to the browser as they are
    received on the backend.
    :return:
    """
    def eventStream():

        while True:
            # print("entered line 60")
            print("entered while loop")
            if len(messages) != 0:
                print("entered line 62")
                print("popped messages ")
                temp = messages.pop()
                print(temp)
                yield str(temp) + "\n"
            else:
                yield ""
            sleep(2)

    return Response(eventStream(), mimetype="text/event-stream")


if __name__ == "__main__":
    """
    Starts the flask app
    """
    app.run(debug=True, host='0.0.0.0', port=int(sys.argv[1]), threaded=True)
    # app.run(port=6001, debug=True, threaded=True)

