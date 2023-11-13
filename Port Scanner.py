import socket
import ipaddress
from typing import Dict

class PortScanner:
    def scan(self, ip: str, udp: bool, from_port: int, to_port: int) -> Dict[int, bool]:
        try:
            ipaddress.IPv4Address(ip)
        except ipaddress.AddressValueError:
            return {}  # Invalid IP address format

        if from_port > to_port or from_port < 0 or to_port < 0:
            return {}  # Invalid port range

        result = {}
        protocol = socket.SOCK_DGRAM if udp else socket.SOCK_STREAM

        for port in range(from_port, to_port + 1):
            try:
                with socket.socket(socket.AF_INET, protocol) as sock:
                    sock.settimeout(1)  # Set a timeout of 1 second
                    if sock.connect_ex((ip, port)) == 0:
                        result[port] = True  # Port is open
                    else:
                        result[port] = False  # Port is closed
            except socket.error:
                result[port] = False  # Error occurred while scanning the port

        return result
