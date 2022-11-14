<!--
 * @Author: linin00
 * @Date: 2022-11-14 21:48:46
 * @LastEditTime: 2022-11-14 21:49:58
 * @LastEditors: linin00
 * @Description: 
 * @FilePath: /lj/11.14/task3/README.md
 * 
-->
实践中发现利用serial来控制会卡死在读串口的过程中，原因是serial的写入速度太快，导致一行永远都读不完