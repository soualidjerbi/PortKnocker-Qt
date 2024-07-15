import pytest
from classes.Resolver import Resolver
from unittest.mock import Mock

def test_getDnsData_valid_hostname():
    # Arrange
    logger = Mock()
    resolver = Resolver(logger)
    hostname = "example.com"
    expected_ipv4_addresses = ["192.0.2.1", "192.0.2.2"]  # Example IP addresses

    # Act
    ipv4_addresses = resolver.getDnsData(hostname)

    # Assert
    assert ipv4_addresses == expected_ipv4_addresses
    logger.debug.assert_not_called()

def test_getDnsData_invalid_hostname():
    # Arrange
    logger = Mock()
    resolver = Resolver(logger)
    hostname = "invalid.hostname"

    # Act
    ipv4_addresses = resolver.getDnsData(hostname)

    # Assert
    assert ipv4_addresses == []
    logger.debug.assert_called_once()