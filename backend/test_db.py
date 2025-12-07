# backend/test_db.py

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # add backend folder to import path

from db import init_db, insert_incident, get_recent_incidents


def test():
    print("Initializing database...")
    init_db()
    print("Inserting sample incident...")
    insert_incident("192.168.1.100", "192.168.1.1", "Test Attack", "Sample log entry for testing.")
    print("Fetching recent incidents...")
    incidents = get_recent_incidents()
    for inc in incidents:
        print(inc)


if __name__ == "__main__":
    test()

