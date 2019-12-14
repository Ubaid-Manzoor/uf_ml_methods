import os 
from pathlib import Path 
import zipfile


class fileHandler:

    @staticmethod
    def get_file_extension(cls,name): return name.split(sep='.')[-1]


    @staticmethod
    def remove_files_with_extension(cls,path='.', extension='jpg'):
        for file_name in os.listdir(path):
            if(cls.get_file_extension(file_name) == extension):
                os.remove( (path if path != '.' else '') +file_name)
                print(f"{file_name} removed!")


    @staticmethod
    def list_to_path(cls,l):
        to_return = ""
        for word in l:
            to_return += word + '/'
    
        return Path(to_return[0:-1])


    @staticmethod
    def list_to_str(cls,l,sep):
        to_return = ""
        for word in l:
            to_return += word + '.'

        return to_return[0:-1]

    
    @staticmethod
    def unzip(cls,path,dest):
        file_path = Path( cls.list_to_path(path.parts[0:-1]) / cls.list_to_str( path.parts[-1].split(sep='.')[0:-1],sep='.' ) )
        
        if(not (file_path).exists()):
            with zipfile.ZipFile(path,'r') as file_to_zip:
                file_to_zip.extractall(dest)
        else:
            print("File already Exists")