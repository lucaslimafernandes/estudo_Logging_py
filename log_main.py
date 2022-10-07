# Estudo do uso da biblioteca logging
# https://docs.python.org/3/library/logging.html


import datetime
import logging

# Instancia a classe loggin
log = logging.getLogger('log_main.py')

#configurando o logger
#FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
FORMAT = {
    'dt': '%Y-%m-%d %H:%M:%S',
    'filepath': f"{datetime.datetime.now().strftime('%Y-%m-%d')}.logger.log",
    'format': f'%(asctime)s {__file__} - {__name__}:%(process)d %(levelname)s %(message)s'
    }

logging.basicConfig(format=FORMAT['format'],                
                    filename=f'{FORMAT["filepath"]}',
                    filemode='a+',
                    level=logging.DEBUG
                    )

log.info('Informações')
log.warning('Warning')
log.error('error')

#logging.warning(FORMAT['dt'])


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






