#!/usr/bin/python3
'''
Write a script that lists all states starting with N
from the database hbtn_0e_0_usa
'''

import MySQLdb
from sys import argv

# Create a connection to the database
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",  # replace with your host name
        port=3306,  # add port
        user=argv[1],  # replace with your username
        passwd=argv[2],  # replace with your password
        database=argv[3]  # replace with your database name
    )

    # Create a cursor object
    cur = db.cursor()

    query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON states.id = cities.state_id "
        "WHERE states.name = %s "
        "ORDER BY cities.id")
    # Execute a query
    cur.execute(query, (argv[4],))

    # Fetch all the rows
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))

    # Close the connection
    cur.close()
    db.close()
