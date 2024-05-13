import customtkinter as ctk
from settings import *

def createApp():
    class App(ctk.CTkToplevel):
        def __init__(self):
            #window setup
            super().__init__(fg_color = GREEN)
            self.title('Pierwiastkowanie')
            self.iconbitmap('square_root.ico')
            self.geometry('400x400')
            self.resizable(False, False)
            self.attributes('-topmost', True)
            
            #layout
            self.columnconfigure(0, weight = 1)
            self.rowconfigure((0,1,2,3), weight = 1, uniform = 'a')
            #data
            self.nth_int = ctk.DoubleVar(value=1.0)
            self.xth_int = ctk.DoubleVar(value=1.0)
            self.pier = ctk.StringVar()
            self.update_pier()
            #tracing
            self.xth_int.trace_add('write', self.update_pier)
            self.nth_int.trace_add('write', self.update_pier)
            #widgets
            ResultText(self, self.pier)
            NthInput(self, self.nth_int)
            Xinput(self, self.xth_int)

            self.mainloop()
        def update_pier(self, *args):
            r = self.nth_int.get()
            o = self.xth_int.get()
            z = round(o**(1/r), 2)
            self.pier.set(z)
    class ResultText(ctk.CTkLabel):
        def __init__(self, parent, pier):
            font = ctk.CTkFont(family = FONT,size=MAIN_TEXT_SIZE)
            super().__init__(master = parent, text = pier, font=font, text_color=WHITE, textvariable = pier)
            self.grid(column = 0, row = 0, rowspan = 2, sticky = 'nsew') 
    class NthInput(ctk.CTkFrame):
        def __init__(self, parent, nth_int):
            super().__init__(master=parent, fg_color = WHITE)
            font=ctk.CTkFont(family= FONT, size= 20)
            self.grid(column = 0, row = 2, sticky = 'nsew', padx = 5, pady = 5)
            self.rowconfigure(0, weight=1, uniform='b')
            self.columnconfigure(0, weight = 1, uniform='b')
            self.columnconfigure(1, weight = 1, uniform='b')
            labeltext = ctk.CTkLabel(self, text='Stopień Pierwiastka', text_color=BLACK, font=font)
            labeltext.grid(row=0,column=0)
            N1 = ctk.CTkEntry(self, fg_color=GREEN, textvariable=nth_int, font=font)
            N1.grid(row=0, column=1)
    class Xinput(ctk.CTkFrame):
        def __init__(self, parent, xth_int):
            super().__init__(master=parent, fg_color = WHITE)
            font=ctk.CTkFont(family= FONT, size= 20)
            self.grid(column = 0, row = 3, sticky = 'nsew', padx = 5, pady = 5)
            self.rowconfigure(0, weight=1, uniform='b')
            self.columnconfigure(0, weight = 1, uniform='b')
            self.columnconfigure(1, weight = 1, uniform='b')
            labeltext = ctk.CTkLabel(self, text='podpierwiastkowa', text_color=BLACK, font=font)
            labeltext.grid(row=0,column=0)
            X1 = ctk.CTkEntry(self, placeholder_text="Stopień",fg_color=GREEN, textvariable=xth_int, font=font)
            X1.grid(row=0, column=1)

    App()
