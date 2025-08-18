import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")

        self.entrada = tk.Entry(master, width=16, font=('Arial', 24), borderwidth=2, relief="ridge", justify='right')
        self.entrada.grid(row=0, column=0, columnspan=4)

        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('=', 5, 0, 4)
        ]

        for (texto, linha, coluna, colspan) in [(b[0], b[1], b[2], 1) if len(b) == 3 else b for b in botoes]:
            botao = tk.Button(master, text=texto, width=5, height=2, font=('Arial', 18),
                              command=lambda t=texto: self.clicar(t))
            botao.grid(row=linha, column=coluna, columnspan=colspan)

    def clicar(self, valor):
        if valor == 'C':
            self.entrada.delete(0, tk.END)
        elif valor == '=':
            try:
                expressao = self.entrada.get()
                resultado = eval(expressao)
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, str(resultado))
            except Exception:
                self.entrada.delete(0, tk.END)
                self.entrada.insert(tk.END, "Erro")
        else:
            self.entrada.insert(tk.END, valor)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculadora(root)
    root.mainloop()
