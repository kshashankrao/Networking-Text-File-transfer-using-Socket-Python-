import numpy as np
import cv2
import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

print("Waiting for Client")
s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   data = c.recv(4096)
   fileOpen = open("Recieved.txt","wb")
   print(data)
   fileOpen.write(data)
   c.close
   break

# s = socket.socket()         # Create a socket object
# host = socket.gethostname() # Get local machine name
# port = 12345                # Reserve a port for your service.
# s.bind((host, port))        # Bind to the port
#
# print("Waiting for Client")
# s.listen(5)                 # Now wait for client connection.
# while True:
#    c, addr = s.accept()     # Establish connection with client.
#    print('Got connection from', addr)
#    data = c.recv(4096)
#    data = np.fromstring(data,dtype='uint8')
#    decoded = cv2.imdecode(data,1)
#    cv2.imshow("data",decoded)
#    cv2.waitKey(0)
#    cv2.imwrite("A.jpg",decoded)
#    cv2.destroyAllWindows()

   # #c.send(str.encode('Image Recieved'))
   # c.close()                # Close the connection
   # break
