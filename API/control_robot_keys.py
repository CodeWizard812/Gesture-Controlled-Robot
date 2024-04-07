import sim
from time import sleep as delay
import numpy as np
import cv2
import sys

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



try:
    while (1):
           
        errorCode = sim.simxSetJointTargetVelocity(
            clientID, left_motor_handle, lSpeed, sim.simx_opmode_oneshot_wait)
        errorCode = sim.simxSetJointTargetVelocity(
            clientID, right_motor_handle, rSpeed, sim.simx_opmode_oneshot_wait)

        com = input("Enter: ")
        if (com == 'q'):
            break
        elif (com == 'w'):
            lSpeed = 0.2
            rSpeed = 0.2
        elif (com == ord('a')):
            lSpeed = -0.1
            rSpeed = 0.2
        elif (com == ord('d')):
            lSpeed = 0.2
            rSpeed = -0.1
        elif (com == ord('s')):
            lSpeed = -0.2
            rSpeed = -0.2
        else:
            lSpeed = 0
            rSpeed = 0
        com = 'o'

    cv2.destroyAllWindows()
except:
    cv2.destroyAllWindows()