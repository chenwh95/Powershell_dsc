#!/bin/bash

source /etc/profile


echo "************************************************************" >> /root/shadowsocks_monitor/flow.txt
date "+%Y-%m-%d %H:%M:%S" >> /root/shadowsocks_monitor/flow.txt

#get all configured shadowsocks ports and add iptables monitor

#ss -lntp | grep ssserver | awk -F [*:] '{print $3}'

#get port count
count=`ss -lntp | grep ssserver | awk -F [*:] '{print $3}' | wc -l `

#automatically create monitor rules in iptables,if already existed , then passs.
 for ((i=1;i< 1+$count;i++))
 do
 Port_num=` ss -lntp | grep ssserver | awk -F [*:] '{print $3}' | awk '{print $1}' | sed -n ${i}p `

Return_String=`iptables -L OUTPUT -v -n | grep $Port_num`

if [ -z "$Return_String" ]
then

 iptables -I OUTPUT -p tcp --sport $Port_num
 iptables -I OUTPUT -p udp --sport $Port_num
fi

#get port usage and determine the limit

Port_usage1=`iptables -L -n -v -x | grep spt:$Port_num | grep tcp | awk '{print $2}' `
Port_usage2=`iptables -L -n -v -x | grep spt:$Port_num | grep udp | awk '{print $2}' `
Port_usageall=` expr \( $Port_usage1 + $Port_usage2 \) / 1000000  `

echo -e " Port:${Port_num} have used: ${Port_usageall} MB " >> /root/shadowsocks_monitor/flow.txt

#then to decide if the  total usage  is over the limit.

Max=20480

if [ $Port_usageall -gt $Max ] ; then

iptables -D INPUT -p tcp --dport $Port_num -j ACCEPT
iptables -D INPUT -p udp --dport $Port_num -j ACCEPT

fi

done




