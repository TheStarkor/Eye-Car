import modi
import time

# Initialize MazeRunner, gets MODI class
# Add needed modules
def init_MR(bundle):
  print('modules list\n', bundle.modules)
  motor = bundle.motors[0]
  button = bundle.buttons[0]
  return len(bundle.modules), motor, button

# Checks module connection status by comparing module numbers.
def is_connected(curr_num):
  if curr_num != module_num:
    print('\n--------interrupt!!!---------')
    print('Some modules disconnected!!')
    return False
  else:
    return True

# MODI goes forward, gets delay, speed args
def forward(delay=10, speed=100):
  motor.speed(0, 0)
  time.sleep(0.001)
  print('Pressed! forward!!')
  for _ in range(delay):
    # print(ir.distance())
    time.sleep(0.001)
    motor.speed(-speed, speed)
    time.sleep(0.001)
  motor.speed(0, 0)

# MODI turns left, gets delay arg.
def left(delay=3):
  motor.speed(0, 0)
  time.sleep(0.001)
  print('left!!')
  for _ in range(delay):
    time.sleep(0.001)
    motor.speed(100, 100)
    time.sleep(0.001)
  motor.speed(0, 0)

# MODI turns right, gets delay arg.
def right(delay=3):
  motor.speed(0, 0)
  time.sleep(0.001)
  print('right!!')
  for _ in range(delay):
    time.sleep(0.001)
    motor.speed(-100, -100)
    time.sleep(0.001)
  motor.speed(0, 0)

# Init
bundle = modi.MODI()
time.sleep(1)
start = False
module_num, motor, button = init_MR(bundle)

# Start
while True:
  if button.clicked() == True:
    print('Start Maze Runner!!!')
    start = True

  if start:
    curr_num = len(bundle.modules)
    if is_connected(curr_num) == False: break
    print('ready:', curr_num)
    print('1: forward, 2: left, 3: right')
    n = input('Input commnad: ')
    if n == '1': forward()
    elif n == '2': left()
    elif n == '3': right()
    elif n == '0': 
      print('MazeRunner End!')
      break
    else: print('wrong input')
    print('end')
    time.sleep(0.01)
  else:
    print('Press the button to start!!')
    