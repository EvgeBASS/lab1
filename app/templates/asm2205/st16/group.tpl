{% extends "asm2205/st16/base.tpl" %}

{% block content %}
    {% for obj in items %}
{% include "asm2205/st16/item.tpl" ignore missing %}
    {% else %}
Group is empty.<br>    
    {% endfor %}

{% include "asm2205/st16/add.tpl" ignore missing %}<br>
{% include "asm2205/st16/deleteAll.tpl" ignore missing %}
{% endblock %}