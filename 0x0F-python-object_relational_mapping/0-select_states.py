#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """ Lists all states from the database hbtn_0e_0_usa """
    my_db = MySQLdb.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], my_db=argv[3])
    cur = my_db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for ret in rows:
        print(ret)
    cur.close()
    my_db.close()
