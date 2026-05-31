import sqlite3
from flask import Flask, jsonify, request
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE = os.getenv("DATABASE")
DEBUG = os.getenv("DEBUG")

def get_db():
    conn = sqlite3.connect(DATABASE)  # using env variable
    conn.row_factory = sqlite3.Rowd
    return conn



app = Flask(__name__)

def get_db():
    conn = sqlite3.connect("students.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal server error"}), 500

@app.route("/students")
def get_students():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    conn.close()
    return jsonify([dict(s) for s in students])

@app.route("/students/<int:id>")
def get_student(id):
    try:

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id = ?", (id,))
        student = cursor.fetchone()
        conn.close()

        if student:
            return jsonify(dict(student))
        else:
            return jsonify({"error": "Student not found"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/students", metdhods=["POST"])
def add_student():
    data = request.get_json()
    name = data["name"]
    score = data["score"]

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, score) VALUES (?, ?)", (name, score))
    conn.commit()
    conn.close()

    return jsonify({"message": "Student added!"}), 201

@app.route("/")
def home():
    return "Hello from my server!"

@app.route("/about")
def about():
     return "This is my API!"


if __name__ == "__main__":
    app.run(debug=True)
