from typing import Dict, List, Union

from bson import ObjectId
from pymongo.cursor import Cursor


def obj_to_str(data: Union[List, Dict, ObjectId]):
    """Converts `ObjectId` to string."""
    if isinstance(data, dict):
        return {obj_to_str(key): obj_to_str(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [obj_to_str(element) for element in data]
    elif isinstance(data, ObjectId):
        return str(data)
    else:
        return data


def to_dict(func):
    """A nice decorator to convert pymongo objects to dict"""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result = obj_to_str(result)
        return result

    return wrapper
