import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from communication.receiver import Receiver
import asyncio
import pytest

def test_receiver_sender_off():

    @pytest.mark.asyncio
    async def main(receiver: Receiver):
        try:
            async for message in receiver.receive():
                assert message == "Hello from sender!"
                print("Message received successfully.")
                return
        except RuntimeError:
            assert True
    receiver = Receiver(ip='127.0.0.1', port=12345, message_type="BSM")
    asyncio.run(main(receiver))

def test_receiver_sender_on():

    @pytest.mark.asyncio
    async def main(receiver: Receiver):
        try:
            async for message in receiver.receive():
                assert message == "Hello from sender!"
                print("Message received successfully.")
                return
        except Exception as e:
            print("An error occurred:", e)
            raise AssertionError

    receiver = Receiver(ip='127.0.0.1', port=12345, message_type="BSM")
    asyncio.run(main(receiver))