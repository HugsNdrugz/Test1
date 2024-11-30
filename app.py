
from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'data.db'  # Path to your SQLite database

# Function to connect to SQLite database
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Access rows as dictionaries
    return conn

# API Endpoint: Fetch Chat Messages
@app.route('/api/chat_messages', methods=['GET'])
def get_chat_messages():
    conn = get_db_connection()
    messages = conn.execute('SELECT * FROM ChatMessages ORDER BY time ASC').fetchall()
    conn.close()
    return jsonify([dict(msg) for msg in messages])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
