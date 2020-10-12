import sqlite3 


con = sqlite3.connect('DB.db')
cursor=con.cursor()

def INSERTelev(x,y):
	
		cursor.execute('''INSERT INTO ELEVE(name,date) VALUES(?,?)''',(x,y))
		con.commit()
def listname(x): 
        if x != '' and x !='None' : 
            IDl=""
            for l in cursor.execute('''SELECT  eleve_id FROM GROUPE WHERE name=? ''',(x,)):
                IDl+=str(l[0])+'|'
            lIDl=IDl.split('|')
            lsn=""
            for i in lIDl :
                if i != '' and i !='None' :
                    for l in cursor.execute('''SELECT name FROM ELEVE WHERE IDELEVE=?''',(i,)):
                   		 lsn+=str(l[0])+'|'
            return lsn.split('|')
	



#INSERTelev("ali","03/02/1997")

#SD=input("le name ")
id=cursor.execute('''SELECT DISTINCT name FROM GROUPE ''')
b=""
for i in id : 
	b+=str(i[0])+'|'
liste=b.split('|')
for i in liste : 
	print(i)
	print(listname(i))

#id=cursor.fetchone()
#print(id)
#s=input("iddd ::")
#cursor.execute('''DELETE  FROM ELEVE WHERE name=?''',(s,))
con.commit()
#print(id[0])

con.close()
