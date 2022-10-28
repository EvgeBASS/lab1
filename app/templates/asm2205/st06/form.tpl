{% extends "asm2205/st06/base.tpl" %}

{% block content %}

<form action = '{{selfurl}}/add' method=POST>

<script>
function SetGrade() {
  var checkBox = document.getElementById("agree");
  var text = document.getElementById("grade");
  if (checkBox.checked == true){
    text.readOnly = 0;
  } else {
     text.readOnly = 1;
  }
}
</script>

<input type=hidden name=id value={{it.id}}>
Name:<input type=text name=firstname required value="{{it.firstname}}"><br>
Last name:<input type=text name=lastname required value="{{it.lastname}}"><br>
Age:<input type=text name=age required value={{it.age}}><br>
Experience<input type=text name=experience required value={{it.experience}}><br>
Grade:<input type=text readonly id="grade" name=grade value={{it.grade}} >
<input type="checkbox" id="agree" onclick="SetGrade()"> Master?
<br><input type=submit value="Ok">
</form>

{% endblock %}