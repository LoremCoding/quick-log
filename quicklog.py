import logging , io , os


# Configure logging



class iLogger:
	_instance = None
	_filename = "Log.log"
	_mode = "w"
	def __init__(self) : 
		logging.basicConfig(
			level=logging.DEBUG,  # Set the minimum logging level to capture
			format='[%(levelname)s]: %(message)s',
			filename= iLogger._filename,  # Log file name
			filemode= iLogger._mode # Overwrite the log file each time the program runs
		)
		self.logger = logging.getLogger(__name__)

	def __new__(cls):
		if cls._instance is None:
			cls._instance = super(Logger, cls).__new__(cls)
		return cls._instance

	def debug(self,*args , **kwargs) : 
		iLogger._filename = os.environ.get("QUICK_LOG_FILE"  ,iLogger._filename )
		string_stream = io.StringIO()
		print(*args,**kwargs)
		print(*args,**kwargs , file = string_stream)
		self.logger.debug(string_stream.getvalue())

	def info(self,*args , **kwargs) : 
		iLogger._filename = os.environ.get("QUICK_LOG_FILE"  ,iLogger._filename )
		string_stream = io.StringIO()
		print(*args,**kwargs)
		print(*args,**kwargs , file = string_stream)
		self.logger.info(string_stream.getvalue())

	def warning(self,*args , **kwargs) : 
		iLogger._filename = os.environ.get("QUICK_LOG_FILE"  ,iLogger._filename )
		string_stream = io.StringIO()
		print(*args,**kwargs)
		print(*args,**kwargs , file = string_stream)
		self.logger.warning(string_stream.getvalue())

	def error(self,*args , **kwargs) : 
		iLogger._filename = os.environ.get("QUICK_LOG_FILE"  ,iLogger._filename )
		string_stream = io.StringIO()
		print(*args,**kwargs)
		print(*args,**kwargs , file = string_stream)
		self.logger.error(string_stream.getvalue())

	def critical(self,*args , **kwargs) : 
		iLogger._filename = os.environ.get("QUICK_LOG_FILE"  ,iLogger._filename )
		string_stream = io.StringIO()
		print(*args,**kwargs)
		print(*args,**kwargs , file = string_stream)
		self.logger.critical(string_stream.getvalue())




def dprint(*args,**kwargs) : iLogger().debug(*args,**kwargs)
def iprint(*args,**kwargs) : iLogger().info(*args,**kwargs)
def wprint(*args,**kwargs) : iLogger().warning(*args,**kwargs)
def eprint(*args,**kwargs) : iLogger().error(*args,**kwargs)
def cprint(*args,**kwargs) : iLogger().critical(*args,**kwargs)
def SET_LOG_FILE(filepath) : 
	iLogger._filename = filepath
	os.environ['QUICK_LOG_FILE'] = iLogger._filename
	


__all__ = ['dprint' , 'iprint' , 'wprint' , 'eprint' , 'cprint' , 'SET_LOG_FILE_NAME']



