import time
import pyautogui
from tkinter import *
janela = Tk()
janela.title("Shutdown PC")
# texto = Label(janela, text="digite quantos minutos você deseja reiniciar o seu pc: ")
janela.geometry("900x450")
janela.configure(background="#808080")


Label(janela,text="digite aqui",background="#fff",foreground="#009",anchor=W).place(x=10,y=10,width=100,height=20)
vnome=Entry(janela)
vnome.place(x=10,y=30,width=200,height=20)

janela.mainloop()



of = pyautogui
reiniciar = int(input("digite quantos minutos você deseja reiniciar o seu pc:  "))
of.hotkey('win', 'r')
of.typewrite('cmd')
of.hotkey('enter')
of.sleep(1)
of.typewrite("shutdown -r -t "+str(reiniciar))
time.sleep(1)
of.hotkey('enter')
of.sleep(3)


