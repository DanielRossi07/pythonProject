from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivymd.app import MDApp
from popups import *
from database import DataBase
import crypto


CURRENCY_FROM = None
CURRENCY_TO = None


class LoginWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def login_btn(self):
        if self.username.text != "":
            if self.password.text != "":
                if database.validate_user(self.username.text, self.password.text):
                    self.reset()
                    self.parent.current = 'main'
                else:
                    invalidLogin()
            else:
                emptyPassword()
        else:
            emptyUsername()

    def reset(self):
        self.username.text = ""
        self.password.text = ""


class CreateAccountWindow(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    passwordConfirmation = ObjectProperty(None)

    def create_account_btn(self):
        if self.username.text != "":
            if self.password.text != "":
                if self.passwordConfirmation.text != "":
                    if self.password.text == self.passwordConfirmation.text:
                        if database.add_user(self.username.text, self.password.text):
                            self.reset()
                            self.parent.current = 'login'
                        else:
                            usernameTaken()
                    else:
                        passwordsDoNotMatch()
                else:
                    emptyPasswordConfirmation()
            else:
                emptyPassword()
        else:
            emptyUsername()

    def reset(self):
        self.username.text = ""
        self.password.text = ""


class MainWindow(Screen):
    currency_amount = ObjectProperty(None)

    def set_selected_currency(self, option, currency_id):
        global CURRENCY_FROM, CURRENCY_TO

        if option == "FROM":
            self.children[4].text = currency_id
            CURRENCY_FROM = currency_id
        else:
            self.children[3].text = currency_id
            CURRENCY_TO = currency_id

    def convert_currency(self):
        if self.currency_amount.text != "":
            if CURRENCY_FROM != "" and CURRENCY_FROM is not None:
                if CURRENCY_TO != "" and CURRENCY_TO is not None:
                    result = crypto.CurrencyConverter().convert(CURRENCY_FROM, CURRENCY_TO, self.currency_amount.text)
                    conversionResult(CURRENCY_FROM, CURRENCY_TO, self.currency_amount.text, result)
                else:
                    emptyCurrencyTo()
            else:
                emptyCurrencyFrom()
        else:
            invalidAmount()


screen_manager = ScreenManager()
screen_manager.add_widget(LoginWindow(name='login'))
screen_manager.add_widget(CreateAccountWindow(name='create'))
screen_manager.add_widget(MainWindow(name='main'))

database = DataBase()

class CryptoConverter(MDApp):
    Window.size = (500, 400)

    def build(self):
        return Builder.load_file("design.kv")


CryptoConverter().run()
