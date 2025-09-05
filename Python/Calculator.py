import math
import operator
import tkinter

class Calculator:
    def open_calculator(self):
        self.root = tkinter.Tk()
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.root.resizable(0, 0)
        self.expression = ""
        self.input_text = tkinter.StringVar()
        self.create_widgets()
        self.root.mainloop()
        
    def create_widgets(self):
        self.display = tkinter.Entry(self.root, textvar=self.input_text, font=("Arial", 20), bd=20, insertwidth=4, bg="powder blue", justify="right")
        self.display.pack(ipady=10)
        
        button_frame = tkinter.Frame(self.root)
        button_frame.pack()
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '√',
            '1', '2', '3', '-', '^',
            '0', '.', '=', '+', '!'
        ]
        row_val = 1
        col_val = 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tkinter.Button(button_frame, text=button, width=7, height=3, command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        if button == "C":
            self.expression = ""
            self.input_text.set(self.expression)
        elif button == "√":
            self.expression = str(math.sqrt(eval(self.expression)))
            self.input_text.set(self.expression)
        elif button == "!":
            self.expression = str(math.factorial(int(self.expression)))
            self.input_text.set(self.expression)
        else:
            self.expression += button
            self.input_text.set(self.expression)
            if button == "=":
                try:
                    self.expression = str(eval(self.expression[:-1]))
                    self.input_text.set(self.expression)    
                except Exception as e:
                    self.input_text.set("Error")
                    self.expression = ""
if __name__ == "__main__":
    calc = Calculator()
    calc.open_calculator()
    