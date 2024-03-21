import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import pytest
import pytest_asyncio
import socket
import json
from unittest.mock import MagicMock
from communication.receiver import Receiver
import asyncio
# # @pytest.fixture
# # def mock_socket():
# #     with patch('socket.socket') as mock_socket:
# #         yield mock_socket.return_value
# @pytest_asyncio.fixture()
# # async def async_receiver():
# async def sender():
#     # Create a UDP socket
#     sender_socket = await asyncio.open_connection('127.0.0.1', 12345)

#     # Send message to localhost
#     message = "Hello from sender!"
#     sender_socket[1].write(message.encode())
#     print("Message sent from sender")

# async def listener():
#     ip = '127.0.0.1'
#     port = 12345
#     receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     receiver.bind((ip, port))
#     print("Receiver connected to the server.")
#     while True:
#         print('Waiting for message')
#         data, addr = receiver.recvfrom(1024)  # Buffer size is 1024 bytes
#         print(f"Received message: {data.decode()} from {addr}")
#         await asyncio.sleep(0.1)
   
# async def main():
#     print('here')
#     await asyncio.gather(listener(),sender())
    
# asyncio.run(main())
import asyncio

async def receiver():
    # Create a UDP socket
    receiver_socket = await asyncio.start_server(handle_receiver, '127.0.0.1', 33333)

    print("Receiver started. Waiting for messages...")

    async with receiver_socket:
        await receiver_socket.serve_forever()

async def handle_receiver(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')
    print(f"Received message from {addr}: {message}")

async def sender():
    # Create a UDP socket
    sender_socket = await asyncio.open_connection('127.0.0.1', 33333)

    # Send message to localhost
    message = "Hello from sender!"
    sender_socket[1].write(message.encode())
    print("Message sent from sender")

async def main():
    await asyncio.gather(receiver(), sender())

if __name__ == "__main__":
    asyncio.run(main())


   
    # yield receiver.receive()

# @pytest.mark.asyncio
# async def test_receive(monkeypatch):
#     """
#     A function to test the calling of the receive method of a Receiver object using monkeypatching.
    
#     Parameters:
#     - monkeypatch: a pytest fixture for monkeypatching
    
#     Returns:
#     - None
#     """
    
#     @pytest.mark.asyncio
    
    # task2 = asyncio.create_task(async_receiver())
    # value_task2 = await task2
    # asyncio.gather(task1, task2)
    # print(list(value_task2))
    # del receiver
    # mock_inside.assert_called_with("Test message")
    
    
# def test_update_message(monkeypatch):
#     receiver = Receiver(ip='127.0.0.1', port=1234)
#     mock_inside = MagicMock()
#     monkeypatch.setattr(receiver, 'update_message', mock_inside)
    
#     ip = '127.0.0.1'
#     port = 1234
#     message_sent = "Test message"
#     sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     sender.connect((ip, port+1))
#     sender.sendto(message_sent.encode(), (ip, port))

#     receiver.receive()
#     mock_inside.assert_called_once()
#     del receiver
    

# if __name__ == '__main__':
#     pytest.main(['-v', '-s', __file__])