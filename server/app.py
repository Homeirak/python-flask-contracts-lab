#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [
    {"id": 1, "contract_information": "This contract is for John and building a shed"},
    {"id": 2, "contract_information": "This contract is for a deck for a buisiness"},
    {"id": 3, "contract_information": "This contract is to confirm ownership of this car"}
]
customers = ["bob","bill","john","sarah"]

app = Flask(__name__)

# Route: GET /contract/<id>
# Returns contract information if ID is found, else 404
@app.route('/contract/<int:id>', methods=['GET'])
def get_contract(id):
    for contract in contracts:
        if contract["id"] == id:
            response_text = f'Contract Info: {contract["contract_information"]}'
            return make_response(response_text, 200)
            # alternatively, from flask import jsonify and use:
            # return jsonify(contract), 200
    return make_response({"error":"Contract not found"}, 404)

# Route: GET /customer/<customer_name>
# Returns 204 if customer exists (no data returned), else 404
@app.route('/customer/<string:customer_name>', methods=['GET'])
def get_customer(customer_name):
    if customer_name.lower() in customers:
        return make_response('', 204)
    return make_response({"error":"Customer not found"}, 404)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
