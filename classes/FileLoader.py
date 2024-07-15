import json, os, sys
from pathlib import Path

class FileLoader:
    def __init__(self, config_file, logger=None):
        self.logger = logger
        self.config_file = self.getFilePath(config_file)

    def getFilePath(self, config_file)->str:
        path = f'{Path(sys._MEIPASS).resolve()}' if getattr(sys, 'frozen', False) else f'{Path(__file__).parent.parent.resolve()}/configs'
        return f'{path}/{config_file}'
  
    def loadFileData(self):
        if Path(self.config_file).exists() == False:
            return ValueError(f'File not found: {self.config_file}')
        with open(self.config_file, 'r') as f:
            config = json.load(f)
        return config
    
    def saveDataToFile(self, jsonData)->None:
        with open(self.config_file, 'w') as f:
            json.dump(obj=jsonData, fp=f ,indent=4)
    
    def saveTextToFile(self, textData)->None:
        with open(self.config_file, 'w') as f:
            f.write(textData)