var price = prompt("Сумма:");
var years = prompt("Годы:");
var procent = prompt("Процент:");


for(var i = 1; i<years; i++){
  price *= 1 + procent/100;
  console.log(i + "year - " + Math.round(price));
}

console.log("После" + (i - 1) + "лет сумма будет -" + Math.round(price*(1 + procent/100)));
