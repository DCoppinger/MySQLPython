import os
import datetime
import pymysql

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        list_of_names = ['fred','Fred']
        # Prepare a string with same number of placeholders as in list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
        connection.commit()
        #rows = cursor.executemany("DELETE FROM Friends WHERE name = %s;",['Bob','Jim'])
        #connection.commit()
        #rows = cursor.execute("DELETE FROM Friends WHERE name = %s;",'Bob')
        #connection.commit()
        # rows = [(23, 'bob'),
        #        (24, 'jim'),
        #        (25, 'fred')]
        #cursor.executemany("UPDATE Friends SET age = %s where name = %s;", rows)
        # connection.commit()
        #
        # cursor.execute("UPDATE Friends SET age = %s where name = %s;",
        # (23, 'Bob'))
        # connection.commit()
        #
        #row =   [("Bob", 29, "1990-02-06 23:04"),
        #        ("jim", 56, "1955-05-09 13:12:45"),
        #        ("fred", 100, "1911-09-12 01:01:01")]
        #cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s)", row)
        #connection.commit()
        #
        # Note that the above will still display a warning (not error) if the
        # table already exists
        # with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        #sql = "SELECT * FROM Artist;"
        #sql = "SELECT * FROM Genre;"
        # cursor.execute(sql)
        #result = cursor.fetchall()
        # print(result)
        # for row in cursor:
        #    print(row)
finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()
