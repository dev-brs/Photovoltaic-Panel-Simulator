import fotovoltaica
import graphics
import json
from paho.mqtt import client as mqtt_client

# Parâmetros de conexão TCP
host = 'test.mosquitto.org'
port = 1883
topic = 'Liberato/Tramposos/B_M'  # Tópico MQTT utilizado para a comunicação
client_id = '20000298'  # ID do cliente


def is_json(string):
    try:
        json.loads(string)
    except ValueError as e:
        return False
    return True


def connect_mqtt():
    # Callback para quando a conexão com o broker é estabelecida
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Conexão estabelecida com sucesso!")
        else:
            print(f"FALHA NA CONEXÃO, ERRO: {rc}")

    client = mqtt_client.Client(client_id)  # Criação do objeto do cliente
    client.on_connect = on_connect  # Atribuição do callback ao objeto
    client.connect(host, port)  # Conexão com o broker
    return client


# Função para se inscrever em um tópico no broker
def subscribe(client: mqtt_client):
    # Callback para quando uma mensagem é recebida
    def on_message(client, userdata, msg):
        print(msg.payload.decode())  # Exibe a mensagem recebida
        if is_json(msg.payload.decode()):
            print(json.loads(msg.payload.decode()))
            msg_dicpy = json.loads(msg.payload.decode())
            temperatura = msg_dicpy["temp"]
            radiacao = msg_dicpy["rad"]
            reset = msg_dicpy["PR"]
            opc = msg_dicpy["graph"]
            if reset == 1:
                graphics.reset_graphics()
            elif opc == 1:
                fotovoltaica.calculo_pot(temperatura, radiacao)
                graphics.plot_pot(graphics.curvas_pot)
            elif opc == 2:
                fotovoltaica.calculo_iv(temperatura, radiacao)
                graphics.plot_iv(graphics.curvas_iv)
            elif opc == 3:
                fotovoltaica.calculo_iv(temperatura, radiacao)
                graphics.plot_iv(graphics.curvas_iv)
                fotovoltaica.calculo_pot(temperatura, radiacao)
                graphics.plot_pot(graphics.curvas_pot)

    client.subscribe(topic)
    client.on_message = on_message  # Definição do callback a ser utilizado


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()
