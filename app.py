from flask import Flask, jsonify
from database import get_accounts, get_balances

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

if __name__ == "__main__":
    app.run(debug=True)
