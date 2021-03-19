from flask import Flask
from flask_restful import Api
from resources.item import Item

application = Flask(__name__)
api = Api(application)

@application.route('/')
def index():
    return "First page"

api.add_resource(Item, '/item')

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()
