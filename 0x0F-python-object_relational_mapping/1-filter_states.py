#!/usr/bin/python3
"""script that lists all states from a database"""


from sys import argv
import MySQLdb


if __name__ == "__main__":
    if len(argv) < 4:
        exit(-1)
    dic = {
        'host': "localhost",
        'port': 3306,
        'user': argv[1],
        'passwd': argv[2],
        'db': argv[3]
    }
    command = "SELECT * FROM states WHERE name like 'N%' ORDER BY states.id"

    db = MySQLdb.connect(**dic)
    cursor = db.cursor()
    cursor.execute(command)

    results = cursor.fetchall()
    for dates in results:
        print(dates)
