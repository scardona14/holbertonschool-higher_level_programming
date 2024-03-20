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
    search = argv[4]

    # Connecting to MySQL database
    db = MySQLdb.connect(host="localhost", user=u_name,
                         passwd=psw, db=base, port=3306)

    # Creating cursor object
    cur = db.cursor()

    proc = ({search},)
    # Executing MySql Query
    query = "SELECT * FROM states WHERE name LIKE BINARY %s"
    cur.execute(query, proc)

    # Obtaining Query Result & prints the result in rows
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Clean Up
    cur.close()
    db.close()
