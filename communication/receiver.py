import socket
import asyncio 
class Receiver():
    def __init__(self, ip:str, port:int, message_type:str="" ,socket_timeout:int = 3):
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
        self.socket.settimeout(socket_timeout)
        self.message = None
        self.status = False

    async def receive(self): 
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
            while self.status:
                data, addr = self.socket.recvfrom(1024)  # Buffer size is 1024 bytes
                self.message = data.decode()
        except KeyboardInterrupt:
            print("Gracefully closing...receiver")
        except socket.timeout:
            raise RuntimeError("Socket timed out.")
        except Exception as e:
            print("An error occurred:", e)
        
        finally:
            # Close the socket
            self.socket.close()
            print("Socket closed.")
        
    def start_receiving(self):
        """
        Change status to start receiving messages.
        """
        self.status = True
        
    def stop_receiving(self):
        """
        Change status to stop receiving messages.
        """
        self.status = False
        