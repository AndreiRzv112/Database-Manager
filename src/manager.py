import sqlite3, os, sys
import db_error

class database:
    def create(self, name:str=None, dir:str=None):
        if name is not None or False:
            name = name.split(".")
            name = name[0]
        else:
            name = "database"
        if dir is not None or False:
            _, folders, _ = next(os.walk(sys.path[0]))
            valid = False
            for x in folders:
                if x.lower() == dir.lower():
                    dir = x
                    valid = True
                    break
            if valid is False:
                os.mkdir(dir)
            db_path = sys.path[0] + "\\" + dir
            _, _, filename = next(os.walk(db_path))
            for x in filename:
                x = x[:-3]
                if x.lower() == name.lower():
                    raise db_error.DatabaseAlreadyExists("This database already exists")
            sqlite3.connect("./" + dir + "/" + name + ".db")
        elif dir == None or dir == False:
            _, _, filename = next(os.walk(sys.path[0]))
            for x in filename:
                x = x[:-3]
                if x.lower() == name.lower():
                    raise db_error.DatabaseAlreadyExists("This database already exists")
                sqlite3.connect(name + ".db")
        else:
            raise db_error.UnexpectedError("An unexpected Error occurred")

    def delete(self, name, dir:str=None):
        if name is not None or False:
            name = name.split(".")
            name = name[0]
        if dir is not None or False:
            _, folders, _ = next(os.walk(sys.path[0]))
            valid = False
            for x in folders:
                if x.lower() == dir.lower():
                    dir = x
                    valid = True
                    break
            if valid is False:
                raise db_error.DirectoryNotFound(f"Folder | {dir} | not found")
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
                raise db_error.FileNotFound(f"Database | {name}.db | not found")
            os.remove("./" + dir + "/" + name + ".db")
        elif dir == None or dir == False:
            _, _, filename = next(os.walk(sys.path[0]))
            valid = False
            for x in filename:
                x = x[:-3]
                if x.lower() == name.lower():
                    name = x
                    valid = True
                    break
            if valid == False:
                raise db_error.FileNotFound(f"Database | {name}.db | not found")
            os.remove(name + ".db")
        else:
            raise db_error.UnexpectedError("An unexpected Error occurred")
        
class table:
    pass
