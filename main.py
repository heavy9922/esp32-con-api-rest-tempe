from connection import Wifi
import urequests
from machine import Pin as pin
from dht import DHT11
from utime import sleep
sensor = DHT11(pin(4))
boton = pin(15, pin.IN, pin.PULL_DOWN)


def wifi_con():
    name = 'yeferson'
    lastname = 'castiblanco'
    nameMoto = 'r15 v2'
    wifi = Wifi()
    if wifi.conectaWifi("Jadapa", "MENESES03"):

        print("Conexión exitosa!")
        print('Datos de la red (IP/netmask/gw/DNS):', wifi.miRed.ifconfig())
        while (True):
            sensor.measure()
            tempe = sensor.temperature()
            hume = sensor.humidity()
            button = boton.value()
            print(tempe, 'soy tempe', end="\t")
            print(hume, 'soy hume', end="\t")
            print(button)
            if button == 1:
                get = get_user()
                if len(get) == 0:
                    create_user(name, lastname, nameMoto, tempe, hume)
                    print('usuario creado')
                else:
                    for i in get:
                        if i['name'] is name and i['lastname'] is lastname:
                            print({"messages": "El usuario ya fue creado"})
                        else:
                            create_user(name, lastname, nameMoto, tempe, hume)
                            print('usuario creado')
            sleep(1)
    else:
        print("Imposible conectar")
        miRed.active(False)


def get_user():
    url = 'http://192.168.0.57:5000/user'
    response = urequests.get(url)
    return response.json()


def create_user(name, lastname, nameMoto, tempe, hume):
    url = 'http://192.168.0.57:5000/user'
    data = {
        'name': name,
        'lastname': lastname,
        'nameMoto': name,
        'temperaturaMoto': tempe,
        'humedadMoto': hume
    }
    response = urequests.post(url, json=data)
    return response.json()


def delete_user(id):
    url = f'http://192.168.0.57:5000/user/{id}'
    response = urequests.delete(url)
    print(response.json())
    return True


def update_user():
    url = 'http://192.168.0.57:5000/user/62c396eff366128d9a7a50d3'
    data = {
        'name': "yeferson",
        'nameMoto': "R15 v2",
        'temperaturaMoto': 60,
        'humedadMoto': 45
    }
    response = urequests.put(url, json=data)
    print(response.json())
    return True


if __name__ == '__main__':
    wifi_con()
