def typeBasedTransformer(**a):
    transformed = {}
    
    for key, val in a.items():
        if type(val) in (int, float): 
            transformed[key] = val ** 2
        elif type(val) is str:  
            transformed[key] = val[::-1]
        elif type(val) is bool:  
            transformed[key] = not val
        elif type(val) in (list, tuple):  
            transformed[key] = val[::-1]
        elif type(val) is dict:
            if len(set(val.values())) == len(val):  
                transformed[key] = {v: k for k, v in val.items()}
            else:
                transformed[key] = val  
        else:
            transformed[key] = val  
    
    return transformed

# Call
data = {
    "Interger": 4,
    "Float": 2.5,
    "String": "Hello",
    "Bool": True,
    "List": [1, 2, 3],
    "Tuple": ("a", "b", "c"),
    "Mapping": {"a": 1, "b": 2}
}

print(typeBasedTransformer(**data))
