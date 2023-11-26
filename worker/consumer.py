import logging

import boto3
from django.core.management.base import BaseCommand
from django.conf import settings

from openai import OpenAI

logger = logging.Logger(__name__)
sqs = boto3.client("sqs")


class Command(BaseCommand):
    help = "Consume messages from rabbitmq"

    def handle(self, *args, **options):
        while True:
            # Receive message from SQS queue
            response = sqs.receive_message(QueueUrl=settings.SQS_URL)

            # Check if any messages were received
            for message in response["Messages"]:
                try:
                    event = message.get("Body")
                    process_message(event)
                    receipt_handle = message["ReceiptHandle"]
                    sqs.delete_message(
                        QueueUrl="https://sqs.us-east-1.amazonaws.com/073317479885/btg-team6-docgen-request",
                        ReceiptHandle=receipt_handle,
                    )
                except Exception as e:
                    logger.info("error on consumer", e)
                    print(e)
            else:
                break
