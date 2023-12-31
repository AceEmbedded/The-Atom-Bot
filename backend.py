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
   

    # Check if user already exists
    usernames = [u["username"] for u in users]
    if username not in usernames:
        return jsonify({"message": "User dont  exist!"}), 400

    # Get user ID
    user = get_user_by_id(username, password)
    if user is None:
       return jsonify({"message": "User not found or incorrect credentials."}), 400
    print(user)
    return jsonify(user)



if __name__ == '__main__':
    app.run(debug=True)












