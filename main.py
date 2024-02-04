##This import random
import random

##This import kivy moduls
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.clipboard import Clipboard

class PasswordGeneratedApp(App):
    ##This main class PasswordGeneratedApp 
    def Update_Label(self):
        ##Function for update label
        self.lbl.text = self.password


    def Generated_Password_Function(self,instance):
        ##Function for generated password
        
        self.password = ""

        ##This chars using in generated password
        chars = "!@#$%^&*()_+{|:<>}?-=[]\;',./~`1234567890€£¥•§±©®™×÷¬°¢µ¶‹›«»‡†∞≈≠≤≥∑∏√qwertyuiopasdfghjklzxcvbnm"
        
        for steps_generated_password in range(random.randint(5,30)):
            ##Cycle for generated password
            self.password += random.choice(chars)

        self.Update_Label()

    def Label_Clear(self,instance):
        ##Function for clear label
        self.lbl.text = 'Чтобы сгенерировался пароль нажми кнопку <Сгенерировать пароль>'

    def Password_Save(self,instance):
        ##Function for save password in clipboard 
        Clipboard.copy(self.lbl.text)

    def build(self):
        ##This function build is main function
        
        
        b1 = BoxLayout(orientation = 'vertical',padding = 10)
        g1 = GridLayout(cols=2,spacing = 1)

        self.lbl = Label(text='Чтобы сгенерировался пароль нажми кнопку <Сгенерировать пароль>')
        b1.add_widget(self.lbl)
        g1.add_widget(Button(text='Сгенерировать пароль из 5 символов и больше',on_press = self.Generated_Password_Function))
        g1.add_widget(Button(text='Отчистить',on_press = self.Label_Clear))
        g1.add_widget(Button(text='Сохранить пароль',on_press=self.Password_Save))
        
        ##This unites BoxLayout and GridLayout
        b1.add_widget(g1)

        ##This return BoxLayout(GridLayout)
        return b1

##This main <if __name__ == '__main__'> run main class ParolGeneratedApp 
if __name__ == '__main__':
    PasswordGeneratedApp().run()