# Eye-Car
Eye-car는 주행 중 사람의 직접적인 조종없이 차선의 중앙을 인식하여 운행하며, 인간의 손글씨 속도 신호를 읽게 되었을 경우 이를 인식하고 속도를 조절하는 기능을 갖춘 자율주행 자동차 프로젝트다.

## Documents
### [Eye-Car Final Report](https://docs.google.com/document/d/1Pd1ApwdkshFOSEoRoL0Al_gcqtSfRtKXIdYn5p_j0cE/edit?usp=sharing)

### Demo
![Demo](https://user-images.githubusercontent.com/45455072/71264599-c754c500-2387-11ea-87bd-64846ea6d787.gif)

### Lane Detection
![LaneDetection](https://user-images.githubusercontent.com/45455072/71264729-0f73e780-2388-11ea-8522-8014d6b1c63c.PNG)
### Number Recognition
![NumberRecognition](https://user-images.githubusercontent.com/45455072/71264769-20245d80-2388-11ea-85fa-8edde4e8e3dd.PNG)

## Members
### Team 8
- KAIST 17 Seungho Baek
- KAIST 18 Juyeon Kim
- KAIST 19 ABHIJEET SHARMA  

Thx to prof. Sungho Jo, TA. Jungwook Mun, Daekyum Kim


## Directory
```
MazeRunner
└─ src                          (All needed files, Codes, Tests, imgs, models)
    ├─ Study                    (Basic functions we needed)
    ├─ epic_num_reader*.model   (CNN model for number prediction)
    ├─ img                      (Test image sets)
    ├─ tests                    (Files for testing)
    ├─ video                    (Test video sets)
    └─ EyeCar.py                (Main program)
```

## Table of Contents
1. [Getting Started](#getting-started)
2. [Features](#features)

---

## Getting Started
- `src/EyeCar.py`, `src/epic_num_reader.model` required to get started

### Clone
- Clone this repo to your local machine using `https://github.com/TheStarkor/MazeRunner.git`

### Prerequisites
#### Hardware
```
MODI
Raspberry Pi
```
#### Software
```
Rasbian Buster (2019-09-26 Released)
pyMODI
OpenCV
Tensorflow ver.1
All modules required for tensorflow
```

### Testing
For checking the module connection, we provide test files in the `src/tests` directory
1. `PiCamera/camera_test.py`, `PiCamera/cap.py` for checking Raspberry Pi Camera.

2. `ModiTest.py` for checking Modi connection and modules working

3. `LaneTest.py` for lane detection function

4. `NumberTest.py` for number detction and number prediction

5. *(Additional)* `firebaseTest.py` for firebase and firestore connection

### Running
```
$ python EyeCar.py
$ python3 EyeCar.py (If there is python2)
```