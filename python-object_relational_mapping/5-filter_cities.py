#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb

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

    # Executing MySql Query
    cur.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s ORDER BY cities.id", (search,))

    # Obtaining Query Result & prints the result in rows
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))

    # Clean Up
    cur.close()
    db.close()
