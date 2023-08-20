import boto3
myec2 = boto3.resource("ec2"  )

"""
You also have to configure AWS 
First Downoad this file - https://awscli.amazonaws.com/AWSCLIV2.ms
Then Go to cmd and write "aws configure"
Then put the aws detail 
"""
def launchOS():
    response = myec2.create_instances( 
        ImageId="ami-0da59f1af71ea4ad2",  
        InstanceType="t2.micro",
        MaxCount=1,
        MinCount=1
    )

import  cv2
cap = cv2.VideoCapture( 1 ) #here you can select camera using number

from cvzone.HandTrackingModule import HandDetector
detector = HandDetector()



while True:
    status , photo = cap.read()
    cv2.imshow("my photo" , photo)
    if cv2.waitKey(100) == 13:
        break
    
    handphoto = detector.findHands(photo , draw=False)
    
    if handphoto:
        lmlist = handphoto[0]
        fingerstatus = detector.fingersUp(lmlist)

        if fingerstatus == [1,1,1,1,1]:
            print("all up")
            launchOS()
            launchOS()
            launchOS()
            launchOS()
            launchOS()
    
        elif fingerstatus == [ 0 ,1 ,0 , 0, 0]:
            print("index finger up")
            launchOS()
    
        elif fingerstatus == [ 0 , 1, 1, 0 , 0 ]:
            print("index and middle finger up")
            launchOS()
            launchOS()
    
        else:
            print("idk")

        
cv2.destroyAllWindows()	#To close the camera window after entering


cap.release()	#To release the camera because your pyhton code use the camera
