import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
time.sleep(3)

pyautogui.click(x=887, y=370)
pyautogui.write('testeemail@gmail.com')
pyautogui.press('tab')
pyautogui.write('teste')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3)

tabela = pd.read_csv('produtos.csv')

for linha in tabela.index:    
    pyautogui.click(x=916, y=255)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    tipo = tabela.loc[linha, "tipo"] 
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press('tab')

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')  

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.scroll(50000)

pyautogui.scroll(-50000)