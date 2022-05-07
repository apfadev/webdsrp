import mysql.connector as mysql


                    
def get_prueba():
    con = mysql.connect(host = 'localhost',
                        port = '3306',
                        user = 'admin',
                        database = 'dsrp',
                        password = 't8P2uEeRHsiDnCEDaaRE')
    #execute query mysql
    cursor = con.cursor()
    cursor.execute("select * from dsrp.tabla_pip limit 1")
    #fetch all rows from query
    rows = cursor.fetchall()
    #print all rows
    for row in rows:
        print(row)
    #close connection
    con.close()
#end of file




#mysql.connector.errors.DatabaseError: 2003 (HY000): Can't connect to MySQL server on 'db-dsrp-dev.cdykihpovon2.us-east-1.rds.amazonaws.com:3306' (111                    