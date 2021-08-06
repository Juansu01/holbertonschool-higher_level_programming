#!/usr/bin/python3
"""
This module lists all states
"""
import sys
import MySQLdb

if __name__ == "__main__":
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=u, passwd=p, db=d, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, \
    cities.name, states.name \
    FROM cities JOIN states ON state_id=states.id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
