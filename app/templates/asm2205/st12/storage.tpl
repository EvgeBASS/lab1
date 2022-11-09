{% extends "asm2205/st12/base.tpl" %}
{% block content %}
{% include "asm2205/st12/form.tpl" ignore missing %}
    {% for i in items %}
        {% include "asm2205/st12/entity.tpl" ignore missing %}
    {% else %}
        <label>
            Nothing HERE
        </label>
    {% endfor %}
{% endblock %}