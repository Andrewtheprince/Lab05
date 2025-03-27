from database.DB_connect import get_connection
import mysql.connector

class studenteDAO:

    def __init__(self):
        pass

    def getStudentiCorso(self, corso):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """ select *
                    from iscrizione i, studente s
                    where i.codins = %s and i.matricola = s.matricola """
        cursor.execute(query, (corso,))
        listaStudenti = []
        for row in cursor:
            listaStudenti.append(row)
        cursor.close()
        cnx.close()
        return listaStudenti

    def getStudente(self, matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary = True)
        query = """ select *
                    from studente s
                    where s.matricola = %s """
        cursor.execute(query, (matricola,))
        studente = "None"
        for row in cursor:
            studente = [row["matricola"], row["cognome"], row["nome"]]
        cursor.close()
        cnx.close()
        return studente

    def iscrivi(self, codins, matricola):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """ INSERT INTO iscrizione
                    (matricola, codins)
                    VALUES (%s, %s) """
        cursor.execute(query, (matricola, codins))
        cnx.commit()
        cursor.close()
        cnx.close()

