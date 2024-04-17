import socket
import asyncio
from ..messages.message import Message, MessageType
from ..messages.inspector import Inspector
from typing import Union

class Sender():
    def __init__(self,message_type:Union[MessageType.BSM,MessageType.TIM,MessageType.PSM,MessageType.RSA], host_ip:str, host_port:int, receiver_ip:str, receiver_port:int, message:str=""):
        """
        Initialize the object with the provided IP, port, message, and message_type.

        Parameters:
            host_ip (str): The IP address to connect the socket.
            host_port (int): The port number to connect the socket.
            receiver_ip (str): The IP address of the receiver.
            receiver_port (int): The port number of the receiver.
            message (str): The message to send.
            message_type (str): The type of message (default is an empty string).
        Returns:
            None
        """
        self.message_type = message_type
        self.inspector = Inspector(message_type)
        self.host_ip = host_ip
        self.host_port = host_port
        self.receiver_ip = receiver_ip
        self.receiver_port = receiver_port
        self.status = False
        self.message = message
        self.message_object = None

        
    async def send(self):
        """
        A method to send data to a server using a socket connection. 
        Connects to the specified IP address and port, then sends the message.
        Catches any exceptions that might occur during the process. 
        Finally, closes the socket connection. 
        """
        
        try:
            # Initialize socket
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            # Connect to the server
            self.socket.connect((self.host_ip, self.host_port))
            while self.status:
                # Inspect if message in string format on the messages list from transceiver is properly formatted, if it is then store the message object in self.message_object
                # and then forward the message to the receiver. The inspector class will correct the message if necessary and possible. 
                if self.message is not "":
                    self.message_object,self.message = self.inspector.inspect_sending(self.message)
                    if self.message_object is not None:
                        self.socket.sendto(self.message.encode(), (self.receiver_ip, self.receiver_port))
                        print("Message sent successfully:", self.message)
                        await asyncio.sleep(0.001)
                    else:
                        print("No message to send.")
        except KeyboardInterrupt:
            print("Gracefully closing...sender")
        except Exception as e:
            print("An error occurred:", e)

        finally:
            # Close the socket
            self.socket.close()
       
    def update_message(self,message:str):
        """
        Update the message attribute with a new message.

        Parameters:
            message (str): The new message to update the attribute with.
        """
        self.message = message
    def start_sending(self):
        """
        Change status to start sending messages.
        """
        self.status = True
    
    def stop_sending(self):
        """
         Change status to stop sending messages.
        """
        self.status = False