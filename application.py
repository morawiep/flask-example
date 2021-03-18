from flask import Flask, request, render_template

application = Flask(__name__)

@application.route("/")
def index():
    return 'Hello world', 200

application.run()
