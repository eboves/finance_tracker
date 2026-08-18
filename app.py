from flask import Flask, jsonify, request
from database import get_accounts, get_balances, add_account

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/accounts")
def get_accounts_route():
    accounts = get_accounts()
    return jsonify(accounts)

@app.route("/balances")
def get_balances_route():
    balances = get_balances()
    return jsonify(balances)

@app.route("/accounts", methods=["POST"])
def post_accounts():

    data = request.json
    name = data['name']
    account_type = data['account_type']
    institution = data['institution']
    date_opened = data['date_opened']
    adding_account = add_account(name=name, account_type=account_type, institution=institution, date_opened=date_opened)
    return jsonify({"message":"Operation Success!", "accounts": data}), 201

if __name__ == "__main__":
    app.run(debug=True)
