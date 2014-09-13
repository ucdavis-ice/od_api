'''
Created on Sep 11, 2014

@author: roth
'''

import psycopg2, csv


def makeTable(conn):
    sqldrp = "DROP TABLE IF EXISTS epa_od;"
    sql = "CREATE TABLE epa_od (objectid SERIAL, origin VARCHAR(25), dest VARCHAR(25), time NUMERIC, distance NUMERIC, CONSTRAINT od_pk PRIMARY KEY (objectid));"
    cur = conn.cursor()
    cur.execute(sqldrp)
    conn.commit()
    cur.execute(sql)
    conn.commit()
    
    
def loadTable(conn, infile):
    # Open cursor
    cur = conn.cursor()
    # Open File
    ofile = open(infile, 'r')
    ocsv = csv.reader(ofile)
    ocsv.next()
    for row in ocsv:
#         origin = row[1][0:12] 
#         print(origin)
#         dest = row[1][15:27]
#         print(dest)
#         minutes = row[5]
#         dist = row[6]
        insrow = (row[1][0:12],row[1][15:27],row[5],row[6])
        sql = "INSERT INTO od_api_odpairs (origin,dest,ttime,tdistance) VALUES(%s,%s,%s,%s);"
        cur.execute(sql,insrow)
#         print(".")
    conn.commit()
        
        
        

connstr = "host='localhost' dbname='django_postgis' user='django_user' password='g0'"
infile = "/home/roth/Workspace2/epa_od/ODmat_CA3_LAX6.txt"

try:
    conn = psycopg2.connect(connstr)
    print("Connection open")
except:
    print("Failed to open connections")
    exit()

    
try:
    makeTable(conn)
    print("Made Tables")
except:
    print("Table construction failed")
    exit()

try:
    loadTable(conn,infile)
    print("Loaded Tables")
except:
    print("Table load failed")
    exit()

print("Done")    
    



    
