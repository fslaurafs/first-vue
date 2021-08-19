import paho.mqtt.client as mqtt
from random import randrange, uniform, randint
import time


mqttBroker = "IP MQTT BROKER"

client = mqtt.Client("Temperature_Inside")
client.connect(mqttBroker)


while True:
    randNumber = randint(-200, 200)
    client.publish("casa/cozinha/in4", randNumber)  # tópico
    time.sleep(3)   # 3 segundos

    print("Just Published " + str(randNumber) + " to topic TEMPERATURE")
    time.sleep(1)   # 1 segundo
