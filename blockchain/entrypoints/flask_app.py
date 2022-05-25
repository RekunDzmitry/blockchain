from flask import Flask, jsonify, request
from blockchain import bootstrap


app = Flask(__name__)
bus = bootstrap.bootstrap()


@app.route('/mine', methods=['GET'])
def mine():
    return None


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return None

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {}
    return jsonify(response), 200


