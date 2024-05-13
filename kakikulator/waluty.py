import customtkinter as ctk
from currency_converter import CurrencyConverter


def createApp():

    #okno
    window = ctk.CTk(fg_color='#50BFAB')
    window.geometry('340x600')
    window.title('Konwerter walut')
    window.iconbitmap('money.ico')

    c = CurrencyConverter()
    submit = ''
    #translation protocol
    def translation(cur):
        if cur == 'Euro':
            return 'EUR'
        elif cur == 'Polski Złoty':
            return 'PLN'
        elif cur == 'Dolar Amerykański':
            return 'USD'
        elif cur == 'Dolar Australijski':
            return 'AUD'
        elif cur == 'Dolar Kanadyjski':
            return 'CAD'
        elif cur == 'Jen Japoński':
            return 'JPY'
        elif cur == 'Korona Szwedzka':
            return 'SEK'
        elif cur == 'Funt Brytyjski':
            return 'GBP'
        elif cur == 'Rubel Rosyjski':
            return 'RUB'
        elif cur == 'Juan Chiński':
            return 'CNY'

    def finalisation():
        output = (c.convert(number.get(), translation(currency1.get()), translation(currency2.get())))
        label_submit.configure(text = f'Wynik po przewalutowaniu: \n {round(output, 2)}')

    #combobox
    currencies = ('Euro', 'Polski Złoty', 'Dolar Amerykański', 'Dolar Australijski', 'Dolar Kanadyjski', 'Jen Japoński', 'Korona Szwedzka', 'Funt Brytyjski', 'Rubel Rosyjski', 'Juan Chiński' )

    label_number = ctk.CTkLabel(window, text = 'Ile waluty?', pady = 20, font=ctk.CTkFont("Helvetica", 32))
    number = ctk.CTkEntry(window)
    label_number.pack()
    number.pack()

    label1 = ctk.CTkLabel(window, text = 'Z jakiej waluty?', pady = 30, font=ctk.CTkFont("Helvetica", 32))
    currency1 = ctk.CTkComboBox(window, values = currencies, width=147)
    label1.pack()
    currency1.pack()

    label2 = ctk.CTkLabel(window, text = 'Na jaką walutę?', pady = 30, font=ctk.CTkFont("Helvetica", 32))
    currency2 = ctk.CTkComboBox(window, values = currencies, width=147)
    label2.pack()
    currency2.pack()

    label_secret = ctk.CTkLabel(window, text= '', pady=30)
    label_secret.pack()

    #submit button
    button = ctk.CTkButton(window, text = 'Zatwierdź', command = finalisation, fg_color='#ffffff', text_color='#000000', border_color='#000000', border_width=2)
    button.pack()

    label_submit = ctk.CTkLabel(window, text = '', pady = 45, font=ctk.CTkFont("Helvetica", 26))
    label_submit.pack()
    window.mainloop()