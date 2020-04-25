#!/usr/bin/env python2
# -*- coding:utf-8 -*-

from scapy.all import *

dst_ip = "8.8.8.8"
src_port = RandShort()
dst_port = 80

tcp_fin_scan = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port, flags='F'), timeout=10)

# 判断是否收到应答包
if type(tcp_fin_scan) == type(None):
    print ("[+] Port is open|filtered.")
# 判断收到的应答包是否具有TCP层
elif tcp_fin_scan.haslayer(TCP):
    # 判断是否为RST数据包
    if tcp_fin_scan.getlayer(TCP).flags == 0x14:
        print ("[-] Port is closed.")
# 判断数据包是否具有ICMP层
elif tcp_xmas_scan.haslayer(ICMP):
    # 判断是否被防火墙过滤
    if tcp_fin_scan.getlayer(TCP).type == 3 and tcp_fin_scan.getlayer(TCP).code in [1, 2, 3, 9, 10, 13]:
        print ("[-] Filtered.")
