from connection import Wifi

def wifi_con():
    wifi = Wifi()
    if wifi.conectaWifi("Jadapa", "MENESES03"):

        print("Conexión exitosa!")
        print('Datos de la red (IP/netmask/gw/DNS):', wifi.miRed.ifconfig())

        while (True):
            pass

    else:
        print("Imposible conectar")
        miRed.active(False)

def main():
    pass

if __name__ == '__main__':
    wifi_con()
    main()