import serial

ser=serial.Serial("/dev/ttys009",timeout=1)

while True:
    print("reading....")
    resp=ser.readline()
    if resp != b"":
        a=resp.decode()
        print(a)
        print("get commnd, I will handle it",resp)
        b=a.strip()
        if b == '~':
            break
        c=b.split(",")
        d=list(map(int,c))
        servo1=d[0]
        servo2=d[1]
        servo3=d[2]
        print("move servo to angle",servo1,servo2,servo3)
    else:
        print("working on something else..")
    
