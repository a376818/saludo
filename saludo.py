import datetime
from time import sleep

def main():
    time = datetime.datetime.now()
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    meridian = time.strftime("%p")

    print("Hola, son las " + hour + ":" + minute + " " + meridian)
    input("     Presione enter para salir...\n")

main()