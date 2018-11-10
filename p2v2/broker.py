from flask import Flask, render_template, request, stream_with_context, Response
from time import sleep
from threading import Thread
import requests

# from pprint import pprint

import os
import sys

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

global_list = [1, 2, 3, 4, 5, 6, 7]
messages = {}#{"dummy_topic": [1, 2, 3, 4, 5, 6, 7]}
subscribe_dict = {}


@app.route('/')
def my_form():
    """
    When the user loads the website the default page that will be loaded using this method.
    Gets the default directions and weather form buffalo to nyc.
    :return: html file that returns the default directions and weather information from Buffalo to nyc
    """

    return render_template("directions.html")


@app.route('/', methods=['POST'])
def my_form_post():

    source = request.form['source']
    destination = request.form['destination']

    path = "/Users/srinivasrishindra/Desktop/Fall_2018/Distributed_Systems/project2/phase1/phase1_docker/"
    print("Source is ", source)
    print("destination is ", destination)

    #os.system(source + " > " + path + "/" + destination)

    text_file = open(path + destination, "w")

    text_file.write(source)

    text_file.close()

    os.system("sh /Users/srinivasrishindra/IdeaProjects/DistributedProjectTwo/rundocker.sh")

    return render_template("directions_stream.html")


@app.route('/publish', methods=['POST'])
def publish():
    print("published message here")
    topic = request.form["topic"]
    message = request.form["message"]
    print(topic)
    print(message)

    if messages.get(topic) is None:
        messages[topic] = [message]
    else:
        messages[topic].append(message)

    return 'Received !'


@app.route('/subscribe', methods=['POST'])
def subscribe():
    topic = request.form["topic"]
    url = request.form["url"]
    # subscribe_dict[topic] = url
    if subscribe_dict.get(topic) is not None:
        subscribe_dict[topic].append(url)
    else:
        subscribe_dict[topic] = [url]

    print(subscribe_dict)

    return 'Received !'


def notify():
    while True:
        # print ("entered line 89")
        for topic, urls in subscribe_dict.items():
            while messages.get(topic) is not None and len(messages.get(topic)) != 0:
                message = messages[topic].pop()
                for url in urls:
                    print("sending to  topic " + str(topic) + " with url " + url)

                    try:
                        requests.post(url, data={'topic': topic, "message": message})
                    except Exception as e:
                        print("an exception has been caught")
                        print(e)

        # if global_list:
        #     print(global_list.pop())
        sleep(2)


if __name__ == "__main__":

    t1 = Thread(target=notify)
    t1.setDaemon(True)
    t1.start()

    # notify()

    print("thread finished...exiting")
    app.run(debug=False, host='0.0.0.0', port=int(sys.argv[1]))
    # app.run(debug=False)

    # while True:
    #     print("entered line 112")
    #     for topic, urls in subscribe_dict.items():
    #         while messages.get(topic) is not None:
    #             for url in urls:
    #                 print("sending to  topic " + str(topic) + " with url " + url)
    #
    #                 requests.post(url, data={'topic': topic, "message": messages[topic].pop()})
