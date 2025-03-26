from oauthlib.uri_validate import query

from database.DB_connect import get_connection
import mysql.connector

class studenteDAO:

    def __init__(self):
        pass

    def getStudentiCorso(self, corso):
        cnx = get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """ SELECT * FROM """