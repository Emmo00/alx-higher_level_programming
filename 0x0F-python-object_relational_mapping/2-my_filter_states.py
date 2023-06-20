#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa
where name matches the argument"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8")
    cur = conn.cursor()

    query = "SELECT * FROM states WHERE name LIKE BINARY \
    '{}' ORDER BY id ASC".format(name)
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)
