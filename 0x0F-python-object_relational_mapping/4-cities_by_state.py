#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) == 4:
        USER = sys.argv[1]
        PASSWD = sys.argv[2]
        DATABASE = sys.argv[3]

        try:
            db = MySQLdb.connect(host="localhost", port=3306,
                                 user=USER, passwd=PASSWD, db=DATABASE)
            cursor = db.cursor()
            query = "SELECT c.id, c.name, s.name \
                     FROM cities AS c, states AS s \
                     WHERE c.state_id = s.id \
                     ORDER BY c.id ASC"
            cursor.execute(query)

            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Exception as ex:
            print(ex)
