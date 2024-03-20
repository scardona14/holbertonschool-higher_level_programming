#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    """Function that connects to MySQL server on localhost at port 3306"""

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("SELECT cities.id, cities.name, states.name \
                     FROM cities \
                     JOIN states \
                     ON cities.state_id = states.id \
                     WHERE states.name LIKE BINARY %(state_name)s \
                     ORDER BY cities.id ASC", {'state_name': argv[4]})
        rows = cur.fetchall()
        if rows is not None:
            result = ", ".join([row[1] for row in rows])
            print(result)
