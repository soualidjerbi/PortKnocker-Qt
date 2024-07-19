import json, sys
from pathlib import Path

class FileLoader:
    @staticmethod
    def getFilePath(config_file) -> str:
        path = f'{Path(sys._MEIPASS).resolve()}' if getattr(sys, 'frozen', False) else f'{Path(__file__).parent.parent.resolve()}/configs'
        config_file = f'{path}/{config_file}'
        if Path(config_file).exists() == True:
            return config_file
        else:
            return FileNotFoundError(f'File not found: {config_file}')
    @staticmethod
    def loadFileData(config_file) -> dict:
        config_file = FileLoader.getFilePath(config_file)
        with open(config_file, 'r') as f:
            config = json.load(f)
        return config
    @staticmethod
    def saveDictToFile(config_file, jsonData)->None:
        config_file = FileLoader.getFilePath(config_file)
        with open(config_file, 'w') as f:
            json.dump(obj=jsonData, fp=f ,indent=4)
    @staticmethod
    def saveTextToFile(config_file, textData)->None:
        config_file = FileLoader.getFilePath(config_file)
        with open(config_file, 'w') as f:
            f.write(textData)