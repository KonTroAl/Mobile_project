"""
My firts try in BeeWare
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

# фунцкия проверки наличия имени в окне ввода
def greeting(name):
    if name:
        return f'Hello, {name}'
    else:
        return 'Hello, stranger'

class HelloWorld(toga.App):

    # функция моделирования приложения
    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """

        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_lable = toga.Label(
            'Your name: ',
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        name_box.add(name_lable)
        name_box.add(self.name_input)

        button = toga.Button(
            'Say Hello!',
            on_press=self.say_hello,
            style=Pack(padding=5)
        )

        main_box.add(name_box)
        main_box.add(button)


        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    # функция вывода сообщения в диалоговом окне
    def say_hello(self, widget):
        self.main_window.info_dialog(
            greeting(self.name_input.value),
            'Hi there!',
        )

def main():
    return HelloWorld()
