import pytest
from unittest.mock import patch
from classes.Knocker import Knocker
from classes.FileLoader import FileLoader

@pytest.fixture
def knocker():
    return Knocker()

def test_knocker_attempts_to_connect(knocker):
    with patch.object(FileLoader, 'loadFileData') as mock_loadFileData:
        mock_loadFileData.return_value = {'host': 'example.com', 'port': 8080}
        knocker.attemptConnection()
        assert knocker.isConnected == False  # Replace with actual connection logic

def test_knocker_handles_connection_error(knocker):
    with patch.object(FileLoader, 'loadFileData') as mock_loadFileData:
        mock_loadFileData.return_value = {'host': 'example.com', 'port': 8080}
        with pytest.raises(ConnectionError):
            knocker.attemptConnection()  # Replace with actual connection logic

def test_knocker_handles_timeout_error(knocker):
    with patch.object(FileLoader, 'loadFileData') as mock_loadFileData:
        mock_loadFileData.return_value = {'host': 'example.com', 'port': 8080}
        with pytest.raises(TimeoutError):
            knocker.attemptConnection()  # Replace with actual connection logic