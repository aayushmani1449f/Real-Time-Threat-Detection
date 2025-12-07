from scapy.all import sniff, IP, TCP, UDP
from collections import defaultdict
import time
from app import socketio, app
from db import insert_incident

# Track packet count per IP
packet_count = defaultdict(int)
last_reset = time.time()

THRESHOLD = 200  # packets per minute (you can tweak)
SCAN_PORT_LIMIT = 10  # number of unique ports hit from a single IP

ip_ports = defaultdict(set)

def detect_attack(pkt):
    global last_reset

    if not pkt.haslayer(IP):
        return

    src_ip = pkt[IP].src
    dst_ip = pkt[IP].dst
    packet_count[src_ip] += 1

    # Track destination ports for port scan detection
    if pkt.haslayer(TCP) or pkt.haslayer(UDP):
        dport = pkt[TCP].dport if pkt.haslayer(TCP) else pkt[UDP].dport
        ip_ports[src_ip].add(dport)

    now = time.time()

    # Reset counts every 60 seconds
    if now - last_reset > 60:
        packet_count.clear()
        ip_ports.clear()
        last_reset = now

    # Rule 1: DDoS detection
    if packet_count[src_ip] > THRESHOLD:
        report_attack(src_ip, dst_ip, "DDoS Attack", f"{packet_count[src_ip]} packets in 60 seconds")

    # Rule 2: Port scan detection
    if len(ip_ports[src_ip]) > SCAN_PORT_LIMIT:
        report_attack(src_ip, dst_ip, "Port Scan", f"Accessed {len(ip_ports[src_ip])} unique ports")

def report_attack(src_ip, dst_ip, attack_type, details):
    with app.app_context():
        insert_incident(src_ip, dst_ip, attack_type, details)

        alert = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "src_ip": src_ip,
            "dst_ip": dst_ip,
            "type": attack_type,
            "details": details,
        }

        socketio.emit("new_alert", alert, namespace="/")
        print(f"🚨 ALERT: {attack_type} from {src_ip} → {dst_ip} | {details}")

def start_sniffing():
    print("🔍 Starting packet sniffing... (press CTRL+C to stop)")
    sniff(prn=detect_attack, store=0)

if __name__ == "__main__":
    start_sniffing()
