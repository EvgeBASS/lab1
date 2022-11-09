
<br>
NAME:   {{i.name}}<br>
RACE:   {{i.race}}<br>
Age:   {{i.age}}<br>
isAggressive:   {{i.isAggressive}}<br>
{% if i.isTrained %}
    isTrained:   {{i.isTrained}} <br>
{% endif %}
<a href="{{selfurl}}/kill/{{i.id}}">kill</a>
<a href="{{selfurl}}/edit/{{i.id}}">edit</a>