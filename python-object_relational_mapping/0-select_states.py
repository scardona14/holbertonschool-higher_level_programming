#!/usr/bin/python3
"""
Script that lists all states from the databse hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    u_name = argv[1]
    psw = argv[2]
    base = argv[3]

    # Connecting to MySQL database
    db = MySQLdb.connect(host="localhost", user=u_name,
                         passwd=psw, db=base, port=3306)

    # Creating cursor object
    cur = db.cursor()

    # Executing MySql Query
    cur.execute("SELECT * FROM states ORDER BY id")

    # Obtaining Query Result & prints the result in rows
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean Up
    cur.close()
    db.close()