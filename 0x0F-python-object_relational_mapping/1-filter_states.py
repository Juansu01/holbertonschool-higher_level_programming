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
    conn = MySQLdb.connect(
        host="localhost", port=3306, user=u, passwd=p, db=d, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name like 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1][0] == 'N':
            print(row)
    cur.close()
    conn.close()
