#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa
under the state that is passed as argument"""
if __name__ == '__main__':
    import sys
    import MySQLdb

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name,
        charset="utf8")
    cur = conn.cursor()

    query = "SELECT cities.name \
            FROM cities \
            LEFT JOIN states \
            ON cities.state_id = states.id \
            WHERE states.name = %s \
            GROUP BY cities.name, cities.id \
            ORDER BY cities.id ASC"
    cur.execute(query, (state,))

    rows = cur.fetchall()
    cities = []
    for row in rows:
        if row != rows[0]:
            print(", ", end="")
        print(row[0], end="")
    print("")
