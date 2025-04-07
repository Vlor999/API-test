import json
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def write_data(filename:str, data:json, timeInfo:bool = False) -> str:
    if timeInfo:
        current_datetime = datetime.now()
        currentTime = current_datetime.strftime("%m-%d-%Y:%Hh%Mm%Ss")
        filename += "-" + currentTime
        logger.debug(f"Current date time : {currentTime}")
    
    filename += ".json"

    logger.debug(f"Writting datas into the file : {filename}")
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return filename