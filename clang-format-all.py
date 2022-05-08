#!C:\Users\Admin\.pyenv\pyenv-win\versions\3.7.2\python.exe
import subprocess
import os
import sys
pypath = os.path.dirname(sys.executable)
print("pypath=", pypath)
files = [f for f in os.listdir(".") if os.path.isfile(f)]
files_filtered = [f for f in files if ".cpp" in f]
for f in files_filtered:
    print("Formatting", f)
    try:
        subprocess.run(["clang-format", "-i", f])
        print("Successfully Formated", f)
    except Exception as e:
        print("Failed Formated", f)
        print(e)
