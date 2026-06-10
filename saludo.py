import datetime
import socket

name = socket.gethostname()
time = datetime.datetime.now()
hour = time.strftime("%I")
minute = time.strftime("%M")
meridian = time.strftime("%p")

print("Hola " + name + ", son las " + hour + ":" + minute + " " + meridian)

input("     Presione una tecla para salir...")