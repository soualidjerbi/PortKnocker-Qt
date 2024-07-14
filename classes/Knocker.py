import socket, time, select
from classes.Resolver import Resolver
from classes.FileLoader import FileLoader
from classes.Host import Host

class KnockerConfigurationLoader:
	def __init__(self, config_file, logger=None):
		self.logger = logger
		self.fileLoader = FileLoader(config_file, self.logger)
		
	def load(self):
		self.logger.debug('------Load Config-------')
		self.config = self.fileLoader.loadFileData()
		allConfs = []
		for config in self.config['configurations']:
			tempconfig = Host()
			tempconfig = tempconfig.createHost(config)
			allConfs.append(tempconfig)
			tempconfig = None
		return allConfs, self.config['last_used']
	
	def save(self, config, index) -> None:
		allConfs = [
			configuration.hostConfiguration for configuration in config
		]
		json_config = {
			"configurations": allConfs,
			"last_used": index
		}
		self.fileLoader.saveDataToFile(json_config)

class PortKnocker:
	def __init__(self,logger=None):
		self.logger = logger
		self.delay = 0.3
		self.configurationLoader = KnockerConfigurationLoader('Knocker.json', self.logger)
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
			









