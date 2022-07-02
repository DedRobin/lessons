from flask import Flask, request, render_template
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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


@app.route("/test", methods=["GET"])
def test():
    return "Test URL"


if __name__ == "__main__":
    app.run()
