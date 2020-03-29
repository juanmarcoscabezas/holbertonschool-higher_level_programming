#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) == 5:
        USER = sys.argv[1]
        PASSWD = sys.argv[2]
        DATABASE = sys.argv[3]
        STATE = sys.argv[4]

        try:
            db = MySQLdb.connect(host="localhost", port=3306,
                                 user=USER, passwd=PASSWD, db=DATABASE)
            cursor = db.cursor()
            query = "SELECT c.name \
                     FROM cities AS c, states AS s \
                     WHERE c.state_id = s.id \
                     AND BINARY s.name = %s \
                     ORDER BY c.id ASC"
            cursor.execute(query, [STATE])

            rows = cursor.fetchall()
            for i, row in enumerate(rows):
                if i != 0:
                    print(', ', end="")
                print(row[0], end="")
            print()
        except Exception as ex:
            print(ex)
