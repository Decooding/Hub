var even = 0;
var odd = 0;

console.log("Input digit:");

var user_num = prompt("specify digit");

while(user_num>0){
  if(user_num % 2 == 0)
    even += 1;
  else
    odd +=1; 
    user_num = Math.floor(user_num/10);

}

console.log("Chetnyi: " + even);
console.log("Not Chetnyi: " + odd);
