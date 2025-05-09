import os 
import sys 

import numpy as np 
import dill 
import yaml 
from pandas import DataFrame 

from src.exception import MyException
from src.logger import logging 

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, 'rb') as f:
            return yaml.safe_load(f)
    
    except Exception as e:
        raise MyException(e, sys)
    
def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            yaml.dump(f, content)
    
    except Exception as e:
        raise MyException(e, sys)
    

def save_object(file_path: str, obj: object) -> None:
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as f:
            dill.dump(obj, f)
            
    except Exception as e:
        raise MyException(e, sys)
    

def load_object(file_path: str) -> object:
    """
    Returns model/object from project directory.
    file_path: str location of object file to load
    return: Model/Obj
    """
    try:
        with open(file_path, "rb") as f:
            obj = dill.load(f)
        return obj 
    
    except Exception as e:
        raise MyException(e, sys)
    

def save_numpy_array_data(file_path: str, array: np.array) -> None:
    """
    Save numpy array data to file
    file_path: str location of file to save
    array: np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as f:
            np.save(f, array)
    
    except Exception as e:
        raise MyException(e, sys)

def load_numpy_array_data(file_path: str) -> np.array:
    """
    Load numpy array data from file
    file_path: str location of file to load
    return: np.array data
    """
    try:
        with open(file_path, "rb") as f:
            return np.load(f)
    except Exception as e:
        raise MyException(e, sys)
    
