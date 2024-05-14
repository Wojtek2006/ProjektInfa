import customtkinter as ctk
from settings import *
import random as rng

def createApp():
    class App(ctk.CTkToplevel):
        def __init__(self):
            super().__init__(fg_color=GREEN)
            self.title('Randomizer')
            self.geometry('400x400')
            self.resizable(False, False)

            self.columnconfigure(0, weight=1)
            self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')

            self.nth_int = ctk.IntVar(value=1)
            self.xth_int = ctk.IntVar(value=10)
            self.los = ctk.StringVar()

            self.nth_int.trace_add('write', self.update_los)
            self.xth_int.trace_add('write', self.update_los)

            self.result_text = ResultText(self, self.los)
            self.nth_input = NthInput(self, self.nth_int)
            self.x_input = Xinput(self, self.xth_int)
            self.fin = Fin(self, self)

            self.mainloop()

        def update_los(self, *args):
            r = self.nth_int.get()
            o = self.xth_int.get()
            z = rng.randrange(r, o)
            self.los.set(z)

    class ResultText(ctk.CTkLabel):
        def __init__(self, parent: ctk.CTk, los: ctk.StringVar):
            font = ctk.CTkFont(family=FONT, size=MAIN_TEXT_SIZE)
            super().__init__(master=parent, text=los, font=font, text_color=WHITE, textvariable=los)
            self.grid(column=0, row=0, rowspan=2, sticky='nsew')

    class NthInput(ctk.CTkFrame):
        def __init__(self, parent: ctk.CTk, nth_int: ctk.IntVar):
            super().__init__(master=parent, fg_color=WHITE)
            font = ctk.CTkFont(family=FONT, size=20)
            self.grid(column=0, row=2, sticky='nsew', padx=5, pady=5)
            self.rowconfigure(0, weight=1, uniform='b')
            self.columnconfigure(0, weight=1, uniform='b')
            self.columnconfigure(1, weight=1, uniform='b')
            label_text = ctk.CTkLabel(self, text='Od', text_color=BLACK, font=font)
            label_text.grid(row=0, column=0)
            N1 = ctk.CTkEntry(self, fg_color=GREEN, textvariable=nth_int, font=font)
            N1.grid(row=0, column=1)

    class Xinput(ctk.CTkFrame):
        def __init__(self, parent: ctk.CTk, xth_int: ctk.IntVar):
            super().__init__(master=parent, fg_color=WHITE)
            font = ctk.CTkFont(family=FONT, size=20)
            self.grid(column=0, row=3, sticky='nsew', padx=5, pady=5)
            self.rowconfigure(0, weight=1, uniform='b')
            self.columnconfigure(0, weight=1, uniform='b')
            self.columnconfigure(1, weight=1, uniform='b')
            label_text = ctk.CTkLabel(self, text='Do', text_color=BLACK, font=font)
            label_text.grid(row=0, column=0)
            X1 = ctk.CTkEntry(self, placeholder_text="Stopień", fg_color=GREEN, textvariable=xth_int, font=font)
            X1.grid(row=0, column=1)

    class Fin(ctk.CTkFrame):
        def __init__(self, parent: ctk.CTk, app: App):
            super().__init__(master=parent, fg_color=GREEN)
            font = ctk.CTkFont(family=FONT, size=20)
            self.grid(column=0, row=4, sticky='nsew', padx=5, pady=5)
            self.rowconfigure(0, weight=1, uniform='b')
            self.columnconfigure(0, weight=1, uniform='b')
            N1 = ctk.CTkButton(self, text='Generuj', command=app.update_los, fg_color=WHITE, text_color=BLACK)
            N1.grid(row=0, column=0)

    App()
