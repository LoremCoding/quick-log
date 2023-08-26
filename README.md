# quick-log
Minimal easy logging 
# Introduction  : 
***quicklog*** library is a python package the purpose from it , is to facilitate redirect logging with minimal config , also provide feature that other packages make it hard coded .

# Installation : 
```bash
pip install git+pip install git+https://github.com/LoremCoding/quick-log.git
```

# Features and Examples  : 
* Quick start :
```python
from quicklog import *
SET_LOG_FILE("./myLog.log")
dprint("this is a debuging message")
wprint("this is a warning message")
eprint("this is a error message")
cprint("this is a critical message")
iprint("this is a info message")
```
