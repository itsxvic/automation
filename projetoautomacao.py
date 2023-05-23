#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyautogui as py
import time

#1
py.PAUSE = 1 

py.hotkey ("ctrl", "t")
py.write ("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
py.press ("enter")
time.sleep (3)

#2

py.click (x=1035, y=436)
py.write ("meu login")
py.press ('tab')
py.write ('minha senha')
py.press ('tab')
py.press ('enter')
time.sleep (3)

#3

import pyautogui as py
py.click (x=808, y=363)
py.click (x=874, y=211)
py.click (x=981, y=678)
time.sleep (3)
#4 


import pandas as p

tabela = p.read_csv (r"C:\Users\casti_ivip3np\Downloads\Compras.csv", sep = ';')
print (tabela)

import pandas as p

tabela = p.read_csv (r"C:\Users\casti_ivip3np\Downloads\Compras.csv", sep = ';')

total_gasto = tabela ['ValorFinal'].sum ()
quantidade = tabela ['Quantidade'].sum ()
preco_medio = total_gasto/quantidade

print (total_gasto)
print (quantidade)
print (preco_medio)

#5
import pyperclip

py.hotkey ('ctrl', 't')

time.sleep (1)

email = f"""https://mail.google.com/mail/u/0/?pli=1#inbox"""
pyperclip.copy (email)
py.hotkey ('ctrl', 'v')
py.press ('enter')

time.sleep (5)

py.click (x=183, y=206)

time.sleep (2)

py.write ('vicamaojao@gmail.com')
py.press ('tab')

time.sleep (1)

py.press ('tab')
py.write ('relatorio')
py.press ('tab')

texto = f"""
prezado,

segue o relatorio de compras

total gasto = R${total_gasto:,.2f}
quantidade de produtos = R${quantidade:,.2f}
preco medio = R${preco_medio:,.2f}

att,
victoria
"""

pyperclip.copy (texto)
py.hotkey ('ctrl','v')

py.hotkey ('ctrl', 'enter')

