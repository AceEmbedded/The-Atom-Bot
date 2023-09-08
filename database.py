

from sqlalchemy import create_engine, Column, String, Integer, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True, default=str(uuid.uuid4()), unique=True)
    email = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)  # Consider hashing before storing

#Solution to Assignment
class Products(Base):
    __tablename__ = 'products'
    id = Column(String, primary_key=True, default=str(uuid.uuid4()), unique=True)
    product_name = Column(String, unique=True)
    product_price = Column(String)
    product_description = Column(String)
    # Consider hashing before storing


class Orders(Base):
    __tablename__ = 'products'
    id = Column(String, primary_key=True, default=str(uuid.uuid4()), unique=True)
    product_name = Column(String, unique=True)
    product_price = Column(String)
    product_description = Column(String)
    # Consider hashing before storing


# class Users(Base):
#     __tablename__ = 'order'
#     id = Column(String, primary_key=True, default=str(uuid.uuid4()), unique=True)
#     email = Column(String, unique=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     password = Column(String)  # Consider hashing before storing


# Connect to PostgreSQL database
engine = create_engine('postgresql://postgres:GbfGbo7L8mHKZozsBqqw@containers-us-west-99.railway.app:5896/railway')


# Create tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Function to add a new user
def add_user(email, first_name, last_name, password):

    try:
        new_user = Users(email=email, first_name=first_name, last_name=last_name, password=password)
        session.add(new_user)
        session.commit()
    except:
        return False

    return True

# Function to get a user by ID
def get_user(user_id):
    user = session.query(Users).filter_by(id=user_id).first()
    return user


# Function to update a user profile
def update_user(user_id, first_name=None, last_name=None):
    user = get_user(user_id)
    if user:
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        session.commit()

# Function to delete a user
def delete_user(user_id):
    user = get_user(user_id)
    if user:
        session.delete(user)
        session.commit()



def login(email, password):
    user = session.query(Users).filter_by(email=email).first()
    if user:
        if user.password == password:  # NOTE: Use hashed passwords in production
            return {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name
            }
        else:
            return "Incorrect password"
    else:
        return "User not found"
    
#Solution to Assignment
# Function to add a new product
def add_product(product_name, product_price, product_description):

    try:
        new_product = Products(product_name=product_name, product_price=product_price, product_description=product_description)
        session.add(new_product)
        session.commit()
    except:
        return False

    return True

# Function to get a product by ID
def get_product(product_id):
    product = session.query(Products).filter_by(id=product_id).first()
    return product

def fetch_all_products():
    try:
        # Query the Products table and fetch all rows
        all_products = session.query(Products).all()
        
        # Convert all_products to a list of dictionaries
        all_products_dict = [
            {
                "id": product.id,
                "product_name": product.product_name,
                "product_price": product.product_price,
                "product_description": product.product_description
            }
            for product in all_products
        ]

        return all_products_dict
      
    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()
        return None


# user = get_user('ef97426d-1128-4f06-9af1-3da88eeb3724')

#delete_user('49917238-6b4c-4f66-9849-1b1462abf86f')


#add_user('john2.doe@example.com', 'John', 'Doe', 'password123')

# print()
# print(user.email)
# print(user.id)
# print(user.password)
# print(user.first_name)
# print(user.last_name)

# update_user(user.id, 'Johnny123', 'Atom')


# print()
# print(user.email)
# print(user.id)
# print(user.password)
# print(user.first_name)
# print(user.last_name)


# user = login("john2.ple.com", "passwordxvb123")
# print(user)
