#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) == 5:
        USER = sys.argv[1]
        PASSWD = sys.argv[2]
        DATABASE = sys.argv[3]

        try:
            db = MySQLdb.connect(host="localhost", port=3306,
                                 user=USER, passwd=PASSWD, db=DATABASE)
            cursor = db.cursor()
            query = "SELECT * \
                     FROM states \
                     WHERE BINARY name = '{}' \
                     ORDER BY id ASC".format(sys.argv[4])
            cursor.execute(query)

            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Exception as ex:
            print(ex)
