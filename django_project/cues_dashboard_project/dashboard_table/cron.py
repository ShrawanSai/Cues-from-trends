import os
import datetime
from dashboard_table.src.main import start_main
import logging
def run_scheduler():


    path_to_save_to = os.getcwd()
    if start_main(path_to_save_to):
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

            
