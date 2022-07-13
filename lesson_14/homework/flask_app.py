from flask import Flask, request, render_template
import logging

from __create_tables import create_current_session
from models import *

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
current_session = create_current_session()


def dict_to_str(data: dict) -> str:
    return " " + ", ".join(f"{key} : {value}" for key, value in data.items())


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        dictionary = request.form.to_dict()
        string = dict_to_str(dictionary)
        logger.info(string)
        return string

    dictionary = request.args.to_dict()
    string = dict_to_str(dictionary)
    logger.info(string)
    return string


@app.route("/create_user", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        name = request.form.get("name")
        phone = request.form.get("phone")
        age = request.form.get("age")
        city = request.form.get("city")
        address = request.form.get("address")

        user = User(email=email, password=password)
        profile = Profile(user=user, name=name, phone=phone, age=age)
        address = Address(user=user, city=city, address=address)

        data = (user, profile, address)

        current_session.add_all(data)
        current_session.commit()

        return f"Create user: {user.email}"

    return "It's GET-method!"


@app.route("/get_<column>", methods=["GET"])
def get_user(column):
    result = "Not matches."
    if column == "users":
        result = current_session.query(User).all()
        result = [(u.id, u.email) for u in result]
        return f"{result}"
    elif column == "addresses":
        result = current_session.query(Address).all()
        result = [(a.id, a.address, a.user.id) for a in result]
        return f"{result}"
    elif column == "profiles":
        result = current_session.query(Profile).all()
        result = [(p.id, p.name, p.phone, p.age, p.user.id) for p in result]
        return f"{result}"
    elif column == "products":
        result = current_session.query(Product).all()
        result = [(p.id, p.product_name, p.price, p.product_quantity) for p in result]
        return f"{result}"
    elif column == "purchases":
        result = current_session.query(Purchase).all()
        result = [(p.id, p.purchase_quantity, p.user.id, p.product.id) for p in result]
        return f"{result}"
    else:
        return result


if __name__ == "__main__":
    app.run()
