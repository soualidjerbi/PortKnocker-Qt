from dataclasses import dataclass, field

@dataclass(slots=True)
class Host:
    name : str = None
    ip_address : str = None
    socket_port : str = None
    ports_in : list = field(default_factory=list)
    ports_out : list = field(default_factory=list)
    
    @property
    def hostConfiguration(self) -> dict:
        return {
            "name": self.name,
            "ip_address": self.ip_address,
            "socket_port": self.socket_port,
            "ports_in": self.ports_in,
            "ports_out": self.ports_out
        }
    def createHost(self, parameters) -> 'Host' : 
        host = Host()
        host.name = parameters['name']
        host.ip_address = parameters['ip_address']
        host.socket_port = parameters['socket_port']
        host.ports_in = parameters['ports_in']
        host.ports_out = parameters['ports_out'] 
        return host