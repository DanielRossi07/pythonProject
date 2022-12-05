from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def conversionResult(currency_from, currency_to, currency_amount, result):
    pop = Popup(title='Conversion result',
                  content=Label(text=f'{currency_amount} {currency_from} = {result} {currency_to}'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidAmount():
    pop = Popup(title='Invalid amount',
                  content=Label(text='Fill in amount field'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def usernameTaken():
    pop = Popup(title='Username taken',
                  content=Label(text='Sorry, this username already exist'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def passwordsDoNotMatch():
    pop = Popup(title="Password do not match",
                  content=Label(text="Passwords do not match"),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def emptyPasswordConfirmation():
    pop = Popup(title="Empty password confirmation",
                  content=Label(text="Please, fill in password confirmation field"),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def emptyPassword():
    pop = Popup(title="Empty password",
                  content=Label(text="Please, fill in password field"),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def emptyUsername():
    pop = Popup(title="Empty username",
                  content=Label(text="Please, fill in username field"),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def emptyCurrencyFrom():
    pop = Popup(title="Empty currency",
                  content=Label(text="Please, select what currency you want to convert FROM"),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def emptyCurrencyTo():
    pop = Popup(title="Empty currency",
                  content=Label(text="Please, select what currency you want to convert TO"),
                  size_hint=(None, None), size=(400, 400))
    pop.open()