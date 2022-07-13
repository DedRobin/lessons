from flask import Flask, request, render_template
import logging

from __create_tables import create_current_session
from models import User

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


if __name__ == "__main__":
    app.run()
