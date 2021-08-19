import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, message):
    print("Received message: ", str(message.payload.decode("utf-8")),
          'tópico = ', message.topic)


mqttBroker = "IP MQTT BROKER"

client = mqtt.Client("Smartphone")
client.connect(mqttBroker)

client.loop_start()

client.subscribe("casa/#")      # todos os tópicos
client.on_message = on_message


while True:
    time.sleep(30)  # segundos

client.loop_stop()
