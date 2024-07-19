import socket, time, select
from classes.Resolver import Resolver
from classes.FileLoader import FileLoader
from classes.Host import Host
from dataclasses import dataclass, field

@dataclass
class KnockerConfigurationLoader:
	logger : dict = field(default_factory=dict)
	fileLoader : dict = None
	knockerConfigFileName : str = field(default='Knocker.json')
		
	def load(self) -> dict:
		self.logger.debug('------Load Config-------')
		config = FileLoader.loadFileData(self.knockerConfigFileName)
		allConfs = []
		for conf in config['configurations']:
			tempconfig = Host()
			tempconfig = tempconfig.createHost(conf)
			allConfs.append(tempconfig)
			tempconfig = None
		return allConfs, config['last_used']
	
	def save(self, config, index) -> None:
		allConfs = [
			configuration.hostConfiguration for configuration in config
		]
		json_config = {
			"configurations": allConfs,
			"last_used": index
		}
		FileLoader.saveDictToFile(self.knockerConfigFileName, json_config)
@dataclass
class PortKnocker:
	logger : dict = field(default_factory=dict)
	delay  : float = 0.3
	configurationLoader : dict = field(default_factory=dict)
 
	def __post_init__(self):
		self.configurationLoader = KnockerConfigurationLoader(self.logger)
  
	def configure(self, host):
		self.host = host
		self.ipAddress = self.getIpFromName()
	def knock_in(self):
		self.knock(1)
	def knock_out(self):
		self.knock(0)
	def knock(self, action):
		ports_list = self.host.ports_in if action == 1 else self.host.ports_out
		for i, ( port , proto ) in enumerate(ports_list):
			if port != '':
				use_udp = proto == 'udp'
				last_index = len(ports_list) - 1
				port = int(port)
				self.sendPackets(port, use_udp)
				if self.delay and i != last_index:
					time.sleep(self.delay)

	def getIpFromName(self):
		resolver = Resolver(self.logger)
		return resolver.getDnsData(self.host.ip_address)[0]

	def sendPackets(self, port, use_udp):
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if use_udp else socket.SOCK_STREAM)
		s.setblocking(False)
		socket_address = (self.ipAddress, port)
		if use_udp:
			s.sendto(b'', socket_address)
		else:
			s.connect_ex(socket_address)
		self.logger.debug(f'Hitting {socket_address}')
		select.select([s], [s], [s], self.delay)
		s.close()
			









