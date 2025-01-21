# vutil-py
Very Unofficial Python Bindings for Vision File Utility

## before installing
Copy a version of vutil32.exe from MicroFocus / OpenText to an accessible path.
vutil32.exe is a proprietary program and will not be included in this repo. 

## install
```sh
pip install git+https://github.com/officeofperformancemanagement/vutil-py
```

## usage
```py
from vutil import VUTIL

# create an instance of VUTIL
v = VUTIL("/Users/user/vutil32.exe")

src = "/Users/user/Documents/folder/DATA"
dst = "/Users/user/Documents/folder/DATA.txt"
v.unload(src, dst)
# creates a fixed-width text file of the data
```
