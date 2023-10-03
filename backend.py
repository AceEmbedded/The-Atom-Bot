from flask import Flask, request, jsonify
import uuid
from database import add_user
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

def get_user_by_id(username, password):
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    return None  # Return None if no user is found


@app.route('/register', methods=['POST']) #one endpoint/route
def register():
    data = request.json
    username = data['username']
    password = data['password']
    first_name = data['first_name']
    last_name = data['last_name']

    sucess = add_user(username,first_name, last_name, password)
    if sucess == True:
        user=database.login(username,password)
        return jsonify(user)
    
    elif sucess==False:
        return jsonify({"message": "error!"}), 400


@app.route('/', methods=['GET']) #one endpoint/route
def home():
    return jsonify({"message": "Hello there!"})


@app.route('/login', methods=['GET']) #one endpoint/route
def login():
    data = request.json
    username = data['username']
    password = data['password']
    user=database.login(username,password)
    if isinstance(user,str):
        return jsonify({"message": user})
    return jsonify(user)

#Add-Product

#functions
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
    

    sucess = add_product(product_name,product_price, product_description)
    if sucess == True:
        return jsonify(product_name)
    
    elif sucess==False:
        return jsonify({"message": "error!"}), 400    

#Add order
# Dummy data for products and orders (you should replace this with a database)
products = [
    {"id": 1, "product_name": "Product 1", "product_price": 10.0},
    {"id": 2, "product_name": "Product 2", "product_price": 15.0},
    {"id": 3, "product_name": "Product 3", "product_price": 20.0},
]

orders = []

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_order', methods=['POST'])
def add_order_route():
    product_id = int(request.form['product_id'])
    quantity = int(request.form['quantity'])

    # Find the selected product
    product = next((p for p in products if p['id'] == product_id), None)

    if product:
        order = {
            "product_id": product['id'],
            "product_name": product['name'],
            "quantity": quantity,
            "total_price": quantity * product['price']
        }
        orders.append(order)
        print("Order submitted successfully!")
        return redirect(url_for('index'))
    else:
        return "Product not found", 404



@app.route('/view_orders')
def view_orders():
    return render_template('view_orders.html', orders=orders)

@app.route('/success')
def success():
    return "Order submitted successfully!"


if __name__ == '__main__':
    app.run(debug=True)












