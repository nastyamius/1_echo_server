import socket

sock = socket.socket()
sock.setblocking(1)

while True:
	addressIP = str(input('Введите IP-адрес "echo-сервера" или нажмите "enter", чтобы подключиться к IP-адресу по умолчанию: '))
	if len(addressIP) == 0:
		try: sock.connect(('10.0.2.15', 9000))
		except ConnectionRefusedError: print("Адрес по умолчанию не отвечает")
		else: break
	correct_check = addressIP.replace('.', '')
	correct_check = correct_check.replace(' ', '')
	for i in range(10): correct_check = correct_check.replace(str(i), '')
	if len(correct_check) != 0: print('В вашем адресе есть лишние символы, IP может содержать только точки и цифры')
	else:
		format = addressIP.split('.')
		if len(format) != 4: print('В вашем IP-адресе нет 3 точек')
		else:
			for i in range(4):
				if int(format[i]) > 255 or int(format[i]) < 0: 
					print('Неверный IP-адрес, nubers должен быть в диапазоне от 0 до 255')
					break
			else:
				try:
					portNum = int(input('Введите номер порта:'))
				except:
					print('Неправильные символы, номер порта может содержать только 4 цифры')
				else:
					if portNum < 9999 and portNum > 1024:
						try: sock.connect((addressIP, portNum))
						except ConnectionRefusedError:	print('Нет сервера с таким адресом и портом')
						else: break
					else: print('неправильнsq диапозон')
print('Успешно подключенный! Нажмите Enter, чтобы продолжить')
msg = ''
a = 0
while msg!= 'выход':
	msg = input()
	print()
	sock.send(msg.encode())
	if a != 0:print('Сообщение успешно отправлен!\n')
	else: a = 1
	data = sock.recv(1024)
	print('Вы получили сообщение!\n')
	print(data.decode())
	print()
print('Соединение закрыто')
sock.close()
