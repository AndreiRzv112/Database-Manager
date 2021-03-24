import sqlite3, os, sys
from itertools import zip_longest
import db_error
import functions as func

class database:
    def create(self, name:str=None, dir:str=None):
        if isinstance(name, str):
            name = name.split(".")
            name = name[0]
        else:
            name = "database"
        if isinstance(dir, str):
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
                    raise db_error.DatabaseAlreadyExists("This database already exists.")
            sqlite3.connect("./" + dir + "/" + name + ".db")
        elif dir == None or dir == False:
            _, _, filename = next(os.walk(sys.path[0]))
            for x in filename:
                x = x[:-3]
                if x.lower() == name.lower():
                    raise db_error.DatabaseAlreadyExists("This database already exists.")
                sqlite3.connect(name + ".db")
        else:
            raise db_error.UnexpectedError("An unexpected Error occurred, Please check | dir |")

    def delete(self, name:str, dir:str=None):
        if isinstance(name, str):
            name = name.split(".")[0]
        db_path = func.FileDir(self, name=name, dir=dir)
        os.remove(db_path)

class table:
    def create(self, table_name:str, column:list=[], val:list=[], db_name:str=None, db_dir:str=None):
        if isinstance(db_name, str) and isinstance(table_name, str):
            db_name = db_name.split(".")[0]
        else:
            raise db_error.InvalidArgs("Names needs to be a string.")
        if not isinstance(column, list):
            raise db_error.InvalidArgs("| column | needs to be a list.")
        if not isinstance(val, list):
            raise db_error.InvalidArgs("| val | needs to be a list.")
        if len(column) == 0:
            raise db_error.MissingArgs("| column | cannot be empty.")
        valide_vals = ["int", "integer", "text", "blob", "real", "numeric"]
        if len(val) != 0:
            for x in val:
                if not x.lower() in valide_vals:
                    raise db_error.InvalidArgs(f"| {x} | is not valide.")
        db_path = func.FileDir(self, name=db_name, dir=db_dir)
        with sqlite3.connect(db_path) as db:
            c = db.cursor()
            args_list = list(zip_longest(column, val))
            sql_text = ""
            for x in args_list:
                if x[0] is not None:
                    if x[1] is None:
                        y = "TEXT"
                    else:
                        y = x[1]
                    sql_text = sql_text + x[0] + " " + y.upper() + ",\n"
                else:
                    break
            sql_text = sql_text[:-2]
            c.execute(f"CREATE TABLE {table_name.lower()}({sql_text})")
            db.commit()
    
    def delete(self, table_name:str=None, db_name:str=None, db_dir:str=None):
        if isinstance(db_name, str) and isinstance(table_name, str):
            db_name = db_name.split(".")[0]
        else:
            raise db_error.InvalidArgs("Names needs to be a string.")
        db_path = func.FileDir(self, name=db_name, dir=db_dir)
        with sqlite3.connect(db_path) as db:
            c = db.cursor()
            c.execute(f"DROP TABLE {table_name.lower()}")
            db.commit()
