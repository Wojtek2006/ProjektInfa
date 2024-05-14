from settings import *
import customtkinter as ctk
import kalkulator
import pierwiastkowanie
import generatorlosowych
import BMI
import waluty




root = ctk.CTk(fg_color='#D1D1D1')

button_font = ctk.CTkFont("Helvetica", 32)

width = 600
height = 600

root.geometry(f'{width}x{height}+300+300')
root.title("Menu")


root.columnconfigure(0, weight=1)
root.rowconfigure((0, 1, 2, 3, 4), weight=1)


calc_btn = ctk.CTkButton(root, text = 'Kalkulator',
                        command=kalkulator.createApp,
                        width=200,
                        height=50,
                        font=button_font,
                        fg_color=GREEN,
                        hover=False)

calc_btn.grid(row = 0, column = 0)

root_btn = ctk.CTkButton(root, text = 'Pierwiastkowanie',
                        command=pierwiastkowanie.createApp, 
                        width=200, 
                        height=50, 
                        font=button_font, 
                        fg_color=GREEN, 
                        hover=False)

root_btn.grid(row = 1, column = 0)

random_btn = ctk.CTkButton(root, text = 'Randomizer', 
                           command=generatorlosowych.createApp, 
                           width=200, 
                           height=50, 
                           font=button_font, 
                           fg_color=GREEN, 
                           hover=False)

random_btn.grid(row = 2, column = 0)

BMI_btn = ctk.CTkButton(root, text = 'BMI', 
                           command=BMI.createApp, 
                           width=200, 
                           height=50, 
                           font=button_font, 
                           fg_color=GREEN, 
                           hover=False)

BMI_btn.grid(row = 3, column = 0)

currency_btn = ctk.CTkButton(root, text = 'Konwerter Walut', 
                           command=waluty.createApp, 
                           width=200, 
                           height=50, 
                           font=button_font, 
                           fg_color=GREEN, 
                           hover=False)

currency_btn.grid(row = 4, column = 0)


root.mainloop()
