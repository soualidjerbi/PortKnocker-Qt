import pytest
from classes.FileLoader import FileLoader

@pytest.fixture
def file_loader():
    return FileLoader('test_config.json')

def test_file_loader_loads_file(file_loader):
    config_data = file_loader.loadFileData()
    assert isinstance(config_data, dict)

def test_file_loader_handles_missing_file(file_loader):
    file_loader.fileName = 'non_existent_file.json'
    with pytest.raises(FileNotFoundError):
        file_loader.loadFileData()