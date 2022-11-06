{% extends "asm2205/st24/base.tpl" %}

{% block content %}
<h2>{{it.Show()}}</h2>

<form action = '{{selfurl}}/add' method=POST>
<input type=hidden name=id value={{it.id}}>
Имя:<input type=text name=name value={{it.name}}><br>
Возраст:<input type=numeric name=age value={{it.age}}><br>
Зарплата:<input type=numeric name=salary value={{it.salary}}><br>
<br>
Данные для пилота<br>
<br>
Должность:<input type=text name=subject value={{it.subject}}><br>

<br><input type=submit name="Worker" value="Сделать работника">
<br><input type=submit name="Pilot" value="Сделать пилота">
</form>

{% endblock %}