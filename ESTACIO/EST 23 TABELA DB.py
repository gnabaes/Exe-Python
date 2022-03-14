import sqlite3

banco = sqlite3.connect('primeiro_banco2.db')

cursor = banco.cursor()

cursor.execute("CREATE TABLE Pessoas2 (nome text, idade integer, email text )")

cursor.execute("INSERT INTO Pessoas2 VALUES ('Maria', 40,'123@gmail.com')")

banco.commit()




