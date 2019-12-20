# Eye-Car
Eye-car is a self-driving car project that recognizes the center of the lane without direct maneuvering while driving and recognizes and adjusts the speed when a human handwriting speed signal is read.

## Documents
### [Eye-Car Final Report (한국어)](https://docs.google.com/document/d/17igFHHZcF7QzcSuRyHR54PTvwCapKHJ5tV0HvqecKbo/edit?usp=sharing)

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