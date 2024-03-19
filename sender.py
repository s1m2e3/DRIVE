import socket
import time
# IP address and port to listen on
host = '192.168.0.138'  # Listen on all available interfaces
portTIM = 22222
portPSM = 33333

# Create a UDP socket
sockTIM = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockPSM = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the host and port
counterTIM = 1
counterPSM = 1

while True:
    # Send data
    messageTIM = 'here TIM: ' + str(counterTIM)
    messagePSM = 'here PSM: ' + str(counterPSM)
    sockTIM.sendto(messageTIM.encode(),(host,portTIM))
    print('message:'+messageTIM+ 'send to sockTIM')
    sockPSM.sendto(messagePSM.encode(),(host,portPSM))
    print('message:'+messagePSM+ 'send to sockPSM')
    counterPSM +=1
    counterTIM +=1
    time.sleep(0.1)
# Close the socket
sock.close()
