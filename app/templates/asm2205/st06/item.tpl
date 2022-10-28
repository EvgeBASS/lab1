Name: {{obj.firstname}}<br>
Last name: {{obj.lastname}}<br>
Age: {{obj.age}}<br>
Experience: {{obj.experience}}<br>
{% if obj.grade %}
	Grade: {{obj.grade}}<br>
{% endif %}
<a href="{{selfurl}}/form/{{obj.id}}">Edit</a>
<a href="{{selfurl}}/delete/{{obj.id}}">Delete</a>
<br><br>
