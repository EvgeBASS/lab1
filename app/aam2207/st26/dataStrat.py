import pickle
import sqlite3
import shelve
from .chicken import *

class PickleBehaviour:

    @staticmethod
    def obj_to_file(path, obj):
        try:
            with open(path + 'dumpPickle.dat', 'wb') as dump_out:
                pickle.dump(obj, dump_out)
        except Exception as e:
            print('Не получилось: ', e)

    @staticmethod
    def obj_from_file(path):
        try:
            with open(path + 'dumpPickle.dat', 'rb') as dump_in:
                return pickle.load(dump_in)
        except Exception as e:
            print('Не получилось: ', e)

    def __repr__(self):
        return 'поведение Pickle'


class ShelveBehaviour:

    @staticmethod
    def obj_to_file(path, obj):
        db = shelve.open(path + 'dumpShelve')
        try:
            db['obj'] = obj
        except Exception as e:
            print('Не получилось: ', e)
        finally:
            db.close()

    @staticmethod
    def obj_from_file(path):
        db = shelve.open(path + 'dumpShelve')
        obj = []
        try:
            obj = db['obj']
        except Exception as e:
            print('Не получилось: ', e)
        finally:
            db.close()
        return obj

    def __repr__(self):
        return 'поведение Shelve'


class SQLLiteBehaviour:

    @staticmethod
    def obj_to_file(cur, obj):
        cur.execute("DELETE FROM [Chiken] WHERE 3 = 3")
        SQLstr = "INSERT INTO [Chiken] VALUES (NULL, ?, ?, ?, ?, ?, ?)"
        for chick in obj:
            cur.execute(SQLstr, chick.DBInsertStr())

    @staticmethod
    def obj_from_file(cur):
        obj = []
        cur.execute("SELECT * FROM [Chiken]")
        for r in cur:
            class_type = r['Class_type']
            item = None
            if class_type == 'Chicken':
                item = Chicken()
            elif class_type == 'BrolBoy':
                item = BrolBoy()
            elif class_type == 'SuperChicken':
                item = SuperChicken()
            item.DBLoad(r)
            obj.append(item)
        return obj

    def __repr__(self):
        return 'поведение SqlLite'