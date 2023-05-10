# Configuration is saved as json file
import os
import json

class Configuration:
    def __init__(self, path):
        # if no path is given, use a file named json.config in the current directory
        if path == None:
            path = "json.config"

        self.path = path
        self.config = None
        self.load()

    # initializes the configuration file with default values
    def init(self):
        # only init if no config file exists in path
        if not os.path.exists(self.path):
            self.config = {
                'vmrunPath': r'C:\Program Files (x86)\VMware\VMware Player\vmrun.exe',
                'vmwarePath': r'E:\Virtual Machines\Ubuntu DEV',
                'vmwareName': 'Ubuntu DEV'
            }

    def get_vmware_name(self):
        return self.config['vmwareName']

    def set_vmware_name(self, name):
        self.config['vmwareName'] = name

    # gets the path of the vmrun file
    def get_vmrun_path(self):
        return self.config['vmrunPath']

    # sets the path of the vmrun file
    def set_vmrun_path(self, path):
        self.config['vmrunPath'] = path

    # gets the path of the vmware file
    def get_vmware_path(self):
        return self.config['vmwarePath']

    # sets the path of the vmware file
    def set_vmware_path(self, path):
        self.config['vmwarePath'] = path

    def load(self):
        with open(self.path, 'r') as f:
            self.config = json.load(f)

    def save(self):
        with open(self.path, 'w') as f:
            json.dump(self.config, f, indent=4)

    def get(self, key):
        return self.config[key]

    def set(self, key, value):
        self.config[key] = value

    def get_config(self):
        return self.config

    def set_config(self, config):
        self.config = config

    def get_path(self):
        return self.path

    def set_path(self, path):
        self.path = path

