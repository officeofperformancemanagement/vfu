# vfu
Unofficial Python Bindings for Vision File Utility

## install
```sh
pip install vfu
```

## usage
```py
from vfu import vutil32

# create an instance of vutil32
v = vutil32("/Users/user/vutil32.exe")

src = "/Users/user/Documents/folder/DATA"
dst = "/Users/user/Documents/folder/DATA.txt"
v.unload(src, dst)
# creates a fixed-width text file of the data
```
