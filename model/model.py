import database.corso_DAO as cd
from model.corso import Corso
from model.studente import Studente
import database.studente_DAO as sd

class Model:
    def __init__(self):
        self.corsoDao = cd.corsoDAO()
        self.studenteDao = sd.studenteDAO()

    def getCorsi(self):
        listaCorsi = self.corsoDao.getCorsi()
        listaCorsiAggiornata =[]
        for row in listaCorsi:
            corso = Corso(row["codins"], row["crediti"], row["nome"], row["pd"])
            listaCorsiAggiornata.append(corso)
        return listaCorsiAggiornata

    def getStudenti(self, corsoSelezionato):
        listaStudenti = self.studenteDao.getStudentiCorso(corsoSelezionato)
        listaStudentiAggiornata = []
        for row in listaStudenti:
            if "cds" in row:
                studente = Studente(row["matricola"], row["cognome"], row["nome"], row["cds"])
            else:
                studente = Studente(row["matricola"], row["cognome"], row["nome"], "Non definito")
            listaStudentiAggiornata.append(studente)
        return listaStudentiAggiornata

    def getStudente(self, matricola):
        studente = self.studenteDao.getStudente(matricola)
        if studente == "None":
            return "None"
        studente1 = None
        for row in studente:
            if "cds" in row:
                studente1 = Studente(row["matricola"], row["cognome"], row["nome"], row["cds"])
            else:
                studente1 = Studente(row["matricola"], row["cognome"], row["nome"], "Non definito")
        return studente1

