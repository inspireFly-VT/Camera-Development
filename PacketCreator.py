from PIL import Image
from io import BytesIO
import ProcessImage


#Creates a string of characters from the image bytes starting from startingIndex and packetLength characters long.
def getNextPacket(bytesVar, packetLength, numPackets, startingIndex):

    currPacketString = ""
    for x in range(packetLength):
        currPacketString = currPacketString + str(bytesVar[x + startingIndex])
    startingIndex = startingIndex + packetLength
    
    return startingIndex, currPacketString
    
#This code would be implemented in a different file
numPackets = 5
packetLength = 100
startingIndex = 0
img = r"C:\Users\micha\Documents\Virginia Tech\InspireFly\CameraCaptures\High-Res_Test.jpg"
bytesVar = str(ProcessImage.ImageToBytes(img))
print(bytesVar)

for x in range(numPackets):
    startingIndex, currPacketString = getNextPacket(bytesVar, packetLength, numPackets, startingIndex)
    print(currPacketString)
    print("")
