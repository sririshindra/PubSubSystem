from flask import Flask, render_template, request, stream_with_context, Response
from time import sleep
import requests
# from pprint import pprint

import os
import sys

print("entered subscriber")


app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))


messages = []


@app.route('/')
def my_form():
    """
    When the user loads the website the default page that will be loaded using this method.
    Gets the default directions and weather form buffalo to nyc.
    :return: html file that returns the default directions and weather information from Buffalo to nyc
    """

    return render_template("subscribers.html")


@app.route('/', methods=['POST'])
def my_form_post():

    source = request.form['source']
    # destination = request.form['destination']

    requests.post("http://localhost:5000/subscribe", data={'topic': source, 'url': "http://localhost:" + sys.argv[1] + "/receive"})

    return render_template("subscribers_stream.html")


@app.route('/receive', methods=['POST'])
def receive():

    print("received messages")
    print(request.form["topic"])
    print(request.form["message"])

    messages.append({request.form["message"] + "  " + request.form["topic"]})

    return "Received!"


@app.route('/stream')
def stream():
    print("entered stream method")

    def generate():
        print("entered generate method")

        while True:
            # print("entered line 60")
            if len(messages) != 0:
                print("entered line 62")
                print("popped messages ")
                temp = messages.pop()
                print(temp)
                yield str(temp) + "\n"
            else:
                yield ""
            # sleep(1)
        # while messages:
        #     x = messages.pop()
        #     yield str(x)
        sleep(1)

    return Response(stream_with_context(generate()))


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(sys.argv[1]))
    # app.run(port=6001, debug=True, threaded=True)
