from kafka import KafkaProducer

bootstrap_servers = ''
topic = 'test'
key = b'111'
value = b'{"test": 123}'

producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

producer.send(topic=topic, key=key, value=value)
producer.flush()
