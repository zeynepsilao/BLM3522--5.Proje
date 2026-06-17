
import paho.mqtt.client as mqtt
import ssl
import time
import json
import random

AWS_ENDPOINT = "senin.iot.us-east-2.amazonaws.com" 
CLIENT_ID = "SanalHavaSensoru"
TOPIC = "sehir/sensor/hava" 

ROOT_CA = "senin-root.pem"
CERT_FILE = "senin-certificate.pem.crt" 
KEY_FILE = "senin-private.pem.key"      

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("AWS IoT Core'a başarıyla bağlanıldı! Veriler gönderiliyor...\n")
    else:
        print(f"Bağlantı hatası, Kod: {rc}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, CLIENT_ID)
client.on_connect = on_connect

client.tls_set(ca_certs=ROOT_CA, 
               certfile=CERT_FILE, 
               keyfile=KEY_FILE, 
               cert_reqs=ssl.CERT_REQUIRED, 
               tls_version=ssl.PROTOCOL_TLSv1_2, 
               ciphers=None)


print("AWS'ye bağlanmaya çalışılıyor...")
client.connect(AWS_ENDPOINT, 8883, 60) 
client.loop_start() 

try:
    while True:
        sicaklik = round(random.uniform(15.0, 35.0), 2)
        nem = round(random.uniform(30.0, 70.0), 2)
        
        payload = json.dumps({
            "cihaz": CLIENT_ID,
            "sicaklik_celsius": sicaklik,
            "nem_yuzde": nem,
            "durum": "aktif"
        })
        
        client.publish(TOPIC, payload, qos=1)
        print(f"Buluta giden veri -> {payload}")
        
        time.sleep(5)
        
except KeyboardInterrupt:
    print("\nSensör manuel olarak durduruldu.")
    client.loop_stop()
    client.disconnect()