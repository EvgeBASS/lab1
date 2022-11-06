{% extends "asm2205/st25/base.tpl" %}

{% block content %}
    {% for obj in items %}
{% include "asm2205/st25/worker.tpl" ignore missing %}
    {% else %}
Персонал не найден<br>
    {% endfor %}

<a href='{{selfurl}}/init_form/0'>Добавить сотрудника</a>

{% endblock %}