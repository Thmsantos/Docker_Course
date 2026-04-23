from flask import Flask, jsonify
import requests
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://host.docker.internal:27081/")
db = client["docker_course"]
colecao = db["users_host_network_test"]

@app.route("/", methods=["GET"])
def index():
    data = requests.get('https://randomuser.me/api', timeout=5)
    return data.json()

@app.route("/usuarios", methods=["POST"])
def criar_usuario():
    data = requests.get('https://randomuser.me/api', timeout=5).json()

    result = colecao.insert_one(data['results'][0])

    return jsonify({"id": str(result.inserted_id)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=6000)