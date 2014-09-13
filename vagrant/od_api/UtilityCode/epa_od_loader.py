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
    
    
def loadODTable(conn, infile):
    # Open cursor
    cur = conn.cursor()
    # Open File
    ofile = open(infile, 'r')
    ocsv = csv.reader(ofile)
    ocsv.next()
    i = 0
    for row in ocsv:
        i+=1
#         origin = row[1][0:12] 
#         print(origin)
#         dest = row[1][15:27]
#         print(dest)
#         minutes = row[5]
#         dist = row[6]
        insrow = (row[1][0:12],row[1][15:27],1,row[5],row[6])
        sql = "INSERT INTO od_api_odpairs (origin,destination,mode_id,ttime,tdist) VALUES(%s,%s,%s,%s,%s);"
        cur.execute(sql,insrow)
#         print(".")
        if i==5000:
            i=0
            conn.commit()
            print("Committing")
    conn.commit()
        
def loadModeTable(conn):
    # Open cursor
    cur = conn.cursor()
    sql = "INSERT INTO od_api_modes (name) VALUES ('Automobile');"
    cur.execute(sql)
    conn.commit()  
        

connstr = "host='localhost' dbname='django_postgis' user='django_user' password='g0'"
infile = "/vagrant/ODmat_CA3_LAX6.txt"

try:
    conn = psycopg2.connect(connstr)
    print("Connection open")
except:
    print("Failed to open connections")
    exit()

try:
    loadModeTable(conn)
    print("Added mode")
except Exception, e:
    print("Failed to load mode")
    print(str(e))


try:
    loadODTable(conn,infile)
    print("Loaded ODTables")
except Exception, e:
    print("Table load OD failed")
    print(str(e))
    exit()

print("Done")    
    



    
