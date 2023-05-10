import subprocess
from Configuration import Configuration
import os

class vmrun:
    def __init__(self):
        self.config = Configuration(None)

        self.vmrunPath = self.config.get_vmrun_path()
        self.vmwarePath = self.config.get_vmware_path()


    def GetVmwarePath(self):
        vmname = self.config.get_vmware_name()
        vmwarePath = self.vmwarePath + "\\" +  vmname + ".vmx"
        return vmwarePath

    def getRunningVms(self):
        vmname = self.config.get_vmware_name()
        vmwarePath = self.GetVmwarePath(vmname)
        command = self.vmrunPath + " list"
        p = subprocess.Popen(command, stdout=subprocess.PIPE)

        returnValues = p.stdout.readlines()
        for vmware in returnValues[1:]:
            if vmwarePath in vmware.__str__():
                return True
        
        return False

    def StartVm(self):
        vmname = self.config.get_vmware_name()
        vmwarePath = self.GetVmwarePath(vmname)
        command = "\"" + self.vmrunPath + "\" start \"" + vmwarePath + "\" gui"
        subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, start_new_session=True)        
        #print(f"result {p.returncode}")
                
if __name__ == "__main__":
    vr = vmrun()
    if not vr.getRunningVms():
        vr.StartVm()