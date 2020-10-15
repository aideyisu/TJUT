# encoding: utf-8

import os
import sys
import time
import socket
import struct
import select
import argparse

ICMP_ECHO_REQUEST = 8  # Platform specific
DEFAULT_TIMEOUT = 2
DEFAULT_COUNT = 4


class Pinger(object):
    """ Pings to a host -- the Pythonic way"""

    def __init__(self, target_host, count=DEFAULT_COUNT, timeout=DEFAULT_TIMEOUT):
        """ 初始化 """
        self.target_host = target_host
        self.count = count
        self.timeout = timeout

    def do_checksum(self, source_string):
        """  Verify the packet integritity """
        sum = 0
        max_count = (len(source_string)/2)*2
        count = 0
        while count < max_count:

            val = source_string[count + 1]*256 + source_string[count]
            sum = sum + val
            sum = sum & 0xffffffff
            count = count + 2

        if max_count < len(source_string):
            sum = sum + ord(source_string[len(source_string) - 1])
            sum = sum & 0xffffffff

        sum = (sum >> 16) + (sum & 0xffff)
        sum = sum + (sum >> 16)
        answer = ~sum
        answer = answer & 0xffff
        answer = answer >> 8 | (answer << 8 & 0xff00)
        return answer

    def receive_pong(self, sock, ID, timeout):
        """
        Receive ping from the socket.
        """
        time_remaining = timeout
        while True:
            start_time = time.time()
            readable = select.select([sock], [], [], time_remaining)
            time_spent = (time.time() - start_time)
            if readable[0] == []:  # Timeout
                return

            time_received = time.time()
            recv_packet, addr = sock.recvfrom(1024)
            icmp_header = recv_packet[20:28]
            type, code, checksum, packet_ID, sequence = struct.unpack(
                "bbHHh", icmp_header
            )
            if packet_ID == ID:
                bytes_In_double = struct.calcsize("d")
                time_sent = struct.unpack(
                    "d", recv_packet[28:28 + bytes_In_double])[0]
                return time_received - time_sent

            time_remaining = time_remaining - time_spent
            if time_remaining <= 0:
                return

    def send_ping(self, sock,  ID):
        """
        Send ping to the target host
        """
        target_addr = socket.gethostbyname(self.target_host)

        my_checksum = 0

        # Create a dummy heder with a 0 checksum.
        header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, my_checksum, ID, 1)
        bytes_In_double = struct.calcsize("d")
        data = (192 - bytes_In_double) * "Q"
        data = struct.pack("d", time.time()) + bytes(data.encode('utf-8'))

        # Get the checksum on the data and the dummy header.
        my_checksum = self.do_checksum(header + data)
        header = struct.pack(
            "bbHHh", ICMP_ECHO_REQUEST, 0, socket.htons(my_checksum), ID, 1
        )
        packet = header + data
        sock.sendto(packet, (target_addr, 1))

    def ping_once(self):
        """
        Returns the delay (in seconds) or none on timeout.
        """
        msg = ""
        icmp = socket.getprotobyname("icmp")
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)
        except socket.error as e:
            if e.errno == 1:
                # Not superuser, so operation not permitted
                msg += "ICMP messages can only be sent from root user processes"
                raise socket.error(msg)
        except Exception as e:
            print("Exception: %s" % (e))

        my_ID = os.getpid() & 0xFFFF

        self.send_ping(sock, my_ID)
        delay = self.receive_pong(sock, my_ID, self.timeout)
        sock.close()
        return delay

    def ping(self):
        """
        Run the ping process
        """
        for i in range(self.count):
            print("Ping to %s..." % self.target_host,)
            try:
                delay = self.ping_once()
            except socket.gaierror as e:
                print("Ping failed. (socket error: '%s')" % e[1])
                break

            if delay == None:
                print("Ping failed. (timeout within %ssec.)" % self.timeout)
            else:
                delay = delay * 1000
                print("Get pong in %0.4fms" % delay)


def main():
    # Output command line args to screen
    if args.verbose:
        printmsg("Arguments used:")
        print (args)

    starttime = time.time()
    # Start Scanning
    results = {}
    for target in targets:
        results[target] = portscan(target, ports, args.tcpscan, args.udpscan, args.verbose)
    printmsg(("Total scantime %.2f seconds") % (time.time() - starttime))

    for target in results:
        print ("%s TCP:%s  UDP:%s" % (target, results[target][0], results[target][1]))
    return results


def portscan(target, ports, tcp, udp, verbose):
    # target=IPaddr,ports=list of ports,tcp=true/false,udp=true/false,verbose=true/false
    tcpports = []
    udpports = []
    if verbose:
        targetstarttime = time.time()
    if tcp:
        for portnum in ports:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.02)
                s.connect((target, portnum))
            except Exception:
                failvar = 0
                if verbose:
                    print ("%d/tcp \tclosed" % portnum)
            else:
                if verbose:
                    print ("%d/tcp \topen" % portnum)
                tcpports.append(portnum)
            finally:
                s.close()
    if udp:
        for portnum in ports:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                result = s.connect_ex((target, portnum))
                if result == 0:
                    socket.getservbyport(portnum)
                    if verbose:
                        print( "%d/udp \topen" % portnum)
                    udpports.append(portnum)
                else:
                    if verbose:
                        print ("%d/udp \tclosed" % portnum)
            except:
                if verbose:
                    print ("%d/udp \tclosed" % portnum)
            finally:
                s.close()

    if verbose:
        printmsg(("Scanned %s in %.2f seconds - Open: %iTCP, %iUDP" % \
                          (target, time.time() - targetstarttime, len(tcpports), len(udpports))))
    return tcpports, udpports


def errormsg(msg):
    print ("[!] Error: %s" % msg)
    sys.exit(1)


def printmsg(msg):
    print ("[+] nmap.py: %s" % msg)


def iprange(addressrange):  # converts a ip range into a list
    ip_list = []
    first3octets = '.'.join(addressrange.split('-')[0].split('.')[:3]) + '.'
    for i in range(int(addressrange.split('-')[0].split('.')[3]), int(addressrange.split('-')[1]) + 1):
        ip_list.append(first3octets + str(i))
    return ip_list


def ip2bin(ip):
    b = ""
    inQuads = ip.split(".")
    outQuads = 4
    for q in inQuads:
        if q != "":
            b += dec2bin(int(q), 8)
            outQuads -= 1
    while outQuads > 0:
        b += "00000000"
        outQuads -= 1
    return b


def dec2bin(n, d=None):
    s = ""
    while n > 0:
        if n & 1:
            s = "1" + s
        else:
            s = "0" + s
        n >>= 1
    if d is not None:
        while len(s) < d:
            s = "0" + s
    if s == "":
        s = "0"
    return s


def bin2ip(b):
    ip = ""
    for i in range(0, len(b), 8):
        ip += str(int(b[i:i + 8], 2)) + "."
    return ip[:-1]


def returnCIDR(c):
    parts = c.split("/")
    baseIP = ip2bin(parts[0])
    subnet = int(parts[1])
    ips = []
    if subnet == 32:
        return bin2ip(baseIP)
    else:
        ipPrefix = baseIP[:-(32 - subnet)]
        for i in range(2 ** (32 - subnet)):
            ips.append(bin2ip(ipPrefix + dec2bin(i, (32 - subnet))))
        return ips


if __name__ == '__main__':
    # test
    # print portscan('8.8.8.8', range(1, 100), True, True, True)
    # exit()
    parser = argparse.ArgumentParser(description='scan.py - Replicates limited nmap functionality and ping in python')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable this for full output')
    parser.add_argument('-sS', '--tcpscan', action='store_true', help='Enable this for TCP scans')
    parser.add_argument('-sU', '--udpscan', action='store_true', help='Enable this for UDP scans')
    parser.add_argument('-p', '--ports', default='1-1024', help='The ports you want to scan (21,22,80,135-139,443,445)')
    parser.add_argument('-IP',"--host", action="store",
                        help=u'Enable this for PingIP')
    parser.add_argument('-t', '--targets', help='The target(s) you want to scan (192.168.0.1)')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    args = parser.parse_args()
    print (args)

    # Set target (and convert for FQDN)
    targets = []
    if args.host:
        pinger = Pinger(target_host=args.host)
        pinger.ping()
    elif args.targets:
        if '/' in args.targets:  # found cidr target
            targets = returnCIDR(args.targets)
        elif '-' in args.targets:
            targets = iprange(args.targets)
        else:
            try:
                targets.append(socket.gethostbyname(args.targets))  # get IP from FQDN
            except:
                errormsg("Failed to translate hostname to IP address")
    else:
        parser.print_help()
        errormsg("You need to set a hostname")

    # Set ports
    if args.ports == '-':
        args.ports = '1-65535'
    ranges = (x.split("-") for x in args.ports.split(","))
    ports = [i for r in ranges for i in range(int(r[0]), int(r[-1]) + 1)]

    main()
