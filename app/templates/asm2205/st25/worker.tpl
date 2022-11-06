Имя: {{obj.name}}<br>
Фамилия: {{obj.surname}}<br>
Кабинет: {{obj.cabinet}}<br>
{% if obj.post %}
	Зарплата : {{obj.salary}}<br>
	Стаж : {{obj.experience}}<br>
	Должность : {{obj.post}}<br>
{% endif %}
{% if obj.ganarar %}
	Премия: {{obj.ganarar}}<br>
{% endif %}
<a href="{{selfurl}}/init_form/{{obj.id}}">Редактировать</a>
<a href="{{selfurl}}/delete/{{obj.id}}">Удалить</a>
<br><br>
