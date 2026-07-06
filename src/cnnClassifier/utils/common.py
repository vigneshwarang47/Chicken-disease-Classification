import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box.config_box import ConfigBox
from pathlib import Path
from typing import Any
import base64

# Ensures function inputs and outputs follow the specified type annotations.
@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """_summary_

    Args:
        path_to_yaml (Path): _description_

    Returns:
        ConfigBox: _description_
    """

    try:
        with open(path_to_yaml)as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded sucessfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directory:list,verbose=True):
    """_summary_

    Args:
        path_to_directory (list): list of path of directories
        verbose (bool, optional): _description_. Defaults to True.

    Returns:
        _type_: _description_
    """
    for path in path_to_directory:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"create directory at: {path}")


@ensure_annotations
def save_json(path: Path, data:dict):
    """_summary_

    Args:
        path (Path): _description_
        data (dict): _description_
    """
    with open(path,'w') as f:
        json.dump(data,f, indent=4)
    logger.info(f"json file saved at:{path}")

@ensure_annotations
def load_json(path:Path)-> ConfigBox:
    """_summary_

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)
        
    logger.info(f"json file loaded sucessfully from : {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any, path: Path):
    """_summary_

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path:Path)->Any:
    """_summary_

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from : {path}")
    return data

@ensure_annotations
def get_size(path:Path) -> str:
    """_summary_

    Args:
        path (Path): path of the file

    Returns:
        str: size in kb
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"

def decodeImage(imgstring,fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName,'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,'rb')as f:
        return base64.b64encode(f.read())