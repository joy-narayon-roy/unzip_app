import json
from  datetime import datetime 

class SaveHistory:
    file_name = ""
    data_file = "./.history/history.json"
    
    def __init__(self, file_name):
        self.file_name = file_name 
        self.save_data()
    
    def new_history (self):
        return {
            'time':datetime.now().__str__(),
            'file':self.file_name
        }
    
    def create_file(self):
        file = open(self.data_file,'w')
        file.write('[]')
        file.close()
        return self.save_data()
    
    def save_data(self):
        try:
            history = json.load(open(self.data_file))
            history.append(self.new_history())
            json.dump(history,open(self.data_file,"w"))
            
        except Exception as e:
            if (e.__class__.__name__)=='FileNotFoundError':
                self.create_file()
            else :
                print('Some error')
