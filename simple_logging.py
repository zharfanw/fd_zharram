import logging
import logging.config
import os

# Konfigurasi path
log_dir = ".logfile"
log_file_path = os.path.join(log_dir, "logfile.log")
conf_file = "temp.conf"

# Buat folder .logfile kalau belum ada
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Buat file config jika belum ada
if not os.path.exists(conf_file):
    with open(conf_file, "w") as f:
        f.write(f"""
[loggers]
keys=root,simpleExample

[handlers]
keys=consoleHandler,fileHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=WARNING
handlers=consoleHandler

[logger_simpleExample]
level=DEBUG
handlers=consoleHandler,fileHandler
qualname=simpleExample
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args=(sys.stdout,)

[handler_fileHandler]
class=FileHandler
level=DEBUG
formatter=simpleFormatter
args=('{log_file_path}', 'a')

[formatter_simpleFormatter]
format=%(asctime)s - %(name)s - %(levelname)s - %(message)s
datefmt=
""")

# Load logging config
logging.config.fileConfig(conf_file)

# Buat logger
logger = logging.getLogger('simpleExample')

# Contoh pemakaian logging
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
