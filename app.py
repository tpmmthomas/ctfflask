from flask import Flask, request
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
app = Flask(__name__)
logger = logging.getLogger(__name__)
latest = ""


@app.route("/", methods=["GET", "POST"])
def home():
    logger.info(str(request.args))
    # Do what you need if post
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)
