
import tkinter as tk


class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Webverse_Calc")
        master.config(bg='#9867e6')

        self.entrada = tk.Entry(master, bg= "#55348a", fg= "white",  width=16, font=('Comic Sans MS', 24), borderwidth=5, relief="ridge", justify='left' \
        '')
        self.entrada.grid(row=0, column=0, columnspan=4)
        
        botoes = [
            ('+', 1, 0 , 3), ('-', 1, 1 , 5),
            ('9', 2, 0), ('8', 2, 1), ('7', 2, 2), ('.', 2, 3),
            ('6', 3, 0), ('5', 3, 1), ('4', 3, 2), ('C', 3, 3),
            ('2', 4, 0), ('1', 4, 1), ('0', 4, 2), ('=', 4, 3),
        ]


        for (texto, linha, coluna, colspan) in [(b[0], b[1], b[2], 1) if len(b) == 3 else b for b in botoes]:
            botao = tk.Button(master, text=texto, bg="#9867e6", width=5, height=2, font=('Comic Sans MS', 18),
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
