from typing import Any

def all_thing_is_obj(object: Any) -> int:
    if type(object) == list:
        print("List :", type(object))
    elif type(object) == tuple:
        print("tuple :", type(object))
    elif type(object) == set:
        print("set :", type(object))
    elif type(object) == dict:
        print("dict :", type(object))
    elif type(object) == str:
        print(object, "is in the kitchen :", type(object))
    else :
        print("Type not found")
    
    return 42