{% extends "asm2205/st16/base.tpl" %}

{% block content %}

<form action = '{{selfurl}}/add' method=POST>

<input type=hidden name=id value={{it.id}}>
Name:<input type=text name=name value="{{it.name}}"><br>
Age:<input type=text name=age value={{it.age}}><br>
Rate:<input type=text name=rate value={{it.rate}}><br>
Stipend:<input type=text name=stipend value={{it.stipend}}><br>
Phone Number:<input type=hidden id="tel" name=phone_number value={{it.phone_number}} >
<br><input type=submit value="Ok">
<input type="checkbox" id="agree" onclick="myFunction()"> Head Student

<script>
function myFunction() {
  var checkBox = document.getElementById("agree");
  var text = document.getElementById("tel");
  if (checkBox.checked == true){
    text.type = text;
  } else {
     text.type = hidden;
  }
}
</script>
</form>

{% endblock %}