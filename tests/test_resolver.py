import pytest
from classes.Resolver import Resolver
from unittest.mock import Mock

def test_getDnsData_valid_hostname():
    # Arrange
    logger = Mock()
    resolver = Resolver(logger)
    hostname = "google.com"

    # Act
    ipv4_addresses = resolver.getDnsData(hostname)

    # Assert
    assert len(ipv4_addresses) >= 1
    logger.debug.assert_not_called()

def test_getDnsData_invalid_hostname():
    # Arrange
    logger = Mock()
    resolver = Resolver(logger)
    hostname = "invalid.hostname"

    # Act
    ipv4_addresses = resolver.getDnsData(hostname)

    # Assert
    assert ipv4_addresses is None
    logger.debug.assert_called_once()