import os

from tkinter import *


def gravarDados():
    global segundosTotais, meucomando
    getHora(int(vhoras.get()))
    getMin(int(vmin.get()))
    crieComando(segundosTotais)
    os.system(meucomando)


def getHora(hour):
    global horasEmSegundos, segundosTotais
    horasEmSegundos = (hour * 60) * 60
    segundosTotais += horasEmSegundos


def getMin(minutos):
    global minutosEmSegundos, segundosTotais
    minutosEmSegundos = minutos * 60
    segundosTotais += minutosEmSegundos


def crieComando(stotal):
    global meucomando
    meucomando = "shutdown -r -t "+ str(stotal)

def cancelar():
    global meucomando
    meucomando = "shutdown -a"
    os.system(meucomando)


meucomando = None
minutosEmSegundos = None
horasEmSegundos = None
segundosTotais = 0
janela = Tk()
janela.title("Shutdown PC")
# texto = Label(janela, text="digite quantos minutos você deseja reiniciar o seu pc: ")


janela.geometry("320x320")
janela.configure(background="#dde")


Label(janela,text="Horas:",background="#dde",foreground="#009",anchor=W).place(x=10,y=30,width=50,height=20)
vhoras=Entry(janela)
vhoras.place(x=60,y=30,width=50,height=20)

Label(janela,text="Minutos:",background="#dde",foreground="#009",anchor=W).place(x=120,y=30,width=54,height=20)
vmin=Entry(janela)
vmin.place(x=200,y=30,width=50,height=20)


btn=Button(janela,text="Agendar desligamento",background="#0f0",command=gravarDados).place(x=36,y=70,width=220,height=20)

btncancel=Button(janela,text="cancelar desligamento",background="#779",command=cancelar).place(x=36,y=141,width=220,height=20)





janela.mainloop()

#

# os.system(meucomando)


# of = pyautogui
# reiniciar = int(input("digite quantos minutos você deseja reiniciar o seu pc:  "))
# of.hotkey('win', 'r')
# of.typewrite('cmd')
# of.hotkey('enter')
# of.sleep(1)
# of.typewrite("shutdown -r -t "+str(reiniciar))
# time.sleep(1)
# of.hotkey('enter')
# of.sleep(3)
#

