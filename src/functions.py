import db_error
import os, sys

def FileDir(self, name:str, dir:str=None):
    if isinstance(dir, str):
        _, folders, _ = next(os.walk(sys.path[0]))
        valid = False
        for x in folders:
            if x.lower() == dir.lower():
                dir = x
                valid = True
                break
        if valid == False:
            raise db_error.DirectoryNotFound(f"Folder | {dir} | not found.")
        db_path = sys.path[0] + "\\" + dir
        _, _, filename = next(os.walk(db_path))
        valid = False
        for x in filename:
            x = x[:-3]
            if x.lower() == name.lower():
                name = x
                valid = True
                break
        if valid == False:
            raise db_error.FileNotFound(f"Database | {name}.db | not found.")
        return str("./" + dir + "/" + name + ".db")
    elif dir == None:
        _, _, filename = next(os.walk(sys.path[0]))
        valid = False
        for x in filename:
            x = x[:-3]
            if x.lower() == name.lower():
                name = x
                valid = True
                break
        if valid == False:
            raise db_error.FileNotFound(f"Database | {name}.db | not found.")
        return str(name + ".db")
    else:
        raise db_error.UnexpectedError("An unexpected Error occurred, Please check | dir |")