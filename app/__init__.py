from flask import Flask

# create the flask app instance
app = Flask(__name__)

# route imports
from app import routes_base

# api route imports
