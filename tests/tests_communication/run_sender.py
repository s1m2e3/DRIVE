import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from communication.sender import Sender


sender = Sender(host_ip='127.0.0.1', host_port=12346, receiver_ip='127.0.0.1',
                receiver_port=12345, message="Hello from sender!", message_type="BSM")

try:
    while True:
        sender.send()
except KeyboardInterrupt:
    print("Gracefully closing...sender script")
except Exception as e:
    print("An error occurred:", e)


