import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from communication.receiver import Receiver
import asyncio
import pytest

def test_receiver_sender_off():

    @pytest.mark.asyncio
    async def main(receiver: Receiver):
        receiver.start_receiving()
        try:
            await receiver.receive()
        except RuntimeError:
            assert True
    receiver = Receiver(ip='127.0.0.1', port=12345, message_type="BSM")
    asyncio.run(main(receiver))

def test_receiver_sender_on_yield_message():

    @pytest.mark.asyncio
    async def get_message(receiver: Receiver):
        pass
        assert "Hello from sender!" == receiver.message
        receiver.stop_receiving()
     
    async def main(receiver: Receiver):
        receiver.start_receiving()
        try:
            # assert True
            # # await receiver.receive()
            # print('here')
            # # await get_message(receiver)
            asyncio.gather(receiver.receive(), get_message(receiver))
            assert False
            print("Message received successfully.")
            return
        except Exception as e:
            print("An error occurred:", e)
            raise AssertionError

    receiver = Receiver(ip='127.0.0.1', port=12345, message_type="BSM")
    asyncio.run(main(receiver))

def test_receiver_sender_turn_off():

    @pytest.mark.asyncio
    async def main(receiver: Receiver):
        receiver.start_receiving()
        try:
            receiver.receive()
            assert "Hello from sender!" == receiver.message
            print("Message received successfully.")
            receiver.status = False
            assert receiver.socket._closed
            return
        except Exception as e:
            print("An error occurred:", e)
            raise AssertionError
        
    receiver = Receiver(ip='127.0.0.1', port=12345, message_type="BSM")
    asyncio.run(main(receiver))
    assert True