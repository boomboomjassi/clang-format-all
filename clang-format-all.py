#!C:\Users\Admin\.pyenv\pyenv-win\versions\3.7.2\python.exe
import subprocess
import os
import sys

pypath = os.path.dirname(sys.executable)
print("pypath=", pypath)


def format_all_files_under(direc="."):
    print("Formatting all .cpp files directly under : {}".format(direc))
    files = [f for f in os.listdir(direc) if os.path.isfile(direc + "\\" + f)]
    files_filtered = [f for f in files if ".cpp" in f]
    for f in files_filtered:
        print("Formatting", f)
        try:
            subprocess.run(["clang-format", "-i", direc + "\\" + f])
            print("Successfully Formated", f)
        except Exception as e:
            print("Failed Formated", f)
            print(e)


format_all_files_under()
folders = []
for f in os.scandir("."):
    if "." not in f.name:
        folders.append(os.path.abspath(f))

for folder in folders:
    try:
        format_all_files_under(folder + "\\")
    except Exception as e:
        print(e)
