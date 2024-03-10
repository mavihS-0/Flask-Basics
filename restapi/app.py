from flask import Flask, request, jsonify

app = Flask(__name__)

myData=[
    {'id':0,'title':'wow','value':'shivam'},
    {'id':1,'title':'nice','value':'muzu?'}
]

@app.route('/data', methods=['POST','GET'])
def api():
    if request.method == 'POST':
        data = {}
        data['id'] = myData[-1]['id']+1
        data['title'] = request.form['title']
        data['value'] = request.form['value']
        myData.append(data)
        return jsonify({'data': myData}), 201
    elif request.method == 'GET':
        if request.args.get('id'):
            id = request.args.get('id')
            for data in myData:
                if data['id'] == int(id):
                    return jsonify({'data': data}), 200
            return jsonify({'data': 'Not found'}), 404
        return jsonify({'data': myData}), 200
    elif request.method == 'PUT':
        id = request.form['id']
        for data in myData:
            if data['id'] == int(id):
                data['title'] = request.form['title']
                data['value'] = request.form['value']
                return jsonify({'data': data}), 200
        return jsonify({'data': 'Not found'}), 404
            
    elif request.method == 'DELETE':
        if request.form['id']:
            id = request.form['id']
            for data in myData:
                if data['id'] == int(id):
                    myData.remove(data)
                    return jsonify({'data': myData}), 200
            return jsonify({'data': 'Not found'}), 404

@app.route('/data/<int:id>', methods=['PUT','DELETE'])
def update(id):
    if request.method == 'PUT':
        for data in myData:
            if data['id'] == int(id):
                data['title'] = request.form['title']
                data['value'] = request.form['value']
                return jsonify({'data': myData}), 200
        return jsonify({'data': 'Not found'}), 404
    elif request.method == 'DELETE':
        for data in myData:
            if data['id'] == int(id):
                myData.remove(data)
                return jsonify({'data': myData}), 200
        return jsonify({'data': 'Not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)