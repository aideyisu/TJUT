#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from scapy.all import *

dst_ip = "114.114.114.114"
src_port = RandShort()
dst_port = 80

tcp_ack_scan = sr1(IP(dst=dst_ip)/TCP(sport=src_port,
                                      dport=dst_port, flags='A'), timeout=10)

# 判断是否收到应答包
if type(tcp_ack_scan) == type(None):
    print ("[-] Filtered.")
# 判断收到的应答包是否具有TCP层
elif tcp_ack_scan.haslayer(TCP):
    # 判断是否为RST数据包
    if tcp_ack_scan.getlayer(TCP).flags == 0x14:
        print ("[+] Unfiltered.")
# 判断数据包是否具有ICMP层
elif tcp_ack_scan.haslayer(ICMP):
    # 判断是否被防火墙过滤
    if tcp_ack_scan.getlayer(TCP).type == 3 and tcp_ack_scan.getlayer(TCP).code in [1, 2, 3, 9, 10, 13]:
        print ("[-] Filtered.")
