import serial

ser=serial.Serial("/dev/ttys008")


while True:
    a=input("pleas type your cmd here,q for quit, ~ for remote quit :")
    print(a)
    if a == 'q':
        break
    ser.write(a.encode())

