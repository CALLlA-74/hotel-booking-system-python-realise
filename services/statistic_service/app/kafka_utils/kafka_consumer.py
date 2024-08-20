from aiokafka import AIOKafkaConsumer
import asyncio

KAFKA_TOPIC = "booking.statistic.events.topic"
KAFKA_CONSUMER_GROUP = "group-id"
KAFKA_BOOTSTRAP_SERVERS = "kafka:29092"     # 'kafka_utils:9092'


async def consume():
    consumer = AIOKafkaConsumer(
        KAFKA_TOPIC,
        loop=asyncio.get_event_loop(),
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id=KAFKA_CONSUMER_GROUP
    )
    print("start consuming")
    await consumer.start()
    try:
        async for msg in consumer:
            print(f"Consumed msg: {msg}")
    except Exception as e:
        print(e)
    finally:
        await consumer.stop()
