import paramiko 

input()
host = '172.25.2.2'
user = 'admin'
secret = 'sxdc.1029!'
port = 22

input()
## 
##client = paramiko.SSHClient()
##client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
### Подключение
##client.connect(hostname=host, username=user, password=secret, port=port)
## 
### Выполнение команды
##stdin, stdout, stderr = client.exec_command('terminal length')
##
##
##stdin, stdout, stderr = client.exec_command('sh ver') 
### Читаем результат
##data = stdout.read() + stderr.read()
##print(data)
##input()
##client.close()
