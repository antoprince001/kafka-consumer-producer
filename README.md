# kakfa-consumer-producer
Apache Kafka consumers and producers developed using python and spring boot as a learning exercise

## Apache Kafka Setup 

Command to setup Zookeeper and Apache Kafka: 
```
docker-compose -f docker-compose.yml up -d
```

To tear-down the setup

```
docker-compose down
```

## Project implementation

Spring Boot - Producer1 , Consumer1
Python      - Producer2 , Consumer2

Spring Boot Producer1 sends a log message and the python Consumer2 subscribes to that topic and listens to it.

Python Producer2 uses Faker module to generate fake data and publish it to 'users' topic. Consumer1 defined in Spring Boot listens to the 'users' topic and consumes the data.

![Project Architecture](https://github.com/antoprince001/kakfa-consumer-producer/blob/main/Architecture.png)
