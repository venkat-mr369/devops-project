from flask import Flask, request, jsonify
from flask_cors import CORS
from db import conn

app = Flask(__name__)
CORS(app)

@app.route('/add', methods=['POST'])
def add_data():
    data = request.get_json()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO team_tble(name, city) VALUES (%s, %s)",
        (data['name'], data['city'])
    )
    conn.commit()
    cur.close()
    return jsonify({"msg": "Inserted"})

@app.route('/get', methods=['GET'])
def get_data():
    cur = conn.cursor()
    cur.execute("SELECT name, city FROM team_tble")
    rows = cur.fetchall()
    cur.close()

    return jsonify([
        {"name": r[0], "city": r[1]} for r in rows
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)