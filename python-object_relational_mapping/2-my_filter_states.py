#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=db_name)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to fetch data from the states table
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    try:
        # Execute the SQL query
        cursor.execute(sql_query, (state_name,))
        # Fetch all the rows in a list of tuples
        results = cursor.fetchall()
        # Display results
        for row in results:
            print(row)
    except Exception as e:
        print("Error: unable to fetch data -", e)

    # Disconnect from server
    db.close()
    cursor.close()

