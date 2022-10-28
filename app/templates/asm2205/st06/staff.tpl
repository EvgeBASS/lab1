{% extends "asm2205/st06/base.tpl" %}

{% block content %}
    {% for obj in items %}
{% include "asm2205/st06/item.tpl" ignore missing %}
    {% else %}
Staff is empty<br>    
    {% endfor %}

<a href='{{selfurl}}/form/0'>Add trainer</a>
<a href='{{selfurl}}/clear'>Clear staff</a>
{% endblock %}