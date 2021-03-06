#!/usr/bin/python3
import MySQLdb
import sys
"""
Script list all states from database starting with "N"
"""


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id\
    ASC")
    for row in cur:
        if row[1][0] == 'N':
            print("{}".format(row))
    cur.close()
    db.close()
