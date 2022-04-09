from flask import Flask, request, jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
import db
from flask_cors import CORS
import pymongo

app = Flask(__name__)
CORS(app)

# crud pacientes
# create
@app.route("/ingreso", methods=['POST'])
def ingreso():
    data = request.get_json()
    cliente = db.get_connection()
    infoHospitalaria = cliente.infoHospitalaria
    infoHospitalaria.pacientes.insert_one(data)
    return data
# read
@app.route("/paciente/<identificacion>", methods=['GET'])
def paciente(identificacion):
    cliente = db.get_connection()
    infoHospitalaria = cliente.infoHospitalaria
    paciente = infoHospitalaria.pacientes.find_one({"_id": identificacion})
    return jsonify(paciente)
# update
@app.route("/paciente/<identificacion>", methods=['PUT'])
def update(identificacion):
    cliente = db.get_connection()
    infoHospitalaria = cliente.infoHospitalaria
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    data = request.get_json()
    try:
        paciente = infoHospitalaria.pacientes
        print("bbbbbbbbbbbbbbbbbbbbbbbbbb")
        paciente.replace_one(
            {'_id': identificacion},
            data, True
        )
        return jsonify({"message":"OK"})
    finally:
        cliente.close()
        print("Connection closed")
# delete
@app.route("/paciente/<identificacion>", methods=['DELETE'])
def delete(identificacion):
    cliente = db.get_connection()
    infoHospitalaria = cliente.infoHospitalaria
    try:
        pacientes = infoHospitalaria.pacientes
        pacientes.delete_one({'_id': identificacion})
        return jsonify({"message":"OK"})
    finally:
        cliente.close()
        print("Connection closed")

# crud medicos
# create
@app.route("/ingresoMedico", methods=['POST'])
def ingresoMedico():
    data = request.get_json()
    cliente = db.get_connection()
    infoHospitalaria = cliente.infoHospitalaria
    infoHospitalaria.medicos.insert_one(data)
    return data
# read
@app.route("/medico/<identificacion>", methods=['GET'])
def medico(identificacion):
    cliente = db.get_connection()
    infoHospitalaria = cliente.infoHospitalaria
    medico = infoHospitalaria.medicos.find_one({"_id": identificacion})
    return jsonify(medico)
# update
@app.route("/medico/<identificacion>", methods=['PUT'])
def updateMedico(identificacion):
    cliente = db.get_connection()
    infoHospitalaria = cliente.infoHospitalaria
    print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    data = request.get_json()
    try:
        medico = infoHospitalaria.medicos
        print("bbbbbbbbbbbbbbbbbbbbbbbbbb")
        medico.replace_one(
            {'_id': identificacion},
            data, True
        )
        return jsonify({"message":"OK"})
    finally:
        cliente.close()
        print("Connection closed")
# delete
@app.route("/medico/<identificacion>", methods=['DELETE'])
def deleteMedico(identificacion):
    cliente = db.get_connection()
    infoHospitalaria = cliente.infoHospitalaria
    try:
        medico = infoHospitalaria.medicos
        medico.delete_one({'_id': identificacion})
        return jsonify({"message":"OK"})
    finally:
        cliente.close()
        print("Connection closed")
