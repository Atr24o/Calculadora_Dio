import tkinter as tk

janela = tk.Tk()
janela.title("Programa_verso_Calc")
janela.configure(bg= '#9867e6')

tela = tk.Entry(
    janela, width=20, borderwidth= 3, 
    bg= '#55348a', fg= 'white', font=('Quartz MS', 24),
    justify= 'left', insertbackground='white'
)
tela.grid(row= 4, column= 0, columnspan= 4, padx= 10, pady= 20, sticky="nsew")

def clicar(botao):
    if botao == "C":
        tela.delete(0, tk.END)
    elif botao == "=":
        try:
            resultado =  eval(tela.get())
            tela.delete(0, tk.END)
            tela.insert(tk.END, str(resultado))
        except:
            tela.delete(0, tk.END)
            tela.insert(tk.END, "ERRO")
    else:
        tela.insert(tk.END, botao)
#Definição dos botões
botoes = [
    '(', ')', '←', '+'
    '9', '8', '7', '-'
    '6', '5', '4', '*'
    '3', '2', '1', '/'
    ',', '0', 'C', '='
]

cores = {
    "numero": "#865dc7",
    "Operador": "#b570e6",
    "funcao": "#9b46d4",
    "igual":  "#ae5ce6", 
    "parenteses": "#c983f7"
}

row_val = 1
col_val = 0

for botao in botoes:
    if botao.isdigit() or botao == ",":
        cor_bg= cores['numero']
    elif botao in ['+', '-', '*', '/']:
        cor_bg= cores['Operador']
    elif botao == "=":
        cor_bg = cores['igual']
    elif botao == ["(", ")"]:
        cor_bg = cores['parenteses']
    else:
        cor_bg = cores['funcao']
    #Código dos botões
    tk.Button(
        tela, text=botao, font=("Comic Sans MC", 18, "bold"), bg= cor_bg, fg="white", 
        activebackground= "#666", activeforeground="white", bd=0, relief="flat", command=lambda b= botao: clicar(b)
        ).grid(row=row_val, column=col_val, sticky="nsew", padx= 5, pady= 10, ipady= 10)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

for i in range(4):
    tela.grid_columnconfigure(i, weight=1)
for i in range(row_val + 1):
    tela.grid_rowconfigure(i, weight=1)


janela.mainloop()
