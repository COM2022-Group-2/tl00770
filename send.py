import socket
from datetime import datetime
from clients import memberDict
import time

#add time and condition on date match to send to specific ip for each member
dt = datetime.today().strftime('%d/%m')
s= 4
def encryp(MESSAGE, s):
   # transverse the plain text
    for i in range(len(MESSAGE)):
        char = MESSAGE[i]
        # Encrypt uppercase characters in plain text
        
        if (char.isupper()):
            MESSAGE += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            MESSAGE += chr((ord(char) + s - 97) % 26 + 97)
            encryptedMsg = MESSAGE
    return encryptedMsg'

MESSAGE = "Well done!"
print(encryp(MESSAGE, s))
#this will run the code repeatedly with fixed time
starttime = time.time()
while True:
#for every key in memberDict
#it will check if theres birthday match
#if yes it will match back the key to extract the ip address of the person
    for key in memberDict:
        if memberDict[key][0] == dt:
            UDP_IP = memberDict[key][1]
            UDP_IP = bytes.decode(UDP_IP) #change binary to string
            MESSAGE = "Happy birthday to you! " + key
            MESSAGE = str.encode(MESSAGE) #change string to binary
            UDP_PORT = 1001
            
            sock = socket.socket(socket.AF_INET, # Internet socket
                                socket.SOCK_DGRAM) # UDP
            sock.sendto(encryp(MESSAGE), (UDP_IP, UDP_PORT)) #send message to specific ip and port

            print("UDP target IP: %s" % UDP_IP)
            print("UDP target port: %s" % UDP_PORT)
            #decode it so message preview wont have 'b' (which is binary prefix) before message
            MESSAGE = bytes.decode(MESSAGE)
            print("message: %s" % MESSAGE)
            #run the code every after 24 hours
            time.sleep(86400)
        else:
            #run the code every after 24 hours
            time.sleep(86400)
