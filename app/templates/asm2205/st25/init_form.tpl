{% extends "asm2205/st25/base.tpl" %}

{% block content %}

<form action = '{{selfurl}}/add' method=POST>

<script>
function choice() {

    if(document.getElementById("doctor").checked == true) {
    document.getElementById("salary").disabled=0
    document.getElementById("experience").disabled=0
    document.getElementById("post").disabled=0
    document.getElementById("ganarar").disabled=1
    }

    else if(document.getElementById("headDoctor").checked == true) {
    document.getElementById("salary").disabled=0
    document.getElementById("experience").disabled=0
    document.getElementById("post").disabled=0
    document.getElementById("ganarar").disabled=0
    }

    else{
    document.getElementById("salary").disabled=1
    document.getElementById("experience").disabled=1
    document.getElementById("p").disabled=1
    document.getElementById("g").disabled=1
    }

    }

</script>

<input type="radio" name="worker" checked onclick="choice()"> Медсестра
<input type="radio" name="worker" id="doctor"  onclick="choice()"> Доктор
<input type="radio" name="worker" id="headDoctor"  onclick="choice()"> Главный доктор
<br><input type=hidden name=id value={{it.id}}>
<br>Имя:<input type=text name=name  required value="{{it.name}}"><br>
Фамилия:<input type=text  name=surname  required value="{{it.surname}}"><br>
Кабинет:<input type=text name=cabinet  required value={{it.cabinet}}><br>
Зарплата: <input type=text name=salary disabled id="salary" value={{it.salary}}><br>
Стаж: <input type=text name=experience disabled id="experience" value={{it.experience}}><br>
Должность: <input type=text  disabled id="post" name="post" value={{it.post}} ><br>
Премия: <input type=text disabled id="ganarar" name="ganarar" value={{it.ganarar}} ><br>
<br><input type=submit value="Подтвердить">
</form>

{% endblock %}