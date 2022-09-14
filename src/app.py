from flask import Flask
from flask_restful import Resource, Api

from src.resources.generator import Generator

app = Flask(__name__)
api = Api(app)

api.add_resource(Generator, '/generate')

if __name__ == '__main__':
    app.run(debug=True)