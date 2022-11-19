#!/usr/bin/python3
"""Lists all states with a name starting with N from a database"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb
    import re

    if (len(argv) != 5):
        print('Use: username, password, database name, state name')
        exit(1)

    searched = ' '.join(argv[4].split())

    if (re.search('^[a-zA-Z ]+$', searched) is None):
        print('Enter a valid name state (example: Arizona)')
        exit(1)

    try:
        db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                             passwd=argv[2], db=argv[3])
    except Exception:
        print("Can't connect to database")
        exit(0)

    state = argv[4]

    cursor = db.cursor()

    cursor.execute("SELECT cities.name FROM cities\
                    INNER JOIN states ON cities.state_id=states.id\
                    WHERE states.name = '{:s}'\
                    ORDER BY cities.id ASC;".format(state))

    m = cursor.fetchall()

    for row in m:
        print(row)

    cursor.close()
    db.close()
