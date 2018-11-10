from flask import Flask, render_template, request, stream_with_context, Response
from time import sleep
import requests
# from pprint import pprint

import os
import sys

print("entered publisher")

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))


@app.route('/')
def my_form():
    """
    When the user loads the website the default page that will be loaded using this method.
    Gets the default directions and weather form buffalo to nyc.
    :return: html file that returns the default directions and weather information from Buffalo to nyc
    """

    return render_template("publishers.html")


@app.route('/', methods=['POST'])
def my_form_post():

    source = request.form['source']
    destination = request.form['destination']

    r = requests.post("http://localhost:5000/publish", data={'topic': source, 'message': destination})
    print(r.status_code, r.reason)

    return render_template("publishers.html")
    return render_template("directions_stream.html")


if __name__ == "__main__":
    print(sys.argv[0])
    app.run(debug=False, host='0.0.0.0', port=int(sys.argv[1]))
    # app.run(debug=False, port=7001)

