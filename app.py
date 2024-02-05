from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'HEAD'])
def api():
    if request.method == 'GET':
        return jsonify({'method': 'GET'})
    elif request.method == 'POST':
        return jsonify({'method': 'POST'})
    elif request.method == 'HEAD':
        return jsonify({'method': 'HEAD'})
    else:
        return jsonify({'method': 'UNKNOWN'})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)