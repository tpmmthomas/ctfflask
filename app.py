from flask import Flask, request

app = Flask(__name__)

latest = ""


@app.route("/", methods=["GET"])
def home():
    global latest
    latest += str(request.args)
    return "Hello, World!" + str(latest)


if __name__ == "__main__":
    app.run(debug=True)
