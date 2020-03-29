#!/usr/bin/python3
"""script that lists all states from a database"""


from sys import argv
import MySQLdb


if __name__ == "__main__":
        dic = {
                'host': "localhost",
                'port': 3306,
                'user': argv[1],
                'passwd': argv[2],
                'db': argv[3]
        }
        command = """select cities.id, cities.name, states.name from states,
                 cities where cities.state_id = states.id and states.name = %s order by cities.id"""

        db = MySQLdb.connect(**dic)
        cursor = db.cursor()
        cursor.execute(command, (argv[4],))

        results = cursor.fetchall()
        print(", ".join(dates[1] for dates in results))

        cursor.close()
        db.close()
