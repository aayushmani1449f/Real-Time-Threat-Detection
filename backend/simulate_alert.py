import time
from app import socketio, app
from db import insert_incident

def simulate_alert():
    with app.app_context():
        sample_data = [
            ("192.168.1.101", "192.168.1.10", "DDoS Attack", "High packet rate detected"),
            ("192.168.1.150", "192.168.1.12", "Port Scan", "Multiple ports accessed quickly"),
            ("10.0.0.8", "10.0.0.2", "Suspicious Activity", "Repeated malformed packets"),
        ]

        for src, dst, type_, details in sample_data:
            insert_incident(src, dst, type_, details)

            # Emit to connected Socket.IO clients
            socketio.emit("new_alert", {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "src_ip": src,
                "dst_ip": dst,
                "type": type_,
                "details": details,
            }, namespace="/")

            print(f"🚨 Alert sent: {type_} from {src}")
            time.sleep(3)

if __name__ == "__main__":
    print("🔄 Simulating alerts... make sure Flask app is running.")
    socketio.start_background_task(simulate_alert)
    socketio.run(app, host="0.0.0.0", port=5001)
