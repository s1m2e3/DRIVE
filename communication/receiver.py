import socket
import json

class Receiver():
    def __init__(self, ip:str, port:int, message_type:str="" ):
        """
        Initialize the object with the provided IP, port, and message_type.

        Parameters:
            ip (str): The IP address to bind the socket.
            port (int): The port number to bind the socket.
            message_type (str): The type of message (default is an empty string).

        Returns:
            None
        """
        self.message_type = message_type
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.message = None
        self.receive()
    def receive(self):
        """
        A method to receive data from a server using a socket connection. 
        Binds to the specified IP address and port, then continuously listens for incoming data. 
        Prints out the received message along with the sender's address. 
        Catches any exceptions that might occur during the process. 
        Finally, closes the socket connection. 
        """
        try:
        # Connect to the server
            self.socket.bind((self.ip,self.port))
            print("Connected to the server.")
            while True:
                data, addr = self.socket.recvfrom(1024)  # Buffer size is 1024 bytes
                print(f"Received message: {data.decode()} from {addr}")
                self.update_message(data.decode())
        except Exception as e:
            print("An error occurred:", e)

        finally:
            # Close the socket
            self.socket.close()
            print("Socket closed.")
    def update_message(self,message:str):
        """
        Updates the message attribute with the JSON-serialized version of the input message.

        Parameters:
            message (str): The message to be JSON-serialized and stored.

        Returns:
            None
        """
        self.message = json.dumps(message)
        yield self.message
        

