# backend/app.py
from flask import Flask, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
from db import get_recent_incidents, insert_incident, init_db

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Use threading mode for better Windows compatibility
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

# Initialize the SQLite database
init_db()

@app.route("/api/incidents")
def incidents():
    """Return recent security incidents."""
    data = get_recent_incidents()
    return jsonify([
        {
            "id": row[0],
            "timestamp": row[1],
            "src_ip": row[2],
            "dst_ip": row[3],
            "type": row[4],
            "details": row[5]
        }
        for row in data
    ])

@app.route("/api/test-alert")
def test_alert():
    """Insert a sample alert and emit it via SocketIO."""
    sample_alert = {
        "src_ip": "192.168.1.100",
        "dst_ip": "192.168.1.1",
        "type": "Port Scan",
        "details": "Multiple ports accessed within 5 seconds."
    }

    # Save alert to database
    insert_incident(sample_alert["src_ip"], sample_alert["dst_ip"],
                    sample_alert["type"], sample_alert["details"])

    # Emit real-time alert to connected dashboard
    socketio.emit("new_alert", sample_alert)

    return jsonify({"status": "✅ Alert emitted successfully!", "alert": sample_alert})


if __name__ == "__main__":
    print("🚀 Starting Flask-SocketIO server on http://127.0.0.1:5000 ...")
    socketio.run(app, host="127.0.0.1", port=5000, debug=True)
