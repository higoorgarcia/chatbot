# 1 - importar bibliotecas necessarias
import pywhatkit
import keyboard
import time
from datetime import datetime

# 2 - Definir quais contatos receberão as msg's
contatos = ['+5516997590582']

# 3 - Definir um intervalo de envio
while len(contatos) >= 1:
    #envia mensagem
    pywhatkit.sendwhatmsg(contatos[0],'Testando o chatbot, Quero cafe', datetime.now().hour,datetime.now().minute + 2)
    del contatos[0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')
# 4 - Teste !







