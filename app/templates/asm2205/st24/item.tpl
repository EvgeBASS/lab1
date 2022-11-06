Имя: {{it.name}}<br>
Возраст: {{it.age}}<br>
Зарплата: {{it.salary}}<br>
{% if it.__class__.__name__ == "Pilot" %}
    Должность: {{it.subject}}<br>
{% endif %}
<a href="{{selfurl}}/showform/{{it.id}}">Edit</a>
<a href="{{selfurl}}/delete/{{it.id}}">Delete</a>
<br><br>