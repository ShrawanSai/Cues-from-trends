import os
import datetime
from proj import main
def run_scheduler():
    path_to_save_to = os.getcwd()

    if main.main(path_to_save_to):
        ct = datetime.datetime.now() 
        with open('logs.txt','w') as f:
            f.write(f'Succesfully recomputed at {ct}')
    else:
        ct = datetime.datetime.now() 
        with open('logs.txt','w') as f:
            f.write(f'Failed at {ct}')

            
    
