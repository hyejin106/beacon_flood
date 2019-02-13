#!/usr/bin/python3
from scapy.all import *
import concurrent.futures

def sendBeacon(SSID):
    ssid = Dot11Elt(ID="SSID", info=SSID)
    frame = RadioTap()/dot11/dot11Beacon/ssid
    sendp(frame, iface="mon0", loop=1, count=1000)

dot11 = Dot11(type=0, subtype=8,
        addr1="ff:ff:ff:ff:ff:ff",
        addr2="00:01:02:03:04:05",
        addr3="00:01:02:03:04:05")
dot11Beacon = Dot11Beacon(cap="ESS", timestamp=1)

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as e:
	e.submit(sendBeacon, 'aaaaaaaaaaa')
	e.submit(sendBeacon, 'bbbbbbbbbbb')
	e.submit(sendBeacon, 'ccccccccccc')
	e.submit(sendBeacon, 'ddddddddddd')
	e.submit(sendBeacon, 'eeeeeeeeeee')

