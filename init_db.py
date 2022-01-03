import sqlite3

if __name__ == '__main__':
    print('Dont run this file directly!')
    exit(0)


def createDb():
    print('\n >>>Creating test.sqlite<<< \n')
    with open('mdb.sql', 'r') as f:
        connection = sqlite3.connect('test.sqlite')
        cursor = connection.cursor()
        cursor.executescript(f.read())



