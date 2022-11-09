    <form  action = '{{selfurl}}/add' method=POST>
        <input type=hidden name=id value={{object.id}}>
        <div><label>NAME:</label><input type=text name=name required value={{object.name}}></div><br>
        <div><label>RACE:</label><input type=text name=race required value={{object.race}}></div><br>
        <div><label">AGE:</label><input type=text name=age required value={{object.age}}></div><br>
        <div><label>AGGRESSIVE?:</label><input type=text name=isAggressive required value={{object.isAggressive}}></div><br>
        <div><label>TRAINED?:</label><input type=text name=isTrained value={{object.isTrained}}></div><br>
        <br><input type=submit name="tap" value="CREATE AS Wolf"><br>
        <br><input type=submit name="tap" value="CREATE AS Dog">
    </form>
