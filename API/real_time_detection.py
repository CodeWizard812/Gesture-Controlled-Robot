import cv2
import numpy as np
from keras.models import load_model
import sim
from time import sleep as delay
import sys

model = load_model("Gesture_Detection_Model48x48.h5")


def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1,48,48,1)
    return feature/255.0

print('Program started')
sim.simxFinish(-1)
clientID = sim.simxStart('127.0.0.1', 19999, True, True, 5000, 5)

lSpeed = 0
rSpeed = 0

if (clientID != -1):
    print('Connected to remote API server')

else:
    sys.exit('Failed connecting to remote API server')

delay(1)

errorCode, left_motor_handle = sim.simxGetObjectHandle(
    clientID, '/PioneerP3DX/leftMotor', sim.simx_opmode_oneshot_wait)
errorCode, right_motor_handle = sim.simxGetObjectHandle(
    clientID, '/PioneerP3DX/rightMotor', sim.simx_opmode_oneshot_wait)

delay(1)



cap = cv2.VideoCapture(0)
label = ['backward', 'brake', 'forward', 'left', 'null', 'right']
while True:
    _,frame = cap.read()
    cv2.rectangle(frame,(0,40),(300,300),(0, 165, 255),1)
    cropframe=frame[40:300,0:300]
    cropframe=cv2.cvtColor(cropframe,cv2.COLOR_BGR2GRAY)
    cropframe = cv2.resize(cropframe,(48,48))
    cropframe = extract_features(cropframe)
    pred = model.predict(cropframe) 
    prediction_label = label[pred.argmax()]
    cv2.rectangle(frame, (0,0), (300, 40), (0, 165, 255), -1)
    if prediction_label == 'null':
        cv2.putText(frame, " ", (10, 30),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 255, 255),2,cv2.LINE_AA)
    else:
        accu = "{:.2f}".format(np.max(pred)*100)
        cv2.putText(frame, f'{prediction_label}  {accu}%', (10, 30),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 255, 255),2,cv2.LINE_AA)
    cv2.imshow("output",frame)
    cv2.waitKey(27)
    
    errorCode = sim.simxSetJointTargetVelocity(
            clientID, left_motor_handle, lSpeed, sim.simx_opmode_oneshot_wait)
    errorCode = sim.simxSetJointTargetVelocity(
            clientID, right_motor_handle, rSpeed, sim.simx_opmode_oneshot_wait)

    com = prediction_label
    if (com == 'q'):
        break
    elif (com == 'forward'):
        lSpeed = 0.3
        rSpeed = 0.3
    elif (com == 'left'):
        lSpeed = -0.15
        rSpeed = 0.3
    elif (com == 'right'):
        lSpeed = 0.3
        rSpeed = -0.15
    elif (com == 'backward'):
        lSpeed = -0.3
        rSpeed = -0.3
    elif (com == 'brake'):
        lSpeed = 0
        rSpeed = 0
    else:
        pass
cap.release()
cv2.destroyAllWindows()