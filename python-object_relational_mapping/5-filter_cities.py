#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name state_name".format(sys.argv[0]))
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database_name)
        cursor = db.cursor()
        cursor.execute("SELECT cities.name FROM cities INNER JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC", (state_name,))
        cities = cursor.fetchall()
        if not cities:
            print("No cities found for the given state.")
        else:
            city_names = ', '.join(city[0] for city in cities)
            print(city_names)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))