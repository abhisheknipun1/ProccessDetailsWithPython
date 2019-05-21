import psutil
import os


def getTotalProcess():
    # proces = []
    # proc=[]
    # # Iterate over all running process
    # for proc in psutil.process_iter():
    #     try:
    #         # Get process name & pid from process object.
    #     #    processName = proc.name()
    #     #    processID = proc.pid
    #         proc= proc.as_dict(attrs = ['name'])
    #         proc["memory"] = proc.memory_info().vms /(1024*1024)
    #         proces.append(proc);
    #     except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
    #         pass
    # proces= sorted(proces, key = lambda obj: obj['memory'],reverse =True)

    listOfProcObjects = []
    # Iterate over the list
    for proc in psutil.process_iter():
       try:
           # Fetch process details as dict
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
           pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
           # Append dict to list
           listOfProcObjects.append(pinfo);
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass

    # Sort list of dict by key vms i.e. memory usage
    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)

    return listOfProcObjects


def sysLog():
    lines = 0
    logFile  = open("/var/log/syslog.1", "r")
    newLogFile = open("log.txt", "a")
    errorLines = logFile.readlines()
    logFile.close()
    for i, line in enumerate(errorLines):
        if "ERROR" in line:
            newLogFile.write(line)


runningProcess = getTotalProcess()

sysLog()

print ("----------Running Process------------")
for elem  in runningProcess:
    print (elem)
print ("------------Top 5 memory consumtion Running Process----------")
for elem  in runningProcess[:5]:
    print (elem)

print ("----Total Process Running")
print (len(runningProcess))
