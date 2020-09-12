from datetime import datetime
from ipaddress import IPv4Address
from pydantic import Json, UUID4


class ComputeNode:
    """
        The Compute Node is a physical machine with an hypervisor installed.
        It also contains the mikrostack_agent information
    """
    def __init__(self):
        self.id: int = 0  # 1
        self.uuid: UUID4 = UUID4()  # acc556c1-fe9f-4967-977c-efee0e7ea38c
        self.datetime_created: datetime = datetime.now()  # 2020-01-01 00:00:00
        self.datetime_modified: datetime = datetime.now()  # 2020-01-01 00:00:00
        self.datetime_deleted: datetime = datetime.now()  # None
        self.deleted: bool = False  # False
        self.name: str = ""  # h1
        self.fqdn: str = ""  # h1.home.lab
        self.ipaddress: IPv4Address = IPv4Address(address="10.0.0.10")  # 10.0.0.10
        self.stats: Json = Json()  # {'vpcu_total': 48, 'memory_total': 262144}
        self.meta: Json = Json()  # {}


class ComputeGroup:
    """
        The purpose of the Compute Group is to simulate a Host Aggregate in Openstack.
    """
    def __init__(self):
        self.id: int = 0  # 1
        self.uuid: UUID4 = UUID4()  # e2f4dfbc-0994-4db6-a5bf-e40a86a0890b
        self.datetime_created: datetime = datetime.now()  # 2020-01-01 00:00:00
        self.datetime_modified: datetime = datetime.now()  # 2020-01-01 00:00:00
        self.datetime_deleted: datetime = datetime.now()  # None
        self.deleted: bool = False  # False
        self.name: str = ""  # h1
        self.meta: Json = Json()  # {'availability_zone': 'az1'}
