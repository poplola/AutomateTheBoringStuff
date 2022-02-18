# Javascript String Reference : https://www.w3schools.com/jsref/jsref_obj_string.asp

# // 8. switch 
switch (text){
    case "red":
        document.getElementById("header").style.color = "red";
        break;
    case "blue":
        document.getElementById("header").style.color = "blue";
        break;   
    case "green":
        document.getElementById("header").style.color = "green";
        break;     
    default:
        document.getElementById("header").style.color = "black";
        break;                       

# // 8. parseInt() is to transfer string to int.
var text = parseInt(document.getElementById("inp").value);                        