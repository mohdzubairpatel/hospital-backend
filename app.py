from flask import Flask, request, jsonify
from flask_cors import CORS
from config import get_connection

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Hospital Backend is Running Successfully 🚀"

@app.route("/patients", methods=["GET"])
def get_patients():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM patients")
    data = cursor.fetchall()
    connection.close()
    return jsonify(data)

@app.route("/patients", methods=["POST"])
def add_patient():
    data = request.json
    connection = get_connection()
    cursor = connection.cursor()

    query = "INSERT INTO patients (name, age, gender, disease) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (data['name'], data['age'], data['gender'], data['disease']))
    connection.commit()
    connection.close()

    return jsonify({"message": "Patient added successfully"})

@app.route("/patients/<int:id>", methods=["PUT"])
def update_patient(id):
    data = request.json
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    UPDATE patients
    SET name=%s, age=%s, gender=%s, disease=%s
    WHERE id=%s
    """

    cursor.execute(query, (
        data['name'],
        data['age'],
        data['gender'],
        data['disease'],
        id
    ))

    connection.commit()
    connection.close()

    return jsonify({"message": "Patient updated successfully"})

@app.route("/patients/<int:id>", methods=["DELETE"])
def delete_patient(id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM patients WHERE id=%s", (id,))
    connection.commit()
    connection.close()

    return jsonify({"message": "Patient deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)