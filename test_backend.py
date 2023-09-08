import requests
import json

# Specify the URL for the POST request
register_url = 'http://127.0.0.1:5000/register'
login_url = 'http://127.0.0.1:5000/login'
#Solution to Assignment
inventory_url = 'http://127.0.0.1:5000/inventory'
products_url ='http://127.0.0.1:5000/products'




###REGISTER
# Create a dictionary with the data you want to send
payload = {
    'username': 'my_username',
    'password': 'my_password',
    'first_name': 'John',
    'last_name': 'Doe'
}


###Solution to Assignment
payload = {
    'product_name': 'ace_lamp',
    'product_price': '$100',
    'product_description': 'This is an ACE_Embedded Lamp'
}
# # Make the POST request with JSON data
response = requests.get(products_url)
print(response.text)

# print(response.text)
# response_data = json.loads(response.text)
# print(response_data["message"])

######LOGIN
# Create a dictionary with the data you want to send
# payload = {
#     'username': 'my_username',
#     'password': 'my_password',
 #  'first_name': 'John',
# 'last_name': 'Doe'
#}

# Make the POST request with JSON data
# response = requests.get(login_url, json=payload)

# print(response.text)
# response_data = json.loads(response.text)


# print(response_data)
