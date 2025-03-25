from kafka import KafkaConsumer
import json
import psycopg2

NOME_TOPICO = "sensores"

try:
    #Conectar ao banco de dados PostgreSQL
    conn = psycopg2.connect(
        dbname="CODEELEVATE",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432",
    )
    conn.set_client_encoding('UTF-8')
    cursor = conn.cursor()

    #Criar tabela se não existir
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensores (
            id SERIAL PRIMARY KEY,
            sensor_id TEXT,
            temperatura REAL,
            umidade REAL,
            timestamp TIMESTAMP
        );
    """)
    conn.commit()

    consumer = KafkaConsumer(
        NOME_TOPICO,
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda v: json.loads(v.decode('utf-8'))
    )

    print("Aguardando mensagens...")

    for message in consumer:
        data = message.value
        try:
            cursor.execute(
                "INSERT INTO sensores (sensor_id, temperatura, umidade, timestamp) VALUES (%s, %s, %s, %s)",
                (data['sensor_id'], data['temperatura'], data['umidade'], data['timestamp'])
            )
            conn.commit()
            print(f"Salvo no banco: {data}")
        except Exception as e:
            print(f"Erro ao salvar no banco: {e}")

except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")