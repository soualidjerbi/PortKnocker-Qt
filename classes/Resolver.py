import socket

class Resolver():
	def __init__(self, logger):
		self.logger = logger
	
	def getDnsData(self,hostname):
		ipv4_addresses = []
		try:
			results = socket.getaddrinfo(hostname, None, socket.AF_UNSPEC)
			for result in results:
				family, _, _, _, sockaddr = result
				if family == socket.AF_INET:
					address = sockaddr[0]
					ipv4_addresses.append(address)
			return ipv4_addresses
		except socket.gaierror as error:
			self.logger.debug(f"Error: Unable to resolve '{hostname}': {error}")