from aiokafka import AIOKafkaConsumer
from config.config import get_kafka_settings
from services import add_event_info
from database.database import Database
from schemas.dto import EventInfoDTO
import asyncio
import json

kafka_config = get_kafka_settings()
kafka_topic = kafka_config['topic'] # "booking.statistic.events.topic"
kafka_consumer_group = kafka_config['consumer_group'] # "group-id"
kafka_bootstrap_server = kafka_config['bootstrap_server']     # "kafka:29092"     # 'kafka_utils:9092'


async def consume(app_db: Database):
    consumer = AIOKafkaConsumer(
        kafka_topic,
        loop=asyncio.get_event_loop(),
        bootstrap_servers=kafka_bootstrap_server,
        group_id=kafka_consumer_group
    )
    print("start consuming")
    await consumer.start()
    try:
        async for msg in consumer:
            event_info = EventInfoDTO.model_validate(json.loads(msg.value.decode('utf-8')))
            print(f"DTO event_info obj: {event_info}")
            db = app_db.get_session()
            await add_event_info(event_dto=event_info, db=db)
    except Exception as e:
        print(e)
    finally:
        await consumer.stop()
