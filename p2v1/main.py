from flask import Flask, render_template, request, stream_with_context, Response
from time import sleep
import os
import sys


"""
Initializes Flask
"""
app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))


@app.route('/')
def my_form():
    """
    :return: html for entering the source code.
    """

    return render_template("directions.html")


@app.route('/', methods=['POST'])
def my_form_post():
    """
    write the code to a file and build a docker image to run the code in that file.
    :return: output of docker build and docker running html for entering the source code.
    """

    source = request.form['source']
    destination = request.form['destination']

    path = "/Users/srinivasrishindra/IdeaProjects/DistributedProjectTwo/p2v1/"
    print("Source is ", source)
    print("destination is ", destination)

    text_file = open(path + "app.py", "w")
    # text_file = open(path + destination, "w")

    text_file.write(source)

    text_file.close()

    os.system("sh /Users/srinivasrishindra/IdeaProjects/DistributedProjectTwo/p2v1/rundocker.sh")

    return render_template("directions_stream.html")


@app.route('/stream')
def stream():
    """
    code to stream the output of the docker log file to browser
    :return: stream the logs to the browser
    """
    def generate():
        # with open('job.log') as f:
        with open('/Users/srinivasrishindra/IdeaProjects/DistributedProjectTwo/p2v1/logfile.txt') as f:
            while True:
                yield f.read()
                sleep(1)

    return Response(stream_with_context(generate()))


if __name__ == "__main__":
    """
    code to run the flask app 
    """
    app.run(debug=False, port=9000)
