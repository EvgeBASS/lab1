import os
import json

from flask import Blueprint, render_template, request, g

from app.asm2204.st21.database.db_config import DBConfig
from app.asm2204.st21.feature.containers.Notebook import Notebook
from app.asm2204.st21.feature.models.Creature import Creature
from app.asm2204.st21.feature.models.Note import Note
from app.asm2204.st21.feature.strategy.simple.JsonStrategy import JsonStrategy
from app.asm2204.st21.feature.utils.CustomEncoder import CustomEncoder

bp = Blueprint('st0421',
               __name__,
               template_folder=os.getcwd() + "/app/templates/asm2204/st21/",
               static_folder=os.getcwd() + "/app/static/asm2204/st21/", )

@bp.before_request
def preHandler():
    if 'notebook' not in g:
        DBConfig.init_db()

        g.notebook = Notebook()
        g.notebook.set_strategy(JsonStrategy(DBConfig.get_notebook()[0]))
        g.notebook.init_notebook()


@bp.route("/api/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def main_api():
    note_types = {
        'NOTE': Note,
        'CREATURE': Creature
    }

    if request.method == 'GET':
        return json.dumps([note.__dict__ for note in g.notebook.get_notes()], cls=CustomEncoder)

    if request.method == 'POST':
        body = request.json

        note = note_types[body['type']](JsonStrategy(body))
        note.set_note()

        result = g.notebook.add_note(note)

        if result is None:
            return json.dumps(
                {
                    'message': 'Не удалось добавить'
                }), 400, {'ContentType': 'application/json'}
        else:
            return json.dumps(
                {
                    'message': f'Запись добавлена c ID={result}',
                }), 200, {'ContentType': 'application/json'}

    if request.method == 'PUT':
        body = request.json

        note = note_types[body['type']](JsonStrategy(body))
        note.set_note()

        result = g.notebook.edit_note(note)

        if result is None:
            return json.dumps(
                {
                    'message': 'Нет такой записи'
                }), 400, {'ContentType': 'application/json'}
        else:
            return json.dumps(
                {
                    'message': f'Заметка c ID={note.id} обновлена',
                }), 200, {'ContentType': 'application/json'}

    if request.method == 'DELETE':
        id = request.args.get('id')
        type = request.args.get('type')

        result = g.notebook.delete_note(id, type)

        if result is None:
            return json.dumps(
                {
                    'message': 'Нет такой записи'
                }), 400, {'ContentType': 'application/json'}
        else:
            return json.dumps(
                {
                    'message': f'Заметка c ID={id} удалена',
                    'html': render_template("/asm2204/st21/index.html", notes=g.notebook.get_notes())
                }), 200, {'ContentType': 'application/json'}


@bp.route("/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def main():
    note_types = {
        'NOTE': Note,
        'CREATURE': Creature
    }

    if request.method == 'GET':
        return render_template("/asm2204/st21/index.html", notes=g.notebook.get_notes())

    if request.method == 'POST':
        body = request.json

        note = note_types[body['type']](JsonStrategy(request.json))
        note.set_note()

        result = g.notebook.add_note(note)

        if result is None:
            return json.dumps(
                {
                    'message': 'Не удалось добавить'
                }), 400, {'ContentType': 'application/json'}
        else:
            return json.dumps(
                {
                    'message': f'Запись добавлена c ID={result}',
                    'html': render_template("/asm2204/st21/index.html", notes=g.notebook.get_notes())
                }), 200, {'ContentType': 'application/json'}

    if request.method == 'PUT':
        id = request.args.get('id')

        body = request.json

        note = note_types[body['type']](JsonStrategy(request.json))
        note.set_note()

        result = g.notebook.edit_note(note)

        if result is None:
            return json.dumps(
                {
                    'message': 'Нет такой записи'
                }), 400, {'ContentType': 'application/json'}
        else:
            return json.dumps(
                {
                    'message': f'Заметка c ID={id} обновлена',
                    'html': render_template("/asm2204/st21/index.html", notes=g.notebook.get_notes())
                }), 200, {'ContentType': 'application/json'}

    if request.method == 'DELETE':
        id = request.args.get('id')
        type = request.args.get('type')

        result = g.notebook.delete_note(id, type)

        if result is None:
            return json.dumps(
                {
                    'message': 'Нет такой записи'
                }), 400, {'ContentType': 'application/json'}
        else:
            return json.dumps(
                {
                    'message': f'Заметка c ID={id} удалена',
                    'html': render_template("/asm2204/st21/index.html", notes=g.notebook.get_notes())
                }), 200, {'ContentType': 'application/json'}


@bp.route("/load_from_file", methods=['GET'])
def get_fromfile():
    if request.method == 'GET':
        result = g.notebook.load_from_file()

        if result is None:
            return json.dumps(
                {
                    'message': 'Не удалось загрузить данные из файла'
                }), 400, {'ContentType': 'application/json'}
        else:
            return json.dumps(
                {
                    'message': f'Записи загружены из файла',
                    'html': render_template("/asm2204/st21/index.html", notes=g.notebook.get_notes())
                }), 200, {'ContentType': 'application/json'}


@bp.route("/api/load_from_file", methods=['GET'])
def get_fromfile_api():
    if request.method == 'GET':
        result = g.notebook.load_from_file()

        if result is None:
            return json.dumps(
                {
                    'message': 'Не удалось загрузить данные из файла'
                }), 400, {'ContentType': 'application/json'}
        else:
            return json.dumps(
                {
                    'message': f'Записи загружены из файла',
                }), 200, {'ContentType': 'application/json'}
