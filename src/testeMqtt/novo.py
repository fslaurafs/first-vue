import asyncio
import paho.mqtt.client as mqtt
from random import randint


async def led(maquina, url_base, pos, mosquitto):
    valor = 0

    while True:
        await asyncio.sleep(randint(5, 20))
        print(f'{url_base}/{maquina}/leds/{pos} - ', valor.__str__().encode())
        mosquitto.publish(f'{url_base}/{maquina}/leds/{pos}', valor.__str__().encode())

        if valor == 0:
            valor = 1
        else:
            valor = 0


async def temperatura(maquina, url_base, pos, mosquitto):
    valor = 20

    while True:
        await asyncio.sleep(randint(1, 5))
        print(f'{url_base}/{maquina}/temperatura/{pos} - ', valor.__str__().encode())
        mosquitto.publish(f'{url_base}/{maquina}/temperatura/{pos}', valor.__str__().encode())
        valor = randint(18, 50)


async def corrente(maquina, url_base, pos, mosquitto):
    tempo = 1
    valor = 7

    while True:
        await asyncio.sleep(tempo)
        print(f'{url_base}/{maquina}/correntes/{pos} - ', valor.__str__().encode())
        mosquitto.publish(f'{url_base}/{maquina}/correntes/{pos}', valor.__str__().encode())
        valor = randint(5, 10)


async def tensao(maquina, url_base, pos, mosquitto):
    tempo = 5
    valor = 380

    while True:
        await asyncio.sleep(tempo)
        print(f'{url_base}/{maquina}/tensoes/{pos} - ', valor.__str__().encode())
        mosquitto.publish(f'{url_base}/{maquina}/tensoes/{pos}', valor.__str__().encode())
        valor = randint(370, 400)



async def alarme(maquina, url_base, pos, mosquitto):
    valor = 1

    while True:
        await asyncio.sleep(randint(5, 20))
        print(f'{url_base}/{maquina}/alarmes/{pos} - ', valor.__str__().encode())
        mosquitto.publish(f'{url_base}/{maquina}/alarmes/{pos}', valor.__str__().encode())

        if valor == 0:
            valor = 1
        else:
            valor = 0


async def maquina(maquina, url_base, mqttBroker):
    client = mqtt.Client(maquina)
    client.connect(mqttBroker)

    for x in range(5):
        asyncio.create_task(led(maquina, url_base, f'led{x}', client))
    for x in range(2):
        asyncio.create_task(temperatura(maquina, url_base, f'temp{x}', client))
    for x in range(1):
        asyncio.create_task(corrente(maquina, url_base, f'corrente{x}', client))
    for x in range(1):
        asyncio.create_task(tensao(maquina, url_base, f'tensao{x}', client))
    for x in range(1):
        asyncio.create_task(alarme(maquina, url_base, f'alarme{x}', client))


mqttBroker = "autbackup"
url_base = 'aut_lab'

loop = asyncio.get_event_loop()
loop.create_task(maquina('maquina - 1', url_base, mqttBroker))
loop.create_task(maquina('maquina - 2', url_base, mqttBroker))
loop.create_task(maquina('maquina - 3', url_base, mqttBroker))
loop.create_task(maquina('maquina - 4', url_base, mqttBroker))

loop.run_forever()
