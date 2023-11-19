#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """ Lists all states from the database hbtn_0e_0_usa """
    my_db = MySQLdb.connect(host="localhost", user=argv[1], password=argv[2],
                            database=[3], port=3306)
    cur = my_db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for ret in rows:
        print(ret)
    cur.close()
    my_db.close()
