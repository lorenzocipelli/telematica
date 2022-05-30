from callbacks import on_subscribe, on_message, on_connect
from utils import USERNAME, PSW, URL, PORT, LOCALHOST
from pymongo import MongoClient

import paho.mqtt.client as paho
from paho import mqtt

#client_mongo_db = MongoClient(LOCALHOST, connect=False) 
#oil_prices = client_mongo_db.oil_database.oil_prices

client_mqtt = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client_mqtt.on_connect = on_connect

# abilito TLS per una connessione sicura
client_mqtt.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# imposta username e password
client_mqtt.username_pw_set(USERNAME, PSW)
# connetto a HiveMQ Cloud sulla porta 8883 (default per MQTT)
client_mqtt.connect(URL, PORT)

# imposto le callback
client_mqtt.on_subscribe = on_subscribe
client_mqtt.on_message = on_message

# iscrizione ai topic di interesse
client_mqtt.subscribe([("premier_league_news/arsenal", 1),("premier_league_news/heating_gas_oil", 1)])
client_mqtt.subscribe("premier_league_news/#", 1)
#client_mqtt.subscribe([("fuel_prices/euro_super_95", 1),("fuel_prices/west_ham_united", 1)])
#client_mqtt.subscribe("fuel_prices/#", 1)

# entro in loop di ascolto, grazie a questo comando sono rese effettive le callback
client_mqtt.loop_forever()