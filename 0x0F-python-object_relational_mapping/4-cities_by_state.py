#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8")
    cur = conn.cursor()

    query = "SELECT cities.id, cities.name, states.name \
            FROM cities \
            LEFT JOIN states \
            ON cities.state_id = states.id \
            ORDER BY id ASC"
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)
