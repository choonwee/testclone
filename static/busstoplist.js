var func =function(){
    for (var i = 0; i < rows.length; i++) {
        var c = rows[i].className;
        if(i==index%11){
            rows[i].className="red";
        } else {
            rows[i].className="";
        }
    }
    index++;
}

$('#btn').click(function(){
    setInterval(func, 2000);
});