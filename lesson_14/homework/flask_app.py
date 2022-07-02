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
        some_user = User(email=request.form.get("email"), password=request.form.get(""))
        dictionary = request.form.to_dict()
        string = dict_to_str(dictionary)
        logger.info(string)
        return string

    dictionary = request.args.to_dict()
    string = dict_to_str(dictionary)
    logger.info(string)
    return string


@app.route("/test", methods=["GET"])
def test():
    return "Test URL"


if __name__ == "__main__":
    app.run()
