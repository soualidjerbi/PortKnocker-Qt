class Host:
    def __init__(self):
        self._name : str = None
        self._ip_address : str = None
        self._socket_port : str = None
        self._ports_in : list = []
        self._ports_out : list = []
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value):
        self._ip_address = value

    @property
    def socket_port(self):
        return self._socket_port

    @socket_port.setter
    def socket_port(self, value):
        self._socket_port = value

    @property
    def ports_in(self):
        return self._ports_in

    @ports_in.setter
    def ports_in(self, value):
        self._ports_in = value

    @property
    def ports_out(self):
        return self._ports_out

    @ports_out.setter
    def ports_out(self, value):
        self._ports_out = value
    
    @property
    def hostConfiguration(self):
        return {
            "name": self.name,
            "ip_address": self.ip_address,
            "socket_port": self.socket_port,
            "ports_in": self.ports_in,
            "ports_out": self.ports_out
        }
    def createHost(self, parameters): 
        host = Host()
        host.name = parameters['name']
        host.ip_address = parameters['ip_address']
        host.socket_port = parameters['socket_port']
        host.ports_in = parameters['ports_in']
        host.ports_out = parameters['ports_out'] 
        return host