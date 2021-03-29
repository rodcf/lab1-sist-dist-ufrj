# Exemplo basico socket (lado ativo)

import socket as sock

HOST = 'localhost' # maquina onde esta o par passivo
PORT = 5000        # porta que o par passivo esta escutando

# cria socket
activeSocket = sock.socket() # default: socket.AF_INET, socket.SOCK_STREAM 

# conecta-se com o par passivo
activeSocket.connect((HOST, PORT))

while True:

    # obtem a mensagem a ser enviada por meio do input do usuario
    msgToSend = input('Digite a mensagem que deseja enviar: ')

    # caso a mensagem inserida seja a palavra-chave 'exit', encerra o loop
    if msgToSend == 'exit':
        break

    # envia a mensagem para o par conectado
    activeSocket.send(bytes(msgToSend, encoding='utf-8'))

    # imprime a mensagem enviada
    print('Mensagem enviada: ', msgToSend)

    #espera a resposta do par conectado (chamada pode ser BLOQUEANTE)
    receivedMsg = activeSocket.recv(1024) # argumento indica a qtde maxima de bytes da mensagem

    # imprime a mensagem recebida
    print('Mensagem recebida: ', str(receivedMsg, encoding='utf-8'))

# encerra a conexao
activeSocket.close() 