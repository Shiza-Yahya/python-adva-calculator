import tkinter as tk
from tkinter import messagebox
import math

class AdvancedCalculatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("🧮 Advanced Calculator")
        master.geometry("400x600")
        master.resizable(False, False)

        self.expression = ""
        self.memory = 0

        # Display Frame
        self.display = tk.Entry(master, font=("Arial", 24), bd=5, relief="ridge", justify="right")
        self.display.pack(fill="both", ipadx=8, pady=10, padx=10)

        # Buttons Frame
        self.buttons_frame = tk.Frame(master)
        self.buttons_frame.pack()

        # Buttons Layout
        buttons = [
            ['7','8','9','/','√'],
            ['4','5','6','*','%'],
            ['1','2','3','-','^'],
            ['0','.','=','+','C'],
            ['sin','cos','tan','!','log'],
            ['M+','M-','MR','MC','RESET']
        ]

        for r, row in enumerate(buttons):
            for c, btn in enumerate(row):
                tk.Button(
                    self.buttons_frame, text=btn, width=6, height=2, font=("Arial", 14),
                    command=lambda b=btn: self.on_button_click(b)
                ).grid(row=r, column=c, padx=3, pady=3)

    def on_button_click(self, char):
        try:
            if char == "=":
                self.calculate()
            elif char == "C":
                self.expression = self.expression[:-1]
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.expression)
            elif char == "RESET":
                self.expression = ""
                self.display.delete(0, tk.END)
                self.memory = 0
            elif char in ["sin","cos","tan","log","!","√"]:
                self.expression += f"{char}("
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.expression)
            elif char in ["M+","M-","MR","MC"]:
                self.memory_operations(char)
            else:
                self.expression += str(char)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.expression)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def memory_operations(self, op):
        try:
            current = self.evaluate_expression(self.expression) if self.expression else 0
            if op == "M+":
                self.memory += current
            elif op == "M-":
                self.memory -= current
            elif op == "MR":
                self.expression = str(self.memory)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, self.expression)
            elif op == "MC":
                self.memory = 0
            self.expression = ""
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def calculate(self):
        try:
            result = self.evaluate_expression(self.expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
            self.expression = str(result)
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.expression = ""

    def evaluate_expression(self, expr):
        """Evaluate expression with math functions"""
        expr = expr.replace('^', '**').replace('√','math.sqrt')
        expr = expr.replace('sin','math.sin(math.radians')
        expr = expr.replace('cos','math.cos(math.radians')
        expr = expr.replace('tan','math.tan(math.radians')
        expr = expr.replace('log','math.log10')
        expr = expr.replace('!','math.factorial')
        return eval(expr)

if __name__ == "__main__":
    root = tk.Tk()
    calc = AdvancedCalculatorGUI(root)
    root.mainloop()
