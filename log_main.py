# Estudo do uso da biblioteca logging
# https://docs.python.org/3/library/logging.html

## https://github.com/WebGlobal/RobotProxy/blob/master/src/settings.py

import datetime


import logging

#logging.warning(' Iniciou o script! ')

# Instancia a classe loggin
log = logging.getLogger('log_main.py')
#print(log)

#configurando o logger
#FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
FORMAT = {
    'dt': '%Y-%m-%d %H:%M:%S',
    'filepath': f"{datetime.datetime.now().strftime('%Y-%m-%d')}.logger.log",
    'ff': 'log.log'
}

logging.basicConfig(filename=f'{FORMAT["filepath"]}',
                    filemode='a+',
                    level=logging.DEBUG
                    )

log.info('Informações')
log.warning('Warning')
log.error('error')

logging.warning(FORMAT['dt'])


"""
log.log levels
CRITICAL    50
ERROR       40
WARNING     30
INFO        20
DEBUG       10
NOTSET      0
"""
log.log(level=50,msg='log.log')





