from flask import Flask, request, jsonify, abort
from flask_cors import CORS

app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

matkul = [
    {
        'id': 0,
        'course': 'Algoritma Pemrograman 1',
        'lect': 'MN Fakhruzzaman',
        'code': 'SIA107'
    },
    {
        'id': 1,
        'course': 'Algoritma Pemrograman 2',
        'lect': 'MN Fakhruzzaman',
        'code': 'SIA206'
    },
    {
        'id': 2,
        'course': 'Metodologi Penelitian dan Statistik',
        'lect': 'MN Fakhruzzaman',
        'code': 'PNG687'
    }
]

@app.route("/", methods=['GET'])
def home():
    return '<h1>THIS API WORKS!!!!</h1>'

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/matkul/all', methods=['GET'])
def api_all():
    return jsonify(matkul)

@app.route('/api/v1/resources/matkul', methods=['POST'])
def req_matkul():
    if not request.json or not 'id' in request.json:
        abort(400)
    else:
        results = []
        data = request.get_json()
        for mk in matkul:
            if matkul['id'] == data['id']:
                results.append(mk)
        return jsonify(results), 201
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
