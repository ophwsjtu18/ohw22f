<!--
 * @Author: linin00
 * @Date: 2022-11-14 19:31:12
 * @LastEditTime: 2022-11-14 19:32:13
 * @LastEditors: linin00
 * @Description: 
 * @FilePath: /lj/11.14/README.md
 * 
-->
mac 可以使用 `socat`工具来创建虚拟串口
先安装
```bash
brew install socat
```

```bash
socat -d -d pty,raw,echo=0 pty,raw,echo=0
```
创建好的虚拟串口对会在命令行中显示