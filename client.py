import socket               # Import socket module
fileOpen = open("dummy.txt","rb")
fileRead = fileOpen.read()

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.connect((host, port))
while fileRead:
    s.send(fileRead)
    fileRead = fileOpen.read()
print("Successful")
fileOpen.close()
s.close                     # Close the socket when done

#import cv2
# import numpy as np
# image = cv2.imread("image.JPG")
# #cv2.imshow("image",image)
# #cv2.waitKey(0)
# encode_param=[int(cv2.IMWRITE_JPEG_QUALITY),90]
# result, encoded = cv2.imencode('.jpg', image,encode_param)
#
#
# encodedArray = np.array(encoded)
# encodedFinal = encodedArray.tostring()
#
# s = socket.socket()         # Create a socket object
# host = socket.gethostname() # Get local machine name
# port = 12345                # Reserve a port for your service.
# s.connect((host, port))
#
# s.send(encodedFinal)
# s.close                     # Close the socket when done
#
# decoded = cv2.imdecode(encodedArray,1)
# cv2.imshow("Client",decoded)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
