from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    print(request.args)
    return "Hello, World!" + str(request.args)


if __name__ == "__main__":
    app.run(debug=True)
