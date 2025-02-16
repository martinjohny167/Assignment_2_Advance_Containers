from flask import Flask, request, jsonify
import logging
import os
import psycopg2

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='/app/logs/app.log', level=logging.INFO)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="mydb",
        user="user",
        password="password"
    )
    return conn

# Create user table if it doesn't exist
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL
        )
    ''')
    conn.commit()
    cur.close()
    conn.close()

# API Endpoints
@app.route('/user', methods=['POST'])
def create_user():
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (first_name, last_name) VALUES (%s, %s) RETURNING id', (first_name, last_name))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    logging.info(f"User created: {user_id}")
    return jsonify({"id": user_id, "first_name": first_name, "last_name": last_name}), 201

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, first_name, last_name FROM users WHERE id = %s', (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    if user:
        logging.info(f"User fetched: {user_id}")
        return jsonify({"id": user[0], "first_name": user[1], "last_name": user[2]})
    else:
        logging.warning(f"User not found: {user_id}")
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)