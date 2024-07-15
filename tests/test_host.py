import pytest
from classes.Host import Host

class TestHost:
    def test_create_host_initialization(self):
        parameters = {
            'name': 'TestHost',
            'ip_address': '192.168.1.1',
            'socket_port': '8080',
            'ports_in': [80, 443],
            'ports_out': [8080, 8443]
        }
        host = Host().createHost(parameters)
        assert host.name == 'TestHost'
        assert host.ip_address == '192.168.1.1'
        assert host.socket_port == '8080'
        assert host.ports_in == [80, 443]
        assert host.ports_out == [8080, 8443]

    def test_name_property(self):
        host = Host()
        host.name = 'TestHost'
        assert host.name == 'TestHost'

    def test_host_configuration_property(self):
        host = Host()
        host.name = 'TestHost'
        host.ip_address = '192.168.1.1'
        host.socket_port = '8080'
        host.ports_in = [80, 443]
        host.ports_out = [8080, 8443]
        expected_configuration = {
            "name": 'TestHost',
            "ip_address": '192.168.1.1',
            "socket_port": '8080',
            "ports_in": [80, 443],
            "ports_out": [8080, 8443]
        }
        assert host.hostConfiguration == expected_configuration