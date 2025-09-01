import tkinter as tk

janela = tk.Tk()
janela.title("Programa_verso_Calc")
janela.configure(bg= '#9867e6')



tela = tk.Entry(
    janela, width=15, borderwidth= 3, 
    bg= '#55348a', fg= 'white', font=('Quartz MS', 24),
    justify= 'left', insertbackground='white'
)
tela.grid(row= 0, column= 0, columnspan= 4, padx= 10, pady= 20, sticky="nsew")

# Função para tratar eventos de teclado

def pressionar_tecla(event):
    tecla = event.char
    if tecla.isdigit() or tecla in "()+-*/.,":  # Permitir números e operadores
        tela.insert(tk.END, tecla)
    elif tecla == '\r':  # Enter para calcular
        clicar("=")
    elif tecla == '\x08':  # Backspace para apagar
        clicar("⌫")

# Associar o evento de teclado à janela

janela.bind("<Key>", pressionar_tecla)

#Função dos botões

def clicar(botao):
    if botao == "C":
        tela.delete(0, tk.END)
    elif botao == "⌫":
        tela.delete(len(tela.get())-1, tk.END)
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
    '(', ')', '⌫', '+',
    '9', '8', '7', '-',
    '6', '5', '4', '*',
    '3', '2', '1', '/',
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
    elif botao in ['/', '*', '-', '+']:
        cor_bg= cores['Operador']
    elif botao == "=":
        cor_bg = cores['igual']
    elif botao == ["(", ")"]:
        cor_bg = cores['parenteses']
    else:
        cor_bg = cores['funcao']
    #Código dos botões
    tk.Button(
        janela, text=botao, font=("Comic Sans MC", 18, "bold"), bg= cor_bg, fg="white", 
        activebackground= "#666", activeforeground="white", bd=0, relief="flat", command=lambda b= botao: clicar(b)
    ).grid(row=row_val, column=col_val, sticky="nsew", padx= 5, pady= 10, ipadx= 10, ipady= 10)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

for i in range(4):
    janela.grid_columnconfigure(i, weight=1)
for i in range(row_val + 1):
    janela.grid_rowconfigure(i, weight=1)


janela.mainloop()
# Fim do código
