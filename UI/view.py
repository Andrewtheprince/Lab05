import flet as ft
from flet_core import MainAxisAlignment

class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self._btnCercaCorsi = None
        self._btnCercaStudente = None
        self._btnIscrivi = None
        self._txtOut = None
        self._txtInCognome = None
        self._titolo = None
        self._txtInNome = None
        self._txtInMatricola = None
        self._btnCercaIscritti = None
        self._tendinaCorsi = None
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        self._controller = None
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):

        self._titolo = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._tendinaCorsi = ft.Dropdown(label="Selezionare un corso", width=500)
        self._controller.caricaCorsi()
        self._btnCercaIscritti = ft.ElevatedButton("Cerca Iscritti", width=190, on_click=self._controller.cercaIscritti)
        self._txtInMatricola = ft.TextField(label="Matricola", width=240)
        self._txtInNome = ft.TextField(label="Nome",disabled=True, width=220)
        self._txtInCognome = ft.TextField(label="Cognome",disabled=True, width=220)
        row0 = ft.Row([self._titolo], alignment=MainAxisAlignment.CENTER)
        row1 = ft.Row([self._tendinaCorsi, self._btnCercaIscritti], alignment=MainAxisAlignment.CENTER, spacing=10)
        row2 = ft.Row([self._txtInMatricola, self._txtInNome, self._txtInCognome], alignment=MainAxisAlignment.CENTER, spacing=10)

        self._btnCercaStudente = ft.ElevatedButton("Cerca Studente", width=150, on_click=self._controller.cercaStudente)
        self._btnCercaCorsi = ft.ElevatedButton("Cerca Corsi", width=150, on_click=self._controller.cercaCorsiStudente)
        self._btnIscrivi = ft.ElevatedButton("Iscrivi", width=150, on_click=self._controller.iscrivi)
        row3= ft.Row([self._btnCercaStudente, self._btnCercaCorsi, self._btnIscrivi], alignment=MainAxisAlignment.CENTER, spacing=10)
        self._txtOut = ft.ListView(expand=True)
        self._page.add(row0, row1, row2, row3, self._txtOut)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()

