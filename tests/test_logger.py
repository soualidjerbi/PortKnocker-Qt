import pytest
import logging
from unittest.mock import patch
from classes.Logger import Logger
from classes.FileLoader import FileLoader

@pytest.fixture
def logger():
    return Logger()

def test_logger_with_empty_config(logger):
    with patch.object(FileLoader, 'loadFileData') as mock_loadFileData:
        mock_loadFileData.return_value = {}
        logger.debug('Test debug message')
        logger.info('Test info message')
        logger.warning('Test warning message')
        logger.error('Test error message')
        logger.critical('Test critical message')
        assert len(logger.logger.handlers) == 1
        assert logger.logger.level == logging.NOTSET

def test_logger_with_invalid_config(logger):
    with patch.object(FileLoader, 'loadFileData') as mock_loadFileData:
        mock_loadFileData.return_value = {'invalid_key': 'invalid_value'}
        logger.debug('Test debug message')
        logger.info('Test info message')
        logger.warning('Test warning message')
        logger.error('Test error message')
        logger.critical('Test critical message')
        assert len(logger.logger.handlers) == 1
        assert logger.logger.level == logging.NOTSET

def test_logger_with_valid_config(logger):
    with patch.object(FileLoader, 'loadFileData') as mock_loadFileData:
        mock_loadFileData.return_value = {
            'version': 1,
            'disable_existing_loggers': False,
            'handlers': {'console': {'class': 'logging.StreamHandler'}},
            'root': {'level': 'DEBUG', 'handlers': ['console']}
        }
        logger.debug('Test debug message')
        logger.info('Test info message')
        logger.warning('Test warning message')
        logger.error('Test error message')
        logger.critical('Test critical message')
        assert len(logger.logger.handlers) == 1
        assert logger.logger.level == logging.DEBUG

def test_logger_with_missing_handlers(logger):
    with patch.object(FileLoader, 'loadFileData') as mock_loadFileData:
        mock_loadFileData.return_value = {
            'version': 1,
            'disable_existing_loggers': False,
            'root': {'level': 'DEBUG', 'handlers': ['console']}
        }
        logger.debug('Test debug message')
        logger.info('Test info message')
        logger.warning('Test warning message')
        logger.error('Test error message')
        logger.critical('Test critical message')
        assert len(logger.logger.handlers) == 0
        assert logger.logger.level == logging.DEBUG

def test_logger_with_missing_root_level(logger):
    with patch.object(FileLoader, 'loadFileData') as mock_loadFileData:
        mock_loadFileData.return_value = {
            'version': 1,
            'disable_existing_loggers': False,
            'handlers': {'console': {'class': 'logging.StreamHandler'}},
            'root': {'handlers': ['console']}
        }
        logger.debug('Test debug message')
        logger.info('Test info message')
        logger.warning('Test warning message')
        logger.error('Test error message')
        logger.critical('Test critical message')
        assert len(logger.logger.handlers) == 1
        assert logger.logger.level == logging.NOTSET