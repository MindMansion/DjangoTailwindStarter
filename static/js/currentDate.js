
var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
var n = new Date();
var y = n.getFullYear();
var m = n.getMonth();
var d = n.getDate();
// document.getElementById("date").innerHTML = d + " " + months[m] + " " + y;
document.getElementById("date").innerHTML = y;