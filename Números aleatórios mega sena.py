from random import randint
from tkinter import *




def listamega():
    numeros = []
    for n in range(1,7):
        if n not in numeros :
            numeros.append(randint(1,100))
    sorteionum['text'] = numeros
   


janela = Tk()
janela.title('Sorteio mega sena')
textoinicial = Label(janela,text = 'Sorteio números Mega sena .')
textoinicial.grid(column= 0 ,row = 0 , padx= 10 , pady= 10)
botao = Button (janela , text = 'Aperte para ver os números .',command=listamega)
botao.grid(column=0 , row=1 ,padx= 10 ,pady= 10)
sorteionum = Label(janela ,text = '')
sorteionum.grid(column= 0 , row=2 ,padx= 10 , pady= 10)
janela.mainloop()