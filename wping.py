#!/usr/bin/env python
import socket
import time
import sys
from colorama import Fore

g = Fore.GREEN
w = Fore.WHITE
ly = Fore.LIGHTYELLOW_EX
c = Fore.CYAN
lb = Fore.LIGHTBLUE_EX
lr = Fore.LIGHTRED_EX

def ping(ip, port):
    start_time = time.time()
    try:
        with socket.create_connection((ip, port), timeout=2):
            end_time = time.time()
            elapsed = (end_time - start_time) * 1000
            return True, elapsed
    except (socket.timeout, socket.error):
        return False, None

def ping_main(ip, port):
    print(f"{w}Pinging {ly}{ip} {w}on {ly}{port}")
    while True:
        reachable, elapsed = ping(ip, port)
        if reachable:
            print(f"{g}IP={ip} {w}||{c} Port={port} {w}||{lb} Latency={elapsed:.2f}ms")
            time.sleep(0.1)
        else:
            print(f"{lr}IP={ip} {w}|| {lr}Port={port} {w}|| {lr}Connection Timed Out")
            time.sleep(0.1)
def main():
    if len(sys.argv) != 3:
        print(f"Usage: wping <ip> <port>")
        sys.exit(1)

    ip = sys.argv[1]
    try:
        port = int(sys.argv[2])
    except ValueError:
        print("Port is written in numbers, not text!")
        sys.exit(1)

    ping_main(ip, port)

if __name__ == "__main__":
    main()
