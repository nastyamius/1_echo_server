import socket
import datetime

print(datetime.now, 'начало работы сервера')
greet = 'Привет!'
sock = socket.socket()
portNum = 9000
while True:

	try: sock.bind(('', portNum))
	except:	portNum += 1
	else: break

print('Сервер открыт по порту: ', portNum)
c = 0
users = {'key':'info'}
print(list(users.keys()))
while c<5:
	print('Поиск связи')
	sock.listen()
	conn, addr = sock.accept()
	print(addr[0])
	curr = list(users.keys())
	print("Соединение с", addr)
	for i in range(len(curr)):
		if str(curr[i]) == str(addr[0]):
			greet1 = greet + users[addr[0]] + '!'
			conn.send(bytes(greet1, encoding = 'utf-8'))
			break
	else:
		print('запрошенный ник')
		conn.send(b'Привет! Введите имя:')
		sock.listen(0)
		Username = ''
		while Username == '':
			data = conn.recv(1024)
			if not data:
				None
			else:
				Username = str(data)
				Username = Username.replace("'", "")
				Username = Username.replace('b', '', 1)
				print(Username)
				users[addr[0]] = Username
				print('Успешно!')
				conn.send(b'Добро пожаловать на сервер!')
				print(users)
				break
	sock.listen(0)
	msg = ''
	while msg != 'exit':
		msg = ''
		msg = users[addr[0]] + ': '
		data = conn.recv(1024)
		print('Полученное сообщение от ', users[addr[0]])
		if not data:
			break
		msg += data.decode()
		data2 = bytes(msg, encoding = 'utf-8')
		print(msg)
		conn.send(data2)
		print('Сообщение, отправленное этому пользователю!')

	conn.close()
	c += 1
	print('Соединение завершено')
print('Server closed')
