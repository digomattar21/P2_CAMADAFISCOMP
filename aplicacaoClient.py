#####################################################
# Camada Física da Computação
#Carareto
#11/08/2020
#Aplicação
####################################################


#esta é a camada superior, de aplicação do seu software de comunicação serial UART.
#para acompanhar a execução e identificar erros, construa prints ao longo do código! 


from enlace import *
import time
import numpy as np

# voce deverá descomentar e configurar a porta com através da qual ira fazer comunicaçao
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

#use uma das 3 opcoes para atribuir à variável a porta usada
#serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
clientRX = "/dev/tnt1" # Mac    (variacao de)
clientTX = "/dev/tnt3"
#serialName = "COM6"                  # Windows(variacao de)


def main():
    try:
        
        com1 = enlace(clientTX) #envio
        com2 = enlace(clientRX) #recepcao

        com1.enable()
        com2.enable()
       
        print(com1)
        
        imgR = str(input('Digite o caminho do arquivo que vc deseja enviar: '))

        timeStart = time.time()

        txBuffer = open(imgR, 'rb').read()

        bytesToSend = len(txBuffer).to_bytes(3, byteorder='big')

        print(len(txBuffer))
        print(bytesToSend)

        com1.sendData(bytesToSend)

        time.sleep(0.1)
        
        bytesReceived, nBytes = com2.getData(3)
        print(bytesReceived)

        if bytesReceived == bytesToSend:
            print('Verificou')
        
        com1.sendData(txBuffer)
        time.sleep(0.1)

        print(len(txBuffer))

        txSize = com2.tx.getStatus()
        print('tamanho do que enviou {}'.format(txSize))

        timeEnd = time.time()
        txLen = len(txBuffer)

        delta_t = timeEnd - timeStart
        
        velocidade = txLen/delta_t

        print('Velocidade da comunicacao:  {} bytes/s'.format(velocidade))

        
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        com1.disable()
        com2.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
        

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
