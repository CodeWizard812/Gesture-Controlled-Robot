# Gesture-Controlled-Robot
This is a two-wheel vehicle which is being controlled by gesture given on camera using Machine Learning and Computer Vision.

Initailly, dataset is created by collectdata.py and stored in GestureImage48x48 followed by splitting data in 80:20 ratio by split.py and stored in split_dataset_48x48 in train and val folder respectively.

Using, Google Colab(training_model.ipynb) model was trained and Gesture_Detection_48x48.json and Gesture_Detection_Model48x48.h5(In API folder) was created.

Robot design was created on CoppeliaSim -> Robot.ttt

In folder API, all API's required for CoppeliaSim to manage with VS code was copied from C:\Program Files\CoppeliaRobotics\CoppeliaSimEdu\programming\legacyRemoteApi\remoteApiBindings\python\python
&
for remoteApi.dll C:\Program Files\CoppeliaRobotics\CoppeliaSimEdu\programming\legacyRemoteApi\remoteApiBindings\lib\lib\Windows.

In API folder:

Keep CoppeliaSim's Robot.ttt file in Simulation Mode before running below program files
1. test_connection.py is to establish connection between VS code Keep CoppeliaSim in Simulation Mode before running test_connection.py

2. control_robot.py was created to check the robot working or not.

3. control_robot_keys.py is the code to control the robot.

4. real_time_detection.py is the final folder which will predict the gesture and controls the robot

Make sure to open only and only API folder while running the program on VS code, else Gesture_Detection_Model48x48.h5 will not open.

