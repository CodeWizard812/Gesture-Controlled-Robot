import cv2
import os


directory= 'GestureImage48x48/'
print(os.getcwd())

if not os.path.exists(directory):
    os.mkdir(directory)
for subdir in ['null', 'forward', 'backward', 'left', 'right', 'brake']:
    if not os.path.exists(os.path.join(directory, subdir)):
        os.mkdir(os.path.join(directory, subdir))


cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    count = {
             'w': len(os.listdir(directory+"/forward")),
             's': len(os.listdir(directory+"/backward")),
             'a': len(os.listdir(directory+"/left")),
             'd': len(os.listdir(directory+"/right")),
             'e': len(os.listdir(directory+"/brake")),
             'null': len(os.listdir(directory+"/null"))
             }

    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,300),(255,255,255),2)
    cv2.imshow("data",frame)
    frame=frame[40:300,0:300]
    cv2.imshow("ROI",frame)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    frame = cv2.resize(frame,(48,48))
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == ord('w'):
        cv2.imwrite(os.path.join(directory+'forward/'+str(count['w']))+'.jpg',frame)
    elif interrupt & 0xFF == ord('s'):
        cv2.imwrite(os.path.join(directory+'backward/'+str(count['s']))+'.jpg',frame)
    elif interrupt & 0xFF == ord('a'):
        cv2.imwrite(os.path.join(directory+'left/'+str(count['a']))+'.jpg',frame)
    elif interrupt & 0xFF == ord('d'):
        cv2.imwrite(os.path.join(directory+'right/'+str(count['d']))+'.jpg',frame)
    elif interrupt & 0xFF == ord('e'):
        cv2.imwrite(os.path.join(directory+'brake/'+str(count['e']))+'.jpg',frame)
    elif interrupt & 0xFF == ord('.'):
        cv2.imwrite(os.path.join(directory+'null/' + str(count['null']))+ '.jpg',frame)

    if interrupt & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    