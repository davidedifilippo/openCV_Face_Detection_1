import serial

ArduinoSerial = serial.Serial('com11',9600,timeout=0.1)


x = 0
y = 0

while True:
    if x<640:
        x = x+1
    else:
        x = 0
    if y < 400:
        y = y+1
    else:
        y = 0
    string = 'X{0:d}Y{1:d}'.format(x,y)
    print(string)
    ArduinoSerial.write(string.encode('utf-8'))