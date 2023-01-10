import time
import pyautogui
of = pyautogui
reiniciar = int(input("digite quantos minutos você deseja reiniciar o seu pc:  "))
of.hotkey('win', 'r')
of.typewrite('cmd')
of.hotkey('enter')
of.sleep(3)
of.typewrite("shutdown -r -t "+str(reiniciar))
time.sleep(5)


