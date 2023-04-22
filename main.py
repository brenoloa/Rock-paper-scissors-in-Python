import tkinter
from tkinter import *
import random
corpreto = '#000000'
corbranco = '#ffffff'
corverde = '#006600'
corazul = '#00005d'
coramarelo = '#ffffb1'





def escolheu_pedra():
    jokenpo(player='PEDRA')
def escolheu_papel():
    jokenpo(player='PAPEL')
def escolheu_tesoura():
    jokenpo(player='TESOURA')

def jokenpo(player):
    pc = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])

    if player == pc:
        mensagem = f'''
        Você escolheu: {player}
        Eu escolhi: {pc}       
        RESULTADO:  EMPATE!!!'''
    elif(player == 'PEDRA' and pc == 'TESOURA'
        or player == 'PAPEL' and pc == 'PEDRA'
        or player == 'TESOURA' and pc == 'PAPEL'):
         mensagem = f'''
        Você escolheu: {player}
        Eu escolhi: {pc}        
        RESULTADO:  VOCÊ GANHOU.  :(
'''
    else:
        mensagem = f'''
        Você escolheu: {player}
        Eu escolhi: {pc}
        RESULTADO:  EU GANHEI, SIIIIIIIIU
        '''

    resultado.config(text=mensagem)








screen = Tk()
screen.title('sx')
screen.configure(background=corpreto)
screen.geometry('600x600')
#frame
frame_tela = Frame(screen, width=600, height=477, bg=coramarelo)
frame_tela.grid(row=0, column=0)
resultado = Label(frame_tela, text="", width=60, height=5, bg=coramarelo, fg=corpreto, font=('Arial', 20, 'bold'), justify=LEFT)
resultado.place(x=-200, y=100)

frame_corpo = Frame(screen, width=600, height=123, bg=corpreto)
frame_corpo.grid(row=1, column=0)
#-=-=-= TEXT
#texto1 = LabelFrame(frame_corpo, text='Qual você escolhe?', padx=10, pady=10, fg=corbranco)
#texto1.place(x=0, y=0)
#BOTOES
b_tesoura = Button(frame_corpo, text='TESOURA', command=escolheu_tesoura,
                   width=11, height=3,
                   bg=corazul, fg=corbranco,
                   font=('Arial', 20, 'bold'))
b_tesoura.place(x=1, y=2)

b_pedra = Button(frame_corpo, text='PEDRA', command=escolheu_pedra,
                 width=11, height=3,
                 bg=corazul, fg=corbranco,
                   font=('Arial', 20, 'bold'))
b_pedra.place(x=202, y=2)

b_papel = Button(frame_corpo, text='PAPEL', command=escolheu_papel,
                 width=11, height=3,
                 bg=corazul, fg=corbranco,
                   font=('Arial', 20, 'bold'))
b_papel.place(x=403, y=2)


#-=-=-=-=


screen.mainloop()