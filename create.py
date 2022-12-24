import mysql.connector
import datetime

# Abaixo você coloca as informações do seu banco de dados

connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="teste"
)

cursor = connection.cursor()

# em DATA, altere para teste de inserções.

sql = "INSERT INTO users (name, email, created) VALUES (%s, %s, %s)"
data = (
  'Paulo Palmeira',
  'paulopalmeira@dominio.com.br',
  datetime.datetime.today()
)

cursor.execute(sql, data)
connection.commit()

userid = cursor.lastrowid

# Ele fecha o banco no CLOSE e informa no print se deu certo.

cursor.close()
connection.close()

print("Foi cadastrado o novo usuário de ID:", userid)