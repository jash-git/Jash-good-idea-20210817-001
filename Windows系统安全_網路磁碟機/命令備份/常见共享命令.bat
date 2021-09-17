#常见共享命令
net use                               #查看本机建立的连接(本机连接其他机器)
net session                           #查看本机建立的连接(其他机器连接的本机)，需要administrator用户执行
net share                             #查看本地开启的共享
net share ipc$                        #开启ipc$共享
net share ipc$ /del                   #删除ipc$共享
net share admin$ /del                 #删除admin$共享
net share c$ /del                     #删除C盘共享
net share d$ /del                     #删除D盘共享
net use * /del                        #删除所有连接

net use \\192.168.10.15                   #与192.168.10.15建立ipc空连接
net use \\192.168.10.15\ipc$              #与192.168.10.15建立ipc空连接
net use \\192.168.10.15\ipc$ /u:"" ""     #与192.168.10.15建立ipc空连接

net view \\192.168.10.15                  #查看远程主机开启的默认共享

net use \\192.168.10.15 /u:"administrator" "root"   #以administrator身份与192.168.10.15建立ipc连接
net use \\192.168.10.15 /del              #删除建立的ipc连接

net time \\192.168.10.15                  #查看该主机上的时间

net use \\192.168.10.15\c$  /u:"administrator" "root"  #建立C盘共享
dir \\192.168.10.15\c$                  #查看192.168.10.15C盘文件
dir \\192.168.10.15\c$\user             #查看192.168.10.15C盘文件下的user目录
dir \\192.168.10.15\c$\user\test.exe    #查看192.168.10.15C盘文件下的user目录下的test.exe文件
net use \\192.168.10.15\c$  /del        #删除该C盘共享连接

net use k: \\192.168.10.15\c$  /u:"administrator" "root"  #将目标C盘映射到本地K盘
net use k: /del                                           #删除该映射