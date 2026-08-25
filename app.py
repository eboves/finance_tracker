from flask import Flask, jsonify, request
from database import get_accounts, get_balances, add_account, add_balance, get_account_by_id, update_account_by_id, delete_account_by_id, update_balance_by_id, get_balance_by_id, delete_balance_by_id

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
       return jsonify({"Error": "Account not fount with that id"}), 404
    return jsonify(account)
    # account = get_account_by_id(account_id)


################################################### PUT ################################################### 

@app.route("/accounts/<int:account_id>", methods=["PUT"])
def update_account_using_id(account_id):

    data = request.json
    if 'name' not in data:
       return jsonify({"message": "name is missing"}), 400
    if 'account_type' not in data:
        return jsonify({"message": "account_type is missing"}), 400
    if 'institution' not in data:
        return jsonify({"message": "institution is missing"}), 400
    if 'date_opened' not in data:
        return jsonify({"message": "date_opened is missing"}), 400
    
    name = data['name']
    account_type = data['account_type']
    institution = data['institution']
    date_opened = data['date_opened']

    update_account_by_id(name=name, account_type=account_type, institution=institution, date_opened=date_opened, id=account_id)
    return jsonify({"message":"SUCCESSFUL!", "data": data}), 200



################################################### PATCH ################################################### 

@app.route("/accounts/<int:account_id>", methods = ["PATCH"])
def update_account_using_patch(account_id):

    existing = get_account_by_id(account_id=account_id)
    print(existing)
    if existing is None:
        return jsonify({"message": "None account exist with that account_id"}), 404

    data = request.get_json()  
    print(data)

    name = data.get('name', existing['name'])
    account_type = data.get('account_type', existing['account_type'])
    institution = data.get('institution', existing['institution'])
    date_opened = data.get('date_opened', existing['date_opened'])


    # if not data:
    #     return jsonify({"message": "Error occured while loading data"}), 404
    
    update_account_by_id(name=name, account_type=account_type, institution=institution, date_opened=date_opened, id=account_id)
    return jsonify({"message": "SUCCESS!", "data": data}), 200
    

################################################### DELETE ################################################### 

@app.route("/accounts/<int:account_id>", methods=["DELETE"])
def delete_item_using_account_id(account_id):
    deleted_account = delete_account_by_id(account_id=account_id)
    if deleted_account == 0:
        return "", 404
    else:
        return "", 204



################################################### BALANCE ################################################### 



@app.route("/balances/<int:acc_id>", methods=["PUT"])
def update_balance_by_using_id(acc_id):

    data = request.json

    if 'date' not in data:
        return jsonify({"message": "date is missing"}), 400
    if 'amount' not in data:
        return jsonify({"message": "amount is misisng"}), 400
    if 'account_id' not in data:
        return jsonify({"message": "account_id is missing"}), 400

    date = data['date']
    amount = data['amount']
    account_id = data['account_id']

    update_balance_by_id(id=acc_id,date=date, amount=amount, account_id=account_id)
    return jsonify({"message":"SUCCESS!", "data": data}), 200



@app.route('/balances/<int:balance_id>')
def get_balance_using_id(balance_id):

    balance_by_id = get_balance_by_id(balance_id=balance_id)
    print(balance_by_id)
    if not balance_by_id:
        return jsonify({"message": "item was not found"}), 404
    return jsonify(balance_by_id)

@app.route('/balances/<int:balance_id>', methods=["PATCH"])
def patch_balance_by_using_id(balance_id):

    data = request.get_json()

    existing = get_balance_by_id(balance_id=balance_id)
    if not existing:
        return jsonify({"message":"this item could not be found"}), 404
    date = data.get('date', existing['date'])
    amount = data.get('amount', existing['amount'])
    account_id = data.get('account_id', existing['account_id'])

    update_balance_by_id(balance_id, date=date, amount=amount, account_id=account_id)
    return jsonify({"message": "SUCCESS!"}), 200

@app.route("/balances/<int:balance_id>", methods=["DELETE"])
def delete_balance_by_using_id(balance_id):
    deleted_balance = delete_balance_by_id(balance_id=balance_id)
    if deleted_balance == 0:
        return "", 404
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)





# {
#     "amount": 2453.76,
#     "date": "2026-08-18",
#     "name": "retirement roth ira"
# }

# {
#   "message": "institution is missing"
# }


# {
#   "name":"401K",
#   "account_type": "savings",
#   "institution": "job",
#   "date_opened": "2026-11-08"
# }