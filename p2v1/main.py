from flask import Flask, render_template, request, stream_with_context, Response
from time import sleep
# from pprint import pprint

import os
import sys


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

    return render_template("directions.html")


@app.route('/', methods=['POST'])
def my_form_post():

    source = request.form['source']
    destination = request.form['destination']

    path = "/Users/srinivasrishindra/IdeaProjects/DistributedProjectTwo/p2v1/"
    print("Source is ", source)
    print("destination is ", destination)

    #os.system(source + " > " + path + "/" + destination)

    text_file = open(path + destination, "w")

    text_file.write(source)

    text_file.close()

    os.system("sh /Users/srinivasrishindra/IdeaProjects/DistributedProjectTwo/p2v1/rundocker.sh")

    return render_template("directions_stream.html")


@app.route('/stream')
def stream():
    def generate():
        # with open('job.log') as f:
        with open('/Users/srinivasrishindra/IdeaProjects/DistributedProjectTwo/p2v1/logfile.txt') as f:
            while True:
                yield f.read()
                sleep(1)

    return Response(stream_with_context(generate()))


if __name__ == "__main__":
    app.run(debug=False, port=9000)
