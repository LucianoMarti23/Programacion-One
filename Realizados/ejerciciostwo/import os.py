import os
import sys
import win32com.shell.shell as shell
import subprocess
ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    sys.exit(0)
    
print ("I am root now.")

word  = "C:\\Program Files\\Microsoft Office\\root\\Office16"

subprocess.run([word])
