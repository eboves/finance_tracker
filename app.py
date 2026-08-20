from flask import Flask, jsonify, request
from database import get_accounts, get_balances, add_account, add_balance, get_account_by_id

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


################################################### POST ################################################### 


@app.route("/accounts", methods=["POST"])
def post_accounts():

    data = request.json

    if 'name' not in data:
        return jsonify({"message":"Error, name missing"}), 400
    elif 'account_type' not in data:
        return jsonify({"message":"Earror, account_type missing"}),400
    elif 'institution' not in data:
        return jsonify({"message":"Error, institution missing"}),400
    elif 'date_opened' not in data:
        return jsonify({"message":"Error, date_opened missing"}),400
    
    
    name = data['name']
    account_type = data['account_type']
    institution = data['institution']
    date_opened = data['date_opened']
    
    add_account(name=name, account_type=account_type, institution=institution, date_opened=date_opened)
    return jsonify({"message":"Operation Success!", "accounts": data}), 201

@app.route("/balances", methods=["POST"])
def post_balance():
    
    data = request.json

    if "amount" not in data:
        return jsonify({"message":"Error, amount missing"}), 400
    elif "date" not in data:
        return jsonify({"message":"Error, date missing"}),400
    elif "name" not in data:
        return jsonify({"message":"Error, name missing"}),400    

    
    amount = data['amount']
    date = data['date']
    name = data['name']
    
    add_balance(amount=amount, date=date, name=name)
    return jsonify({"message":"Success!", "data": data}), 201


@app.route("/accounts/<int:account_id>")
def get_account_by_id_route(account_id):

    
    account = get_account_by_id(account_id)
    print(account)
    if account is None:
       return jsonify({"Error": "Account not fount withat that id"}), 404
    return jsonify(account)
    # account = get_account_by_id(account_id)




if __name__ == "__main__":
    app.run(debug=True)





# {
#     "amount": 2453.76,
#     "date": "2026-08-18",
#     "name": "retirement roth ira"
# }