import os
import sqlite3
import SimpleHTTPServer

from os import system as sys


def addTable(cursor, table_name, key_names_csv):
    cursor.execute('''CREATE TABLE ''' + table_name + '''
                (''' + key_names_csv.join(',') + ''')''')

def addRow(cursor, table_name, vals_csv):
    """ Str-vals must be embraced in quotes."""
    rows_obj = cursor.execute(db_name, "INSERT INTO " + table_name + 
                          " VALUES (" + vals_csv.join(',') + ")")
    return rows_obj

def getConnection(db_name):
    return sqlite3.connect(db_name)

def genHtml():
    sys('cat head.html > cat body.html > cat foot.html > index.html')

def genRows(cursor, table_name):
    html = ''
    i = 0
    rows = getRows(cursor, table_name)
    for i, row in enumerate(rows):
        html += '<div class="row-' + str(i) + '-of-' + str(len(rows)) + '">'
        for val in row:
            html += '<div class="val" style="display: inline-block; margin-left: 1em;">'
            html += str(val)
            html += '</div>'
        html += '</div>\n'
    with open('body.html', 'w') as fil: fil.write(html)
    genHtml()

def getRows(cursor, table_name):
    rows = []
    rows_obj = cursor.execute('SELECT * FROM ' + table_name + ' ORDER BY price')
    for row in rows_obj:
        rows.append(row)
    return rows

def serve():
    sys('python -m SimpleHTTPServer 8000')

def main(db_name, table_name):
    conn = getConnection(db_name)
    cursor = conn.cursor()
    #############################
    genRows(cursor, table_name)
    #############################
    conn.close()
    serve()

if __name__ == '__main__':
    main('example.db', 'stocks')

