import os
import sys
import pathlib
import zipfile

dir = input()
if not os.path.isdir(dir):
    print("Dir DNE")
    sys.exit(0)
odir=pathlib.Path(dir)
with zipfile.ZipFile("myzip.zip", "w") as a:
    for f in odir.rglob("*"):
        a.write(f,f.relative_to(odir))
if os.path.isfile("my.zip"):
    print("Archive my.zip created succsessfully")
else:
    print("Error in creating archive")
