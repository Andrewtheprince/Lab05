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
        self._view.txtInCognome.value = ""
        self._view.txtInNome.value = ""
        matricola = self._view._txtInMatricola.value
        if matricola == "":
            self._view.create_alert("Inserire una matricola!")
            return
        studente = self._model.getStudente(matricola)
        if studente == "None":
            self._view.create_alert("La matricola inserita non esiste!")
            return
        else:
            self._view.txtInCognome.value = studente.cognome
            self._view.txtInNome.value = studente.nome

    def cercaCorsiStudente(self, e):
        pass

    def iscrivi(self, e):
        pass
