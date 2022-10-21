Name: {{obj.name}}<br>
Age: {{obj.age}}<br>
Rate: {{obj.rate}}<br>
Stipend: {{obj.stipend}}<br>
{% if obj.phone_number %}
	Phone Number: {{obj.phone_number}}<br>
{% endif %}
<a href="{{selfurl}}/showform/{{obj.id}}">Edit</a>
<a href="{{selfurl}}/delete/{{obj.id}}">Delete</a>
<br><br>
