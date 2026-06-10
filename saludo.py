import datetime

def main():
    time = datetime.datetime.now()
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    meridian = time.strftime("%p")

    print("Hola, son las " + hour + ":" + minute + " " + meridian + "\n")

main()