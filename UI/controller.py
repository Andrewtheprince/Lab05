import flet as ft

class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def caricaCorsi(self):
        self.listaCorsi = self._model.getCorsi()
        for corso in self.listaCorsi:
            self._view._tendinaCorsi.options.append(ft.dropdown.Option(key=corso.codins, text=corso.__str__()))

    def cercaIscritti(self, e):
        self._view._txtOut.clean()
        self._view.update_page()
        if self._view._tendinaCorsi.value == None:
            self._view.create_alert("Selezionare un corso!")
            return
        corsoSelezionato = self._view._tendinaCorsi.value
        studentiCorso = self._model.getStudenti(corsoSelezionato)
        for studente in studentiCorso:
            self._view._txtOut.controls.append(ft.Text(studente.__str__()))
        self._view.update_page()

    def cercaStudente(self, e):
        self._view._txtInCognome.value = ""
        self._view._txtInNome.value = ""
        matricola = self._view._txtInMatricola.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola!")
            return
        studente = self._model.getStudente(matricola)
        if studente == "None":
            self._view.create_alert("La matricola inserita non esiste!")
            return
        else:
            self._view._txtInCognome.value = studente.cognome
            self._view._txtInNome.value = studente.nome
            self._view.update_page()

    def cercaCorsiStudente(self, e):
        self._view._txtInCognome.value = ""
        self._view._txtInNome.value = ""
        matricola = self._view._txtInMatricola.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola!")
            return
        studente = self._model.getStudente(matricola)
        if studente == "None":
            self._view.create_alert("La matricola inserita non esiste!")
            return
        else:
            self._view._txtInCognome.value = studente.cognome
            self._view._txtInNome.value = studente.nome
            self._view._txtOut.controls.clear()
            corsiStudente = self._model.corsiStudente(matricola)
            for corso in corsiStudente:
                self._view._txtOut.controls.append(ft.Text(corso.__str__()))
            self._view.update_page()

    def iscrivi(self, e):
        self._view._txtOut.clean()
        self._view.update_page()
        if self._view._tendinaCorsi.value == None:
            self._view.create_alert("Selezionare un corso!")
            return
        corsoSelezionato = self._view._tendinaCorsi.value
        self._view._txtInCognome.value = ""
        self._view._txtInNome.value = ""
        matricola = self._view._txtInMatricola.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola!")
            return
        studente = self._model.getStudente(matricola)
        if studente == "None":
            self._view.create_alert("La matricola inserita non esiste!")
            return
        self._view._txtInCognome.value = studente.cognome
        self._view._txtInNome.value = studente.nome
        self._model.iscrivi(corsoSelezionato, matricola)
        self._view.update_page()
        self._view.create_alert(f"Studente con matricola {matricola} correttamente iscritto al corso {corsoSelezionato}!")
        self._view.update_page()


