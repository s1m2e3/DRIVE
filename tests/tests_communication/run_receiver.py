import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from communication.receiver import Receiver
import asyncio

receiver = Receiver(ip='127.0.0.1', port=12345, message_type="BSM")
receiver.start_receiving()
try:
    asyncio.run(receiver.receive())
except KeyboardInterrupt:
    print("Gracefully closing... receiver script")
