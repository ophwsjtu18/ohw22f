from mcpi.minecraft import Minecraft
import serial
import serial.tools.list_ports
import time

ports = list(serial.tools.list_ports.comports())
print (ports)

for p in ports:
    print (p[1])
    if "SERIAL" in p[1] or "UART" in p[1]:
            #设置串口读取超时为1秒
	    ser=serial.Serial(port=p[0], timeout=1)
    else :
	    print ("No Arduino Device was found connected to the computer")
#ser=serial.Serial(port='COM4')
#ser=serial.Serial(port='/dev/ttymodem542')
#wait 2 seconds for arduino board restart
time.sleep(2)

mc=Minecraft.create()
#mc=Minecraft.create("10.163.80.195",4711)

stayed_time=0

while True:
    print("stay_time"+str(stayed_time))
    time.sleep(0.5)
    pos=mc.player.getTilePos()
    mc.postToChat("please goto home x=-30 y=-6 z=-40 for 15s to fly")
    mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
    #检测四周的9块区域是否有亮的红石灯
    for x in range(3):
        for z in range(3):
           if mc.getBlock(pos.x-1+x,pos.y,pos.z-1+z)==124:
               print("red stone ligh found")
               ser.write("y".encode())
    #读串口一行，查看串口输入是ON还是OFF
    resp=ser.readline()
    rs=str(resp)
    if "ON" in rs:
        print("got ON")
        #外接的开关打开的话，脚下出现玻璃
        mc.setBlock(pos.x,pos.y-1,pos.z,20)
    if "OFF" in rs:
        print("got OFF")
            
    if pos.x==-30 and pos.y==-6 and pos.z==-40:
        mc.postToChat("welcome home")
        stayed_time=stayed_time+1
        #回到家给串口送一个y，arduino收到串口点亮一盏led
        ser.write("y".encode())
        print("y send")
        time.sleep(1)
        if stayed_time>=30:
            mc.player.setTilePos(-30,10,-40)
            stayed_time=0
            #回到家给串口送一个g，arduino收到串口点亮另一盏led
            ser.write("g".encode())
            print("g send")
            time.sleep(1)
    else:
        stayed_time=0
        
     
