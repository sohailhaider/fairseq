import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return 'welcom aboard'
    

app.run('0.0.0.0', 8080)