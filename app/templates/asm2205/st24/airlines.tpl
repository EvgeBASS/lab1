{% extends "asm2205/st24/base.tpl" %}

{% block content %}
    {% for it in items %}
        {% include "asm2205/st24/item.tpl"%}
    {% else %}
        авиакомпании пусты
    {% endfor %}

{% include "asm2205/st24/add.tpl"%}
{% endblock %}