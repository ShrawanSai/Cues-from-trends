import os
import datetime
from dashboard_table.src import *
import logging
def run_scheduler():


    print('starting')
    logging.basicConfig( '%(asctime)s - %(name)s - %(levelname)s: %(message)s')
    logger = logging.getLogger(__name__)
    
    
    logging.info('starting')
    path_to_save_to = os.getcwd()
    path_to_save_to = os.path.join(path_to_save_to,'src')

    logging.warning(f'This is the path : {path_to_save_to}')


    if dashboard_table.src.main.start_main(path_to_save_to):
        print('done')
        logging.critical('Log successful')
        ct = datetime.datetime.now() 
        with open('logs.txt','w') as f:
            f.write(f'Succesfully recomputed at {ct}')
    else:
        print('fail')
        logging.error('Failed')
        ct = datetime.datetime.now() 
        with open('logs.txt','w') as f:
            f.write(f'Failed at {ct}')

            
