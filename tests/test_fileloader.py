import pytest
from classes.FileLoader import FileLoader
from classes.Logger import Logger

@pytest.fixture
def file_loader():
    """
    This function returns an instance of the FileLoader class, initialized with a specific JSON file name and a Logger instance.

    Parameters:
    None.

    Returns:
    file_loader (FileLoader): An instance of the FileLoader class, initialized with 'Knocker.json' as the file name and a Logger instance.
    """
    return FileLoader()

def test_file_loader_loads_file(file_loader):
    """
    This function tests if the FileLoader class can load a JSON file correctly.

    Parameters:
    file_loader (FileLoader): An instance of the FileLoader class, initialized with a valid JSON file name.

    Returns:
    None. This function asserts the type of the loaded data, which should be a dictionary.
    If the loaded data is not a dictionary, an AssertionError will be raised.
    """
    loaded_data = file_loader.loadFileData('Knocker.json')
    assert isinstance(loaded_data, dict)

def test_file_loader_handles_missing_file(file_loader):
    """
    This function tests if the FileLoader class can handle a missing JSON file.

    Parameters:
    file_loader (FileLoader): An instance of the FileLoader class, initialized with a non-existent JSON file name.

    Returns:
    None. This function asserts that the loadFileData method returns a ValueError when trying to load a non-existent file.
    If the loaded data is not a ValueError, an AssertionError will be raised.
    """
    error = FileLoader().getFilePath('none')
    assert isinstance(error, FileNotFoundError)