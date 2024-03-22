#!/usr/bin/python3


import MySQLdb
from sys import argv

"""
 script that lists all states from the database hbtn_0e_0_usa
"""
def listallstates(usern, password, datab):
    db = MySQLdb.connect(host="localhost", port=3306, user=usern, passwd=password, db=datab)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)

if __name__ == "__main__":

    listallstates(user=argv[1], password=argv[2], datab=argv[3])
