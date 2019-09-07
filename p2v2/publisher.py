from flask import Flask, render_template, request, stream_with_context, Response
from time import sleep
import requests
import os
import sys

print("entered publisher")

"""
initializes the flask app
"""
app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))


@app.route('/')
def my_form():
    """
    :returns: the html containing input boxes for topic and message
    """

    return render_template("publishers.html")


@app.route('/', methods=['POST'])
def my_form_post():
    """
    sends the message and topic to the broker
    :return: the html containing input boxes for topic and message
    """
    source = request.form['source']
    destination = request.form['destination']

    r = requests.post("http://localhost:5000/publish", data={'topic': source, 'message': destination})
    print(r.status_code, r.reason)

    return render_template("publishers.html")


if __name__ == "__main__":
    """
    Run the flask app
    """
    print(sys.argv[0])
    app.run(debug=False, host='0.0.0.0', port=int(sys.argv[1]))
    # app.run(debug=False, port=7001)

