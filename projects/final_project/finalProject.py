import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=["GET"])
def home():
    return
    "<h1>Making an API</h1><p>This site makes an API</p>"