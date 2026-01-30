import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    
)

'''
Run the code below only if this file is executed directly, not when it is imported.
Prevents unwanted execution when the file is imported. Allows the file to be reused as a module
'''

"""
if __name__ == "__main__": 
    logging.info("Logging has been set up.")
    
"""
