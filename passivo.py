# Exemplo basico socket (lado passivo)

import socket as sock

HOST = '' # '' possibilita acessar qualquer endereco alcancavel da maquina local
PORT = 5000 # porta onde chegarao as mensagens para essa aplicacao

# cria um socket para comunicacao
passiveSocket = sock.socket() # valores default: socket.AF_INET, socket.SOCK_STREAM  

# vincula a interface e porta para comunicacao
passiveSocket.bind((HOST,PORT))

# define o limite maximo de conexoes pendentes e coloca-se em modo de espera por conexao
passiveSocket.listen(1)

# aceita a primeira conexao da fila (chamada pode ser BLOQUEANTE)
connectionSocket, address = passiveSocket.accept() # retorna um novo socket e o endereco do par conectado

# imprime o par (IP,PORTA) da conexao 
print('Conectado com: ', address)

while True:

    # depois de conectar-se, espera uma mensagem (chamada pode ser BLOQUEANTE)
    msg = connectionSocket.recv(1024) # argumento indica a qtde maxima de dados

    # transforma a mensagem recebida em bytes para string
    msgString = str(msg,encoding='utf-8')

    # caso a mensagem recebida seja de encerramento ou seja a palavra-chave 'exit', encerra o loop
    if not msg or msgString == 'exit':
        break

    else:
        # imprime a mensagem recebida
        print('Mensagem recebida: ', msgString)

        # envia mensagem de resposta igual a mensagem recebida (echo)
        connectionSocket.send(msg)

# fecha o socket da conexao
connectionSocket.close()

# fecha o socket principal
passiveSocket.close()