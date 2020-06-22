#Import do pacote para usar o browser e acessar alguma pagina
import webbrowser
webbrowser.open_new('http://www.tinder.com')

#import do módulo que fornece controle ao teclado e mouse
import pyautogui
pyautogui.moveTo(-443,587, duration=1)

#laço de repetição para os clicks
import time
i = 0
while i < 12:
    pyautogui.click()
    time.sleep(0.9)
    i += 1
