from flask import Flask, render_template, request, redirect, url_for , request, jsonify
import uuid
import database
from database import add_order


app = Flask(__name__)

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
