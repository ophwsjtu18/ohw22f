# 安装python3 版本
www.python.org 选python3.9版本  

# 安装jdk
jdk-16.02-windows-x64.exe

# 安装mcpi
打开 cmd  或powershell     /  mac和linux打开一个终端terminal  
pip install mcpi  

# 验证安装
## java
打开cmd, 运行java -version 可以看到java verson 16.02 等 
## mcp
打开idle,   import mcpi 不报错

# 运行Bukkit服务器
在Bukkit目录中运行批处理  
start.bat  
如果是mac或linux，运行start.sh  
如果报错没有java，请设置你的java路径，或点击安装jdk安装包，或从网上下载安装.  下载好的mac或linux安装包在本目录下可找到。  

# 运行Minecraft客户端
## 方法1
点击启动器HMCL-3.3.188.jar
## 方法2
运行hmclstart.bat

## 添加用户，用你自己名字的首字母
## 选择1.17.1版本启动

## 选多人游戏模式
服务器地址 localhost  或者  127.0.0.1 

## 游戏基本命令
飞起为双击空格 降落为shift 使用物品右键 挖左键 WSAD前后左右 E选物品 1234用物品 F1出字符 F10全屏  
#  验证welcomehome
打开python3 的idle  
打开welcomehome.py  
F5运行  
回到我的世界  
四处走动坐标打印会变化，请根据提示回到家的坐标，停留15秒飞起9格。   

# 其它例程
## 多用户模式例程
welcomehome_multi.py

## 串口点亮arduino的led灯  
comled.py
运行前先打开cmd或powershell，安装pyserial  
pip install pyserial  
然后运行  

## 检查宝剑右键击打方块事件
welcomehome_checkhit.py  
## 串口与红石灯联动
welcomehome_led.py  
## 多用户在同一服务器里，用通天塔标识位置，用宝剑右键击打方块定位玩家
welcomehome_multiplayer.py  

## 其他参考代码
# CodeFiles  各种建造代码
# blockscopy 拷贝建筑到文件
# blockspast  粘贴文件到建筑
# comswitch  串口读ON OFF字符串
