# quick-log
 
***quicklog*** library is a python package the purpose from it , is to facilitate redirect logging with minimal config , also provide feature that other packages make it hard coded .

## Installation : 
```bash
pip install git+pip install git+https://github.com/LoremCoding/quick-log.git
```

## Features and Examples  : 
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
* the logger is designed to be a singelton object , once is imported all the logs will walk through it .
* the log file can be set through then an envirement varibale  :
```bash
export QUICK_LOG_FILE="...path to log file ...." ; python ..run your code ...
```
