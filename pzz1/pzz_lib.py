import os

def workname(filename:str) -> str:
    dirname = os.path.dirname(__file__)
    wname = os.path.join(dirname, filename)
    return wname