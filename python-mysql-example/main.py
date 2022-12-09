#EFFETTUO COLLEGAMENTO CON IL MIO DATABASE SQL
import mysql.connector

mydb = mysql.connector.connect(
host="localhost",
user="enricosql1",
password="ferrosql",1
db='prova'
)

#C-R-U-D

#READ
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM prova2;')
for y in mycursor:
  print(y)

#CREATE
nome = input('Inserisci il nome di chi vuoi aggiungere nel dataset \n')
mycursor.execute("INSERT INTO prova2 VALUES ('" + nome + "');")

#READ
mycursor.execute('SELECT * FROM prova2;')
for y in mycursor:
  print(y)

#UPDATE
condition = input('Hai scritto il nome di qualcuno sbagliato? Digita -yes- se è corretto \n')
if condition == 'yes':
  wrong = input('Quale valore vuoi modificare?\n') 
  update = input('Quale valore vuoi mettere?\n')
  mycursor.execute("UPDATE prova2 SET nome='"+update+"' WHERE NOME='"+wrong+"';")
else:
  print('Siamo contenti che non ci sono problemi')

#READ
mycursor.execute('SELECT * FROM prova2;')
for y in mycursor:
  print(y)


#DELETE 
condition = input('Vuoi cancellare il nome di qualcuno? Digita -yes- se è corretto \n')
if condition == 'yes':
  delete = input('Quale valore vuoi cancellare?\n') 
  mycursor.execute("DELETE FROM prova2 WHERE NOME='"+delete+"';")
else:
  print('Siamo contenti che non ci sono problemi') 

#READ
mycursor.execute('SELECT * FROM prova2;')
for y in mycursor:
  print(y)

