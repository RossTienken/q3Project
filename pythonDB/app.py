from flask import request, jsonify, url_for, redirect, g, send_file
from models import Drawings
from sqlalchemy.exc import IntegrityError
from index import app, db
from modelHandler import addNewModel, getModel, getAllModels
import csv
import ast

@app.route('/api/model', methods=['POST'])
def addModel():
    data = request.get_json()
    alreadyExists = getModel(data['name'])
    if not alreadyExists:
        addNewModel(data['data'], data['name'])
        packet = {'response': 'all good'}
        return jsonify(packet)
    return jsonify({'error': 'Name Already Exists'})

@app.route('/api/model/<data>', methods=['GET'])
def getModelRoute(data):
    array = []
    fileName = getModel(data)
    with open(fileName, 'r') as file:
        read = csv.reader(file, delimiter=',', quotechar='|')
        reader = iter(read)
        next(reader)
        next(reader)
        for line in reader:
            holder = [float(line[0]), float(line[1]), float(line[2]), ast.literal_eval(line[3]), float(line[4])]
            array.append(holder)
    return jsonify({'data': array})

@app.route('/api/models', methods=['GET'])
def getAllModelRoute():
    data = getAllModels()
    return jsonify({'data': data})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, threaded = True)
