from flask import Flask, render_template, request, stream_with_context, Response
from time import sleep
from threading import Thread
import requests

# from pprint import pprint

import os
import sys
import logging
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

print("entered broker")
logging.error("entered broker")

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

messages = {}   #{"dummy_topic": [1, 2, 3, 4, 5, 6, 7]}
subscribe_dict = {}


@app.route('/')
def my_form():
    """
    Does nothing, this code is only there to verify if the broker is alive
    :return:
    """

    return render_template("directions.html")



@app.route('/publish', methods=['POST'])
def publish():
    """
    receives the messages from brokers and saves in the internal memory
    :return: returns the received flag once a message is received
    """
    print("published message here")
    logging.error("published message here")
    topic = request.form["topic"]
    message = request.form["message"]
    print(topic)
    print(message)
    logging.error(topic)
    logging.error(message)

    if messages.get(topic) is None:
        messages[topic] = [message]
    else:
        messages[topic].append(message)

    return 'Received !'


@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    receives the topic from which a subscriber is subscribed
    :return: returns the received flag once a topic is subscribed
    """
    topic = request.form["topic"]
    url = request.form["url"]
    logging.error("")
    logging.error("my remote address is as follows")
    logging.error(request.remote_addr)
    logging.error(url)

    url = "http://" + str(request.remote_addr) + ":6001/receive"
    logging.error(url)
    if subscribe_dict.get(topic) is not None:
        subscribe_dict[topic].append(url)
    else:
        subscribe_dict[topic] = [url]

    print(subscribe_dict)

    return 'Received !'


def notify():
    """
    Continuously check if there are any new messages and sends the message to all the subscribed topics
    :return: None
    """
    while True:
        for topic, urls in subscribe_dict.items():
            while messages.get(topic) is not None and len(messages.get(topic)) != 0:
                message = messages[topic].pop()
                for url in urls:
                    print("sending to  topic " + str(topic) + " with url " + url)
                    logging.error("sending to  topic " + str(topic) + " with url " + url)

                    try:
                        r = requests.post(url, data={'topic': topic, "message": message})
                        logging.error("made a notify request")
                        logging.error("sending to  topic " + str(topic) + " with url " + url)
                        logging.error(r)
                    except Exception as e:
                        print("an exception has been caught")
                        logging.error("an exception has been caught")
                        logging.error(e)
                        print(e)

        sleep(2)


if __name__ == "__main__":

    """
    The starts the thread that notifies the messages to all the subscribers  
    """
    t1 = Thread(target=notify)
    t1.setDaemon(True)
    t1.start()

    print("thread finished...exiting")
    # app.run(debug=False, host='0.0.0.0', port=int(sys.argv[1]))
    app.run(debug=False, host='0.0.0.0')
    # app.run(debug=False, host='0.0.0.0', port=int(sys.argv[1]))
    # app.run(debug=False)
