#####################################################
# Camada Física da Computação
# Carareto
# 11/08/2020
# Aplicação
####################################################


# esta é a camada superior, de aplicação do seu software de comunicação serial UART.
# para acompanhar a execução e identificar erros, construa prints ao longo do código!


from enlace import *
import time
import numpy as np

# voce deverá descomentar e configurar a porta com através da qual ira fazer comunicaçao
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

# use uma das 3 opcoes para atribuir à variável a porta usada
#serverRX = "/dev/ttyACM1"  # Ubuntu (variacao de)

serverTX = "/dev/tnt0" # Mac    (variacao de)
serverRX = "/dev/tnt2"
# serialName = "COM6"                  # Windows(variacao de)


def main():
    try:
        
        com3 = enlace(serverTX)
        com4 = enlace(serverRX)

        imgW = './imgW.jpg'

        com3.enable()
        com4.enable()

        #esperando os dados do client

        bytesToGet, nBytes = com4.getData(3)

        time.sleep(0.1)
        
        com3.sendData(bytesToGet)

        time.sleep(0.1)

        dataToNum = int.from_bytes(bytesToGet, byteorder='big') 

        rxBuffer, nRx = com4.getData(dataToNum)

        print('recebeu {}'.format(rxBuffer))

        #acesso aos bytes recebidos
        rxLen = len(rxBuffer)
        print('Tamanho do que recebeu:', rxLen)

        #escrevendo na imagem
        print('Escrevendo na imagem') 
        f = open(imgW, 'wb').read()
        f.write(rxBuffer)
        f.close()
        print('Imagem escrita e arquivo fechado')

        print('-------------')
        print('Fim da transmissao')
        print('-------------')

        com3.disable()
        com4.disable()

    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()


if __name__ == "__main__":
    main()
