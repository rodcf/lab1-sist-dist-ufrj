# lab1-sist-dist-ufrj
Laboratório 1 da disciplina de Sistemas Distribuídos da UFRJ

Objetivo: Desenvolver uma aplicação distribuída básica usando o modelo de interação requisição/resposta (ou modo ativo/passivo).

Roteiro: A aplicação será um “servidor de echo”, que envia de volta para o emissor a mesma mensagem recebida.

1. Implemente o lado passivo que coloca-se em modo de espera por conexões, recebe a mensagem do lado passivo e a envia de volta, e repete esse procedimento até que o lado ativo encerre a conexão.

2. Implemente o lado ativo que conecta-se com o servidor de echo, envia uma mensagem digitada pelo usuário, aguarda e imprime a mensagem recebida de volta.

3. Defina um código para o usuário indicar que não deseja mais enviar mensagens para o servidor de echo. Quando esse código for digitado pelo usuário, a aplicação deverá ser encerrada.