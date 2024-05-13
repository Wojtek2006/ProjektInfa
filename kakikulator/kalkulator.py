# IMPORTS
import customtkinter as ctk
from PIL import Image

# ROOT WINDOW CREATION
def createApp():
    root = ctk.CTkToplevel()


    # VARIABLES
    button_font = ctk.CTkFont("Helvetica", 32)
    display_font = ctk.CTkFont("Helvetica", 70)

    # 0 (+), 1 (-), 2 (*), 3 (/), 4 (%), 5 (^)
    operation_mode = ctk.IntVar(value=0)
    buffer = ctk.DoubleVar(value=0)
    result = ctk.DoubleVar(value=0)
    formula = ctk.StringVar(value='')
    current_nums = []


    # FUNCTIONS

    def flushMem():
        formula.set('')
        current_nums.clear()


    def clearButton():
        flushMem()
        result.set(0)

    def mathButton(value):
        current_nums.append(f'{value}')
        formula.set("".join(current_nums))


    def plusButton():
        buffer.set(float(formula.get()))
        flushMem()
        operation_mode.set(0)


    def minusButton():
        buffer.set(float(formula.get()))
        flushMem()
        operation_mode.set(1)

    def multiplyButton():
        buffer.set(float(formula.get()))
        flushMem()
        operation_mode.set(2)

    def divisionButton():
        buffer.set(float(formula.get()))
        flushMem()
        operation_mode.set(3)

    def percentButton():
        buffer.set(float(formula.get()))
        flushMem()
        operation_mode.set(4)

    def exponentButton():
        buffer.set(float(formula.get()))
        flushMem()
        operation_mode.set(5)
        

    def equalButton():
        # Addition
        if operation_mode.get() == 0:
            result.set(buffer.get() + float(formula.get()))
            flushMem()

            
        # Substraction
        elif operation_mode.get() == 1:
            result.set(buffer.get() - float(formula.get()))
            flushMem()


        # Multiplication
        elif operation_mode.get() == 2:
            result.set(buffer.get() * float(formula.get()))
            flushMem()

        # Division
        elif operation_mode.get() == 3:
            result.set(buffer.get() / float(formula.get()))
            flushMem()

        # Percentage    
        elif operation_mode.get() == 4:
            result.set(buffer.get() * (float(formula.get()) * 10**-2))
            flushMem()

        # Exponentiation
        elif operation_mode.get() == 5:
            result.set(buffer.get() ** float(formula.get()))
            flushMem()




    # ROOT WINDOW SETUP
    root.title('Kalkulator')
    root.iconbitmap('kalkulator.ico')
    root.geometry('400x600')
    root.resizable(False, False)
    root.attributes('-topmost', True)


    # UPPER FRAME SETUP ( DISPLAY SETUP ) 
    display = ctk.CTkFrame(root, fg_color="black", height=200)
    display.place(x = 0, y = 0, relwidth = 1, relheight = 0.3)

    # UPPER FRAME RESULT AND FORMULA LABELS
    result_label = ctk.CTkLabel(display, text_color="white", font=display_font, textvariable = result)
    formula_label = ctk.CTkLabel(display, text_color="white", font=display_font, textvariable = formula)

    # DISPLAY GRID CONFIG
    display.columnconfigure(0, weight=1)
    display.rowconfigure((0, 1), weight=1)

    # RESULT AND FORMULA LABELS GRID CONFIG
    result_label.grid(row = 0, column = 0, sticky = "SE")
    formula_label.grid(row = 1, column = 0, sticky = "SE")



    # LOWER FRAME SETUP ( BUTTON MENU )
    btn_menu = ctk.CTkFrame(root, fg_color="#D1D1D1")
    btn_menu.place(x = 0, y = 180, relwidth = 1, relheight = 0.7)


    # BUTTON MENU GRID CONFIG
    btn_menu.columnconfigure((0, 1, 2, 3), weight=1)
    btn_menu.rowconfigure((0, 1, 2, 3, 4), weight=1)


    # BUTTONS
    btn_C = ctk.CTkButton(btn_menu, text="C", width=60, height=60, hover = False, cursor="hand2", fg_color='#393E41', font=button_font
    , command = clearButton)

    btn_power = ctk.CTkButton(btn_menu, text="^", width=60, height=60, hover = False, cursor="hand2", fg_color='#393E41', font=button_font
    , command = exponentButton)

    btn_percent = ctk.CTkButton(btn_menu, text="%", width=60, height=60, hover = False, cursor="hand2", fg_color='#393E41', font=button_font
    , command = percentButton)

    btn_divide = ctk.CTkButton(btn_menu, text="/", width=60, height=60, hover = False, cursor="hand2", fg_color='#50BFAB', font=button_font
    , command = divisionButton) 

    btn_1 = ctk.CTkButton(btn_menu, text="1", width=60, height=60, hover = False, cursor="hand2", fg_color='#929292', font=button_font
    , command = lambda : mathButton(1)) 
    btn_2 = ctk.CTkButton(btn_menu, text="2", width=60, height=60, hover = False, cursor="hand2", fg_color='#929292', font=button_font
    , command = lambda : mathButton(2))
    btn_3 = ctk.CTkButton(btn_menu, text="3", width=60, height=60, hover = False, cursor="hand2", fg_color='#929292', font=button_font
    , command = lambda : mathButton(3)) 
    btn_4 = ctk.CTkButton(btn_menu, text="4", width=60, height=60, hover = False, cursor="hand2", fg_color='#929292', font=button_font
    , command = lambda : mathButton(4)) 
    btn_5 = ctk.CTkButton(btn_menu, text="5", width=60, height=60, hover = False, cursor="hand2", fg_color='#929292', font=button_font
    , command = lambda : mathButton(5)) 
    btn_6 = ctk.CTkButton(btn_menu, text="6", width=60, height=60, hover = False, cursor="hand2", fg_color='#929292', font=button_font
    , command = lambda : mathButton(6)) 
    btn_7 = ctk.CTkButton(btn_menu, text="7", width=60, height=60, hover = False, cursor="hand2", fg_color='#929292', font=button_font
    , command = lambda : mathButton(7)) 
    btn_8 = ctk.CTkButton(btn_menu, text="8", width=60, height=60, hover = False, cursor="hand2", fg_color='#929292', font=button_font
    , command = lambda : mathButton(8)) 
    btn_9 = ctk.CTkButton(btn_menu, text="9", width=60, height=60, hover = False, cursor="hand2", fg_color='#929292', font=button_font
    , command = lambda : mathButton(9)) 
    btn_0 = ctk.CTkButton(btn_menu, text="0", width=60, height=60, hover = False, cursor="hand2", fg_color='#929292', font=button_font
    , command = lambda : mathButton(0))
    btn_00 = ctk.CTkButton(btn_menu, text="00", width=60, height=60, hover = False, cursor="hand2", fg_color='#929292', font=button_font
    , command = lambda : mathButton("00"))  


    btn_minus = ctk.CTkButton(btn_menu, text="-", width=60, height=60, hover = False, cursor="hand2", fg_color='#50BFAB', font=button_font
    , command = minusButton ) 
    btn_plus = ctk.CTkButton(btn_menu, text="+", width=60, height=60, hover = False, cursor="hand2", fg_color='#50BFAB', font=button_font
    , command = plusButton ) 
    btn_multiply = ctk.CTkButton(btn_menu, text="x", width=60, height=60, hover = False, cursor="hand2", fg_color='#50BFAB', font=button_font
    , command = multiplyButton )
    btn_equals = ctk.CTkButton(btn_menu, text="=", width=60, height=60, hover = False, cursor="hand2", fg_color='#50BFAB', font=button_font
    , command = equalButton ) 
    btn_dot = ctk.CTkButton(btn_menu, text=".", width=60, height=60, hover = False, cursor="hand2", fg_color='#929292', font=button_font
    , command = lambda : mathButton(".")) 



    # BUTTONS GRID CONFIG
    btn_C.grid(row = 0, column = 0)
    btn_power.grid(row = 0, column = 1)
    btn_percent.grid(row = 0, column = 2)
    btn_divide.grid(row = 0, column = 3)

    btn_1.grid(row = 1, column = 0)
    btn_2.grid(row = 1, column = 1)
    btn_3.grid(row = 1, column = 2)
    btn_minus.grid(row = 1, column = 3)

    btn_4.grid(row = 2, column = 0)
    btn_5.grid(row = 2, column = 1)
    btn_6.grid(row = 2, column = 2)
    btn_plus.grid(row = 2, column = 3)

    btn_7.grid(row = 3, column = 0)
    btn_8.grid(row = 3, column = 1)
    btn_9.grid(row = 3, column = 2)
    btn_multiply.grid(row = 3, column = 3)

    btn_00.grid(row = 4, column = 0)
    btn_0.grid(row = 4, column = 1)
    btn_dot.grid(row = 4, column = 2)
    btn_equals.grid(row = 4, column = 3)


    root.mainloop()

