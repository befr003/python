from flask import Flask,jsonify,request
from sqltest import read_all, add_data, read, update_data

app = Flask(__name__)

@app.route('/client' , methods=['POST'])
def create_client():
    request_data = request.get_json()
    add_data(name=request_data['name'], country=request_data['country'])
    return jsonify(request_data)

@app.route('/client/<string:id>' , methods=['PUT'])
def update_client(id):
    request_data = request.get_json()
#    new_client = {
#        'id':request_data['id'],
#        'name':request_data['name'],
#        'country':request_data['country']
#    }
    update_data(id=request_data['id'],name=request_data['name'],country=request_data['country'])
    return jsonify(request_data)

@app.route('/client/<string:id>')
def get_client(id):
    r = read(id)
    new_item = {
            'id':r[0],
            'name':r[1]
        }
    return jsonify(new_item)


@app.route('/client')
def get_clients():
    retur = []
    for r in read_all():
        new_item = {
            'id':r[0],
            'name':r[1]
        }
        retur.append(new_item)
    return jsonify({'client': retur})

app.run(port=5000)