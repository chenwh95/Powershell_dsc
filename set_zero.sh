#!/bin/bash

source ~/.bash_profile

# this script is used to flush iptable monitors and clear flow.txt file.

iptables -Z

Clean_time=` date "+%Y-%m-%d %H:%M:%S" `

echo "File was set to zero at ${Clean_time} " > /root/shadowsocks_monitor/flow.txt
