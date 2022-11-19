#!/usr/bin/python3
"""Lists all states with a name starting with N from a database"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb

    try:
        db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3])
    except Exception:
        print("Can't connect to database")
        exit(0)
    
    state = argv[4]
    
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name = BINARY \
                    '{:s}' ORDER BY id ASC;".format(state))

    m = cursor.fetchall()

    for row in m:
        print(row)

    cursor.close()
    db.close()
