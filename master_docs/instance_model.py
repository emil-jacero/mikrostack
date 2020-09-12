from datetime import datetime
from ipaddress import IPv4Address, IPv4Network
from pydantic import Json, UUID4


class Instance:
    """
        This class describes what information and type is needed to construct this object.
    """
    name: str = ""  # test-instance-1
    cpu: int = 0  # 4
    memory: int = 0  # 2048 (MB)
    root_disk_size: int = 0  # 20480 (MB)
    network: IPv4Network = IPv4Network(address="192.168.0.1/24")  # 192.168.0.1/24
    ip_address: IPv4Address = IPv4Address(address="192.168.0.10")  # 192.168.0.10
