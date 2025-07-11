from flask import Flask, jsonify, request
from person_dao import Person, Db_operations

app = Flask(__name__)

db_ops = Db_operations()
db_ops.create_db()
db_ops.create_table()

@app.route('/person', methods=['POST'])
def person_create():
    body = request.get_json()
    new_person = Person(body['name'], body['gender'], body['dob'], body['location'])
    person_id = db_ops.insert_row(new_person)
    person = db_ops.search_row(person_id)
    person_dict = {'id': person[0], 'name': person[1], 'gender': person[2], 'dob': person[3], 'location': person[4]}
    return jsonify(person_dict)

@app.route('/person/<int:id>', methods=['GET'])
def person_read_by_id(id):
    person = db_ops.search_row(id)
    if person is None:
        return jsonify({"message": "Person not found"}), 404
    person_dict = {'id': person[0], 'name': person[1], 'gender': person[2], 'dob': person[3], 'location': person[4]}
    return jsonify(person_dict)

@app.route('/person', methods=['GET'])
def person_read_all():
    person_list = db_ops.list_all_rows()
    person_dict = [{'id': person[0], 'name': person[1], 'gender': person[2], 'dob': person[3], 'location': person[4]} for person in person_list]
    return jsonify(person_dict)

@app.route('/person/<int:id>', methods=['PUT'])
def person_update(id):
    body = request.get_json()
    old_person = db_ops.search_row(id)
    if not old_person:
        return jsonify({'message': 'Person not found'}), 404
    updated_person = (body['name'], body['gender'], body['location'], body['dob'], id)
    db_ops.update_row(updated_person)
    person = db_ops.search_row(id)
    person_dict = {'id': person[0], 'name': person[1], 'gender': person[2], 'dob': person[3], 'location': person[4]}
    return jsonify(person_dict)

@app.route('/person/<int:id>', methods=['DELETE'])
def person_delete(id):
    old_person = db_ops.search_row(id)
    if not old_person:
        return jsonify({'message': 'Person not found'}), 404
    db_ops.delete_row(id)
    return jsonify({'message': 'Person deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
