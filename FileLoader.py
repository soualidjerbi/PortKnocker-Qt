import json, os	

class FileLoader:
    def __init__(self, config_file, logger=None):
        self.logger = logger
        self.config_file = self.getFilePath(config_file)

    def getFilePath(self, config_file)->str:
        try:
            path = f'{self.resource_path(".")}/{config_file}'
        except Exception:
            path = f'{os.path.dirname(__file__)}/{config_file}'
        return path 
    
    def loadFileData(self):
        with open(self.config_file, 'r') as f:
            config = json.load(f)
        return config
    
    def saveDataToFile(self, jsonData)->None:
        with open(self.config_file, 'w') as f:
            json.dump(obj=jsonData, fp=f ,indent=4)
    
    def saveTextToFile(self, textData)->None:
        with open(self.config_file, 'w') as f:
            f.write(textData)