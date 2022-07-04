# Envia temperatura y humedad a Drive a traves de ifttA
# https://ifttt.com/maker_webhooks

import network
import time


class Wifi:
    def __init__(self):
        self.miRed = ''

    def conectaWifi(self, red, password):
        self.miRed = network.WLAN(network.STA_IF)
        if not self.miRed.isconnected():  # Si no está conectado…
            self.miRed.active(True)  # activa la interface
            self.miRed.connect(red, password)  # Intenta conectar con la red
            print('Conectando a la red', red + "…")
            timeout = time.time()
            while not self.miRed.isconnected():  # Mientras no se conecte..
                if (time.ticks_diff(time.time(), timeout) > 10):
                    return False
        return True
