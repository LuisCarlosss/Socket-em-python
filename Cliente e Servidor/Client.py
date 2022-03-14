import socket

hp = socket.gethostname(),7777
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(hp)
print('Você entrou no servidor!')


while True:
    #Enviar mensagem
    msg = input('Mensagem: ')
    if msg == 'close': #Usando comando close para desligar conexão e desligar servidor
        print('Saindo do servidor...')
        client.send('Cliente saiu do servidor!'.encode()) #enviar mensagem para servidor!
        break
        
    client.send(f'Client > {msg}'.encode())
    print('Esperando mensagem do servidor!')

    #Receber mensagem
    server_msg = client.recv(1024).decode() #mensagem do servidor
    if server_msg == 'Fechando servidor...':
        print('Servidor foi fechado!')
        break
    print(server_msg)

client.close()
