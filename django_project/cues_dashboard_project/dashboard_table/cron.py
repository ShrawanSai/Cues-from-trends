import os
import datetime
import src
import logging
def run_scheduler():


    with open('logs.txt','a') as f:
        ct = datetime.datetime.now()
        f.write(f'last at {ct}')


    '''logging.basicConfig( '%(asctime)s - %(name)s - %(levelname)s: %(message)s')
    logger = logging.getLogger(__name__)
    
    
    logging.info('starting')
    path_to_save_to = os.getcwd()
    path_to_save_to = os.path.join(path_to_save_to,'src')

    logging.warning(f'This is the path : {path_to_save_to}')


    if src.main.start_main(path_to_save_to):
        logging.critical('Log successful')
        ct = datetime.datetime.now() 
        with open('logs.txt','w') as f:
            f.write(f'Succesfully recomputed at {ct}')
    else:
        logging.error('Failed')
        ct = datetime.datetime.now() 
        with open('logs.txt','w') as f:
            f.write(f'Failed at {ct}')'''

            
