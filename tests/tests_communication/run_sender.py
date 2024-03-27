import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from communication.sender import Sender
import asyncio

sender = Sender(host_ip='127.0.0.1', host_port=12346, receiver_ip='127.0.0.1',
                receiver_port=12345, message="Hello from sender!", message_type="BSM")
sender.start_sending()
try:
    asyncio.run(sender.send())
except KeyboardInterrupt:
    print("Gracefully closing... sender script")