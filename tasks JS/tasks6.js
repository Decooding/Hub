var cars = ["Audi", "Volvo", "BMW", "Mercedes"];
console.log(cars.join(', '));
console.log(cars.toString());
console.log(cars.join());
var arr = [ "a,b,c", "d", "e" ];

var abc = arr.splice(0,1);
var abc2Arr = abc.toString().split(',');

var res = abc2Arr.concat(arr);
console.log(res);