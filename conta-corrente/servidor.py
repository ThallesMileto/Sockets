import sys
import socket
 
T1 = '127.0.0.1'
T2 = 6006
T3 = 20  # Normally 1024, but we want fast response
T4 = None
 
if not len(sys.argv) >= 2:
    print ("[SERVIDOR][ERRO] O valor do saldo deve ser informado.")
    sys.exit(-1)
 
saldo = int(sys.argv[1])
print ("[SERVIDOR][INFO] Saldo inicial:", saldo)
 
print ("[SERVIDOR] Abrindo a porta " + str(T2) + " e ouvindo")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((T1, T2))
s.listen(1)
 
print ("[SERVIDOR] Aguardando conexao")
conn, addr = s.accept()
print ('[SERVIDOR] Conexao com o cliente realizada. Endereco da conexao:', addr)
while 1:
    print ("[SERVIDOR] Aguardando dados do cliente")
    operacao = conn.recv(T3).decode("utf-8")
    if not operacao: break
    print ("[SERVIDOR] Dados recebidos do cliente com sucesso: \"" + operacao + "\"")
   
    valores = operacao.split()
    if(valores[0] == 'saldo'):
        T4 = str(saldo)
    elif(valores[0] == 'credito'):
        saldo = saldo + int(valores[1])
        T4 = str(saldo)
    elif(valores[0] == 'debito'):
        saldo = saldo - int(valores[1])
        T4 = str(saldo)
       
    print ("[SERVIDOR] Enviando T4 para o cliente")
    conn.send(T4.encode())  # echo
    print ("[SERVIDOR] Resposta enviada: \"" + T4 + "\"")
print ("[SERVIDOR] Fechando a porta " + str(T2))
conn.close()
print ("[SERVIDOR] Fim")