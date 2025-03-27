
# Code Elevate - Monitoramento de Sensores IoT

 Este projeto implementa um sistema de monitoramento de sensores IoT utilizando Kafka, com Producer gerando dados falsos de sensores e enviando-os para um tópico Kafka, e Consumer consumindo esses dados para processamento e armazenamento em um banco de dados.

###

## Tecnologias utilizadas

Kafka (para mensageria e envio de dados)

Zookeeper (necessário para o funcionamento do Kafka)

Python (para os scripts do Producer e Consumer)

Docker (para orquestrar os containers Kafka e Zookeeper)

Banco de Dados PostgreSQL para armazenamento dos dados

###

## Estrutura do projeto

Producer: Gera dados falsos de sensores IoT e os envia para o tópico Kafka.

Consumer: Consome os dados do Kafka e os armazena em um banco de dados.

Kafka: Broker de mensagens para armazenar e distribuir os dados.

Zookeeper: Coordena o Kafka, mantendo os dados consistentes e distribuídos.

###

## Como rodar o projeto

1. Requisitos
Docker e Docker Compose instalados

Python 3.x instalado

2. Configurar Kafka e Zookeeper com Docker
Navegue até o diretório do projeto e crie os containers com Docker Compose:

'docker compose up -d'

3. Verificar se o Kafka está funcionando
Dentro do container do Kafka, você pode verificar se os tópicos estão sendo criados corretamente:

'docker exec -it monitoramento_de_sensores_iot-kafka-1 bash' 

'kafka-topics --list --bootstrap-server localhost:9092'

Se o tópico sensores não existir, ele será criado automaticamente na inicialização do Kafka com a configuração do docker-compose.yml.

4. Rodar o Producer
O Producer gera dados falsos e os envia para o tópico sensores no Kafka.


5. Rodar o Consumer
O Consumer lê os dados do Kafka e os armazena no banco de dados.

6. Verificar os Dados no Banco
Após o Consumer processar e armazenar os dados, você pode verificar se os dados foram armazenados corretamente no banco de dados.

7. Parar os Containers
Quando terminar, você pode parar os containers com:

'docker compose down'

###

## Como Funciona?

O Producer gera dados falsos de sensores (como temperatura, umidade, etc.) usando a biblioteca Faker e envia para o tópico "sensores" no Kafka.

O Kafka é o broker de mensagens que armazena esses dados e distribui para quem os consumir.

O Consumer recebe os dados do Kafka, processa e armazena no banco de dados escolhido (MySQL/PostgreSQL).


