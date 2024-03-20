#!/usr/bin/python3
"""
Script that lists all states with a name starting with N
from the databse hbtn_0e_0_usa
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    u_name = argv[1]
    psw = argv[2]
    base = argv[3]
    state = argv[4]

    # Connecting to MySQL database
    db = MySQLdb.connect(host="localhost", user=u_name,
                         passwd=psw, db=base, port=3306)

    # Creating cursor object
    cur = db.cursor()

    # Executing MySql Query
    cur.execute("SELECT name FROM cities WHERE state_id = \
                (SELECT id FROM states WHERE name = '{}')\
                ORDER BY id".format(state))

    # Obtaining Query Result & prints the result in rows
    rows = cur.fetchall()
    lis = []
    for row in rows:
        lis.append(row[0])
    print(', '.join(lis))

    # Clean Up
    cur.close()
    db.close()