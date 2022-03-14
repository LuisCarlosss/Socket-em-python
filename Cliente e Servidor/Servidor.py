import socket 
#path C:\Users\T-Gamer\Documents\GitHub\Socket-em-python\Cliente e Servidor

hp = socket.gethostname(),7777 
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(hp)
server.listen()
print('Abrindo Servidor...')

client,ip = server.accept()
print('{} Entrou no servidor!'.format(ip))

while True:
    #Receber mensagem
    cliente_msg = client.recv(1024).decode() #mensagem do cliente
    if cliente_msg == 'Cliente saiu do servidor!':
        print('Fechando servidor...')
        break
    print(cliente_msg)

    #Enviar mensagem
    msg = input('Mensagem: ')
    if msg == 'close': #Usando comando close para desligar conexão e desligar o servidor
        fs = 'Fechando servidor...'
        print(fs)
        client.send(fs.encode())
        client.close()
        break

    client.send(f'Servidor > {msg}'.encode()) #enviar mensagem para cliente
    print('Esperando mensagem do cliente!')


server.close()

