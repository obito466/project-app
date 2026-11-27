import os
from flask import Flask, jsonify, render_template

app = Flask(__name__)

STUDENTS = [
    {"id": 1, "name": "Aarav Sharma", "course": "Cloud Computing"},
    {"id": 2, "name": "Sita Gurung", "course": "DevOps"},
    {"id": 3, "name": "Bikash Thapa", "course": "Web Development"},
]


@app.route("/")
def home():
    return render_template("index.html", app_name=os.getenv("APP_NAME", "Project App"))


@app.route("/api/students")
def students():
    return jsonify(STUDENTS)


@app.route("/api/students/<int:student_id>")
def student(student_id):
    for s in STUDENTS:
        if s["id"] == student_id:
            return jsonify(s)
    return jsonify({"error": "Student not found"}), 404


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
