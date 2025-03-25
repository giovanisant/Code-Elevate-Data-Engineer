from kafka import KafkaProducer
import json
import time
from faker import Faker

fake = Faker()

#Conectar ao Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

NOME_TOPICO = "sensores"

#Gerar dados aleatórios
def gerador_dados():
    return {
        "sensor_id": fake.uuid4(),
        "temperatura": round(fake.pyfloat(min_value=15, max_value=40), 2),
        "umidade": round(fake.pyfloat(min_value=20, max_value=90), 2),
        "timestamp": fake.iso8601()
    }

#Loop infinito para enviar dados
try:
    while True:
        data = gerador_dados()
        producer.send(NOME_TOPICO, value=data)
        print(f"Enviado: {data}")
        time.sleep(15)  #Envia dados a cada 15 segundos

except KeyboardInterrupt:
    print("\nEncerrando o produtor...")
    producer.close()
