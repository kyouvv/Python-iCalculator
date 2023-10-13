import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.calculation = ""
        self.result = ""
        self.have_answer = False
        self.text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
        self.text_result.grid(columnspan=5)
        self.create_buttons(root)
        self.signatureLabel = tk.Label(root, text="made by: kyouvv")
        self.signatureLabel.grid(column=4, row=6)
    def add_to_calculator(self, symbol):
        if self.have_answer:
            self.result += str(symbol)
            self.update_display(self.result)
        else:
            self.calculation += str(symbol)
            self.update_display(self.calculation)

    def evaluate_calculation(self):
        try:
            if self.have_answer:
                self.result = str(eval(self.result))
            else:
                self.result = str(eval(self.calculation))
                self.calculation = ""
                self.have_answer = True
            self.update_display(self.result)
        except Exception as e:
            self.clear_input()
            self.update_display("Error")

    def clear_input(self):
        self.calculation = ""
        self.result = ""
        self.update_display("")

    def update_display(self, value):
        self.text_result.delete(1.0, "end")
        self.text_result.insert(1.0, value)

    def create_buttons(self, root):
        buttons = [
            "1", "2", "3", "+",
            "4", "5", "6", "-",
            "7", "8", "9", "*",
            "(", "0", ")", "/",
            "=", "C"
        ]
        row, col = 2, 1
        for button_text in buttons:
            if button_text == "=":
                command = self.evaluate_calculation
                col = 1
            elif button_text == "C":
                command = self.clear_input
                col = 3
            else:
                command = lambda text=button_text: self.add_to_calculator(text)
            
            tk.Button(root, text=button_text, command=command, width=5, font=("Arial", 14)).grid(row=row, column=col)
            col += 1
            if col > 4:
                col = 1
                row += 1

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x275")
    root.title("Calculator")
    app = CalculatorApp(root)
    root.mainloop()