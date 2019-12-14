import subprocess
import difflib
from subprocess import PIPE

class package_handler:
  def __init__(self):
    self.__package_dict = self.__get_package_dict() 

  def __get_package_dict(self):
    raw_package_list = subprocess.run(['pip', 'freeze'],stdout=PIPE).stdout.decode().split(sep='\n')

    package_dict = {}
    for raw_package in raw_package_list:
      try:
        name = raw_package.split(sep='==')[0]
        version = raw_package.split(sep='==')[1]

        package_dict[name] = version
      except(Exception):
        pass        
    return package_dict


  def version(self,package_name):
    package_list = self.__package_dict.keys()
    if package_name in package_list:
      return self.__package_dict[package_name]
    else:
      close_matches = difflib.get_close_matches(package_name,package_list)
      print("packes you mentioned does not exits other close matches are")
      print(close_matches)

  def __find_package(self,package):
    if(self.package_dict):
      return self.package_dict
    else:
      return False

  def install(self,package):
    if(self.__find_package(package)):
      print("Package Already Exits")
    else:
      subprocess.run(['pip' , 'install' ,{package}])