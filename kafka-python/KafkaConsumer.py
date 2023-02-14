from confluent_kafka import Consumer

c = Consumer({
    'bootstrap.servers' : 'localhost:9092,localhost:9093,localhost:9094',
    'group.id' : 'python-consumer',
    'auto.offset.reset' : 'earliest'
})

print(c.list_topics().topics)

c.subscribe(['log'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        print('Error : {}'.format(msg.error()))

    data = msg.value().decode('utf-8')
    print(data)

c.close()
