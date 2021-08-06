#!/usr/bin/python3
"""
This module lists all states starting with N
"""
import sys
import MySQLdb

if __name__ == "__main__":
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    uinput_state = sys.argv[4]
    state_list = []
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=u, passwd=p, db=d, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM \
    cities JOIN states ON \
    state_id=states.id WHERE \
    states.name = %(state)s", {'state': uinput_state})
    query_rows = cur.fetchall()
    print(", ".join([i[0] for i in query_rows]))
    cur.close()
    conn.close()
