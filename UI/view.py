import flet as ft

from model import corso
from database import corso_DAO


class View(object):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione Studenti", color="blue", size=24)
        self._page.controls.append(self._title)

        self.dd = ft.Dropdown(label="Corso",
                              width = 600,
                              hint_text="Selezionare un corso",
                              options=[])
        mydao = corso_DAO.IscrittiDao()
        for c in mydao.getCorsi():
            self.dd.options.append(ft.dropdown.Option(key = c[0], text = c[2]))

        self.btnIscritti = ft.ElevatedButton(text = "Cerca Iscritti", on_click=self.handleIscritti)
        row1 = ft.Row([self.dd, self.btnIscritti])

        #ROW with some controls
        # text field for the name
        self.txt_matricola = ft.TextField(
            label="Matricola",
            width=200,
            hint_text="Inserisci la tua matricola"
        )

        self.txt_name = ft.TextField(
            label="Nome",
            width=200,
            hint_text="Inserisci il tuo nome"
        )

        self.txt_cognome = ft.TextField(
            label="Cognome",
            width=200,
            hint_text="Inserisci il tuo cognome"
        )

        # button for the "hello" reply
        self.btn_cercaStudente = ft.ElevatedButton(text="Cerca studente", on_click=self.handleCercaStudente)
        self.btn_cercaCorsi = ft.ElevatedButton(text="Cerca corsi", on_click=self.handleCercaCorsi)
        self.btn_iscrivi = ft.ElevatedButton(text="Iscrivi")
        row2 = ft.Row([self.txt_matricola, self.txt_name, self.txt_cognome],
                      alignment=ft.MainAxisAlignment.CENTER)
        row3 = ft.Row([self.btn_cercaStudente, self.btn_cercaCorsi, self.btn_iscrivi],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        self._page.controls.append(row2)
        self._page.controls.append(row3)

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
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

    def handleIscritti(self, e):
        mydao = corso_DAO.IscrittiDao()
        counter = 0
        for i in mydao.getIscritti():
            if i[1] == self.dd.value:
                counter += 1
        self.txt_result.controls.append(ft.Text(f'Ci sono {counter} iscritti al corso:'))
        for i in mydao.getIscritti():
            if i[1] == self.dd.value:
                for j in mydao.getStudenti():
                    if i[0] == j[0]:
                        self.txt_result.controls.append(ft.Text(f'{j[2]}, {j[1]} ({j[0]})'))

        self._page.update()

    def handleCercaStudente(self, e):
        mydao = corso_DAO.IscrittiDao()
        for i in mydao.getStudenti():
            if self.txt_matricola.value == str(i[0]):
                self.txt_name.value = i[2]
                self.txt_cognome.value = i[1]
        self._page.update()

    def handleCercaCorsi(self, e):
        mydao = corso_DAO.IscrittiDao()
        counter = 0
        for i in mydao.getIscritti():
            if self.txt_matricola.value == str(i[0]):
                counter += 1
        self.txt_result.controls.append(ft.Text(f'Risultano {counter} corsi:'))
        for i in mydao.getIscritti():
            if self.txt_matricola.value == str(i[0]):
                for j in mydao.getCorsi():
                    if i[1] == j[0]:
                        self.txt_result.controls.append(ft.Text(f'{j[2]} ({j[0]})'))
        self._page.update()




