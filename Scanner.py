#!/usr/bin/python3

from re import I
import nmap

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmpa automation tool")

print("<------------------------------------------------------------------->")

# Ask user data on console
ip_addr = input("Please enter the IP address you want to scan: ")
print(" The IP you entered is: ",ip_addr)
type(ip_addr)

resp = input(""" \nPlease enter the type of scan you want to run 
                   1) SYN ACK Scan
                   2) UDP Scan
                   3) Comprehensive Scan\n""")

print("You have selected option: ", resp)

if resp == '1':
    print("Nmap version: ",scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Ip status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == "2":
    print("Nmap version: ",scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Ip status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['udp'].keys())
elif resp == "3":
    print("Nmap version: ",scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['tcp'].keys())
else:
    print("Dont be a dick")