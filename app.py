from flask import Flask, request, jsonify
from flask_cors import CORS
from config import get_connection

app = Flask(__name__)
CORS(app)


# ✅ Root Route
@app.route("/")
def home():
    return "Hospital Backend is Running Successfully 🚀"


# ✅ GET All Patients
@app.route("/patients", methods=["GET"])
def get_patients():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM patients")

        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        data = [dict(zip(columns, row)) for row in rows]

        cursor.close()
        connection.close()

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ✅ Add Patient
@app.route("/patients", methods=["POST"])
def add_patient():
    try:
        data = request.json
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO patients (name, age, gender, disease)
        VALUES (%s, %s, %s, %s)
        RETURNING id
        """

        cursor.execute(query, (
            data['name'],
            data['age'],
            data['gender'],
            data['disease']
        ))

        new_id = cursor.fetchone()[0]
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({
            "message": "Patient added successfully",
            "id": new_id
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ✅ Update Patient
@app.route("/patients/<int:id>", methods=["PUT"])
def update_patient(id):
    try:
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

        cursor.close()
        connection.close()

        return jsonify({"message": "Patient updated successfully"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ✅ Delete Patient
@app.route("/patients/<int:id>", methods=["DELETE"])
def delete_patient(id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("DELETE FROM patients WHERE id=%s", (id,))
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({"message": "Patient deleted successfully"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)