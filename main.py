from tkinter import *
from tkinter import ttk
import random

root  = Tk()
root.title("Filme pra hoje")
root.geometry("800x400")
root.minsize(800, 400)
root.maxsize(800, 400)

def SorteiaFilme():
    filme = random.choice(filmes)
    result_filme = ttk.Label(root, text="Filme pra hoje: " + filme)

    lanche = random.choice(lanches)
    result_lanche = ttk.Label(root, text="Lanche: " + lanche)

    result_filme.pack()
    result_lanche.pack()



label = ttk.Label(root, text='Vamos sortear um filme pra ver hoje?', anchor='center')
label.pack()

button = ttk.Button(root, text="Sortear", command=SorteiaFilme)
button.pack()

filmes = [
    "Diário de uma Paixão",
    "Simplesmente Acontece",
    "Orgulho e Preconceito",
    "A Culpa é das Estrelas",
    "Um Amor para Recordar",
    "Para Sempre Alice",
    "P.S. Eu Te Amo",
    "500 Dias com Ela",
    "Questão de Tempo",
    "O Lado Bom da Vida"
]

lanches = [
    "Pipoca",
    "Nachos com Queijo",
    "Mini Sanduíches",
    "Batata Frita Caseira",
    "Bruschettas",
    "Tábua de Queijos e Embutidos",
    "Hummus com Palitos de Vegetais",
    "Tigela de Frutas",
    "Mini Pizza",
    "Brownies ou Cookies"
]


root.mainloop()






