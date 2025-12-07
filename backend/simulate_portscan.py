# backend/simulate_portscan.py
import sys, time
from scapy.all import IP, TCP, send

def port_scan(target="127.0.0.1", start=20, end=200, delay=0.01):
    print(f"Scanning {target} ports {start}..{end} (delay={delay}s)")
    for p in range(start, end+1):
        pkt = IP(dst=target)/TCP(dport=p, flags="S")  # SYN
        send(pkt, verbose=0)
        if p % 25 == 0:
            print(f"scanned up to port {p}")
        time.sleep(delay)
    print("Port scan finished.")

if __name__ == "__main__":
    tgt = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    s = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    e = int(sys.argv[3]) if len(sys.argv) > 3 else 120
    d = float(sys.argv[4]) if len(sys.argv) > 4 else 0.01
    port_scan(tgt, s, e, d)
