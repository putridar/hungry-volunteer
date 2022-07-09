from doctest import DocFileSuite
import os
import pickle
from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import sys
sys.path.append('./scripts')
from flask import Flask, jsonify, request
import scrape

app = Flask(__name__)
CORS(app)
api = Api(app)

@app.route('/scrape',methods = ['POST', 'GET'])
def get_result():
    result = ''
    if request.method == 'POST':
        name = request.get_json().get('name')
        # get dataframe that contains reviews from google
        links = scrape.run(name)
    return jsonify(links)

if __name__ == "__main__":
  app.run(debug=True)
