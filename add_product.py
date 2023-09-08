from flask import Flask, request, jsonify
import uuid
from database import add_product
import database

app = Flask(__name__)

# In-memory database
users = []
products = []
orders = []
appointments = []

# functions
def generate_unique_id():
    return str(uuid.uuid4())

def get_product_by_id(product_name):
    for product in products:
        if product['product_name'] == product_name:
            return product
    return None  # Return None if no product is found

@app.route('/inventory', methods=['POST']) #one endpoint/route
def inventory():
    data = request.json
    product_name = data['product_name']
    product_price = data['product_price']
    product_description = data['product_description']
    

    success = add_product(product_name,product_price, product_description)
    if success == True:   
        return jsonify(product_name)
    
    elif success==False:
        return jsonify({"message": "error!"}), 400
    


if __name__ == '__main__':
    app.run(debug=True)