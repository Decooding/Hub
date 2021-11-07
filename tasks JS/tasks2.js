var num = prompt("Введите число с 4 цифрами:");

var n1 = Math.floor(num/1000%10);
var n2 = Math.floor(num/100%10);
var n3 = Math.floor(num/10%10);
var n4 = Math.floor(num%10);

console.log(n1 + ", " + n2 + ", " + n3 + ", " + n4);