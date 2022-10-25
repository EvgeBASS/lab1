import os
import json
import sqlite3


class DBConfig():
    db_url = os.getcwd() + '/data/asm2204/st21/notebook.db'

    notebooks_table_creation = 'CREATE TABLE IF NOT EXISTS notebooks (' \
                               'id INTEGER NOT NULL, ' \
                               'PRIMARY KEY (id))'

    notes_table_creation = 'CREATE TABLE IF NOT EXISTS notes (' \
                           'id INTEGER NOT NULL, ' \
                           'type VARCHAR(60) NOT NULL, ' \
                           'title VARCHAR(60), ' \
                           'description VARCHAR(60), ' \
                           'notebook_id INTEGER, ' \
                           'PRIMARY KEY (id), ' \
                           'FOREIGN KEY(notebook_id) REFERENCES notebooks (id))'

    creatures_table_creation = 'CREATE TABLE IF NOT EXISTS creatures (' \
                               'id INTEGER NOT NULL, ' \
                               'type VARCHAR(60) NOT NULL, ' \
                               'title VARCHAR(60), ' \
                               'description VARCHAR(60), ' \
                               'price INTEGER, ' \
                               'notebook_id INTEGER, ' \
                               'PRIMARY KEY (id), ' \
                               'FOREIGN KEY(notebook_id) REFERENCES notebooks (id))'

    notebook_creation = 'INSERT INTO notebooks (id) VALUES (1);'

    notebook_all = 'SELECT * FROM notebooks'

    notes_all = 'SELECT * FROM notes WHERE notebook_id = ?'

    notes_add = 'INSERT INTO notes (type, title, description, notebook_id) VALUES (?, ?, ?, ?)'

    notes_edit = 'UPDATE notes SET title = ?, description = ? WHERE id = ?'

    notes_delete = 'DELETE FROM notes WHERE id = ?'

    creatures_all = 'SELECT * FROM creatures WHERE notebook_id = ?'

    creatures_add = 'INSERT INTO creatures (type, title, description, price,  notebook_id) VALUES (?, ?, ?, ?, ?)'

    creatures_edit = 'UPDATE creatures SET title = ?, description = ?, price = ? WHERE id = ?'

    creatures_delete = 'DELETE FROM creatures WHERE id = ?'

    util_last_id = 'SELECT last_insert_rowid()'

    @staticmethod
    def init_db():
        try:
            with open(DBConfig.db_url, 'r'):
                print("База данных найдена")
        except Exception:
            print("path = ", DBConfig.db_url)
            print("База данных не найдена")

            try:
                connection = sqlite3.connect(DBConfig.db_url)

                cursor = connection.cursor()

                # Создаем пустую записную книжку
                cursor.execute(DBConfig.notebook_creation)

                cursor.fetchall()

                connection.commit()

                connection.close()

                print('Создана новая база данных')
            except Exception:
                print('Не удалось создать новую базу данных')

    @staticmethod
    def get_notebook():
        try:
            connection = sqlite3.connect(DBConfig.db_url)
            connection.row_factory = sqlite3.Row

            cursor = connection.cursor()

            cursor.execute(DBConfig.notebook_all)

            notebooks = json.loads(json.dumps([dict(ix) for ix in cursor.fetchall()]))

            connection.close()

            print("Получен список Записных книжек")

            return notebooks
        except Exception:
            print("Не удалось получить список Записных книжек")

            return []

    @staticmethod
    def get_notes(notebook_id):
        try:
            connection = sqlite3.connect(DBConfig.db_url)
            connection.row_factory = sqlite3.Row

            cursor = connection.cursor()

            cursor.execute(DBConfig.notes_all, (notebook_id,))

            notes_result = cursor.fetchall()

            notes = []

            if notes_result is not None:
                notes = json.loads(json.dumps([dict(ix) for ix in notes_result]))

            cursor.execute(DBConfig.creatures_all, (notebook_id,))

            creatures_result = cursor.fetchall()

            creatures = []

            if notes_result is not None:
                creatures = json.loads(json.dumps([dict(ix) for ix in creatures_result]))

            print('Получен список Записей и Существ')

            connection.close()

            return notes, creatures
        except Exception as e:
            print(e)

            print("Не удалось получить список Записей и Существ")

    @staticmethod
    def add_to_notebook(notebook_id, note):
        try:
            connection = sqlite3.connect(DBConfig.db_url)
            connection.row_factory = sqlite3.Row

            cursor = connection.cursor()

            if note.type == 'NOTE':
                cursor.execute(DBConfig.notes_add, (note.type, note.title, note.description, notebook_id))
            elif note.type == 'CREATURE':
                cursor.execute(DBConfig.creatures_add,
                               (note.type, note.title, note.description, note.price, notebook_id))

            connection.commit()

            cursor.fetchall()

            cursor.execute(DBConfig.util_last_id)

            res = json.loads(json.dumps([dict(ix) for ix in cursor.fetchall()]))[0]

            connection.close()

            return int(res['last_insert_rowid()'])
        except Exception as e:
            print(e)

            print("Не удалось добавить Заметку")

            return None

    @staticmethod
    def edit_notebook(note):
        try:
            connection = sqlite3.connect(DBConfig.db_url)
            connection.row_factory = sqlite3.Row

            cursor = connection.cursor()

            if note.type == 'NOTE':
                cursor.execute(DBConfig.notes_edit, (note.title, note.description, note.id))
            elif note.type == 'CREATURE':
                cursor.execute(DBConfig.creatures_edit,
                               (note.title, note.description, note.price, note.id))

            connection.commit()

            connection.close()

            return 'Ok'
        except Exception:
            print("Не удалось добавить Заметку")

            return None

    @staticmethod
    def delete_from_notebook(id, type):
        try:
            connection = sqlite3.connect(DBConfig.db_url)
            connection.row_factory = sqlite3.Row

            cursor = connection.cursor()

            if type == 'NOTE':
                cursor.execute(DBConfig.notes_delete, (id,))
            elif type == 'CREATURE':
                cursor.execute(DBConfig.creatures_delete, (id,))

            connection.commit()

            connection.close()

            return 'Ok'
        except Exception:
            print("Не удалось добавить Заметку")

            return None
