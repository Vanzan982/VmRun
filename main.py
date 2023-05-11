from vmrun import vmrun

if __name__ == "__main__":
    vr = vmrun()
    if not vr.getRunningVms():
        vr.StartVm()