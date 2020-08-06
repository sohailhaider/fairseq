import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True
@app.route('/', methods=['POST'])

def pharaphrase():
    jsonData = request.get_json(force=True);
    if jsonData and jsonData['sentence']:
        print(jsonData['sentence'])
        
        
        
        return jsonify(jsonData['sentence'])
    else:
        return jsonify({'error':'\'sentence\' is required'})
    
app.run('0.0.0.0', 6000)