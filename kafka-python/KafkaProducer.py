from confluent_kafka import Producer
from faker import Faker
import json

fake = Faker()

p = Producer({
    'bootstrap.servers' : 'localhost:9092,localhost:9093,localhost:9094'
})

print(p.list_topics().topics)


def receipt(err,msg):
    if err is not None:
        print('Error : {}'.format(err))
    else:
        print('Message on topic on partition {}  with value of {}'.format(msg.topic(), msg.partition(), msg.value()))


for i in range(10):
    data = {
        'name' : fake.name(),
        'city'  : fake.city(),
        'message' : fake.text()
    }
    m = json.dumps(data)
    p.poll(0)
    p.produce('users', m.encode('utf-8'), callback=receipt)
    p.flush()

