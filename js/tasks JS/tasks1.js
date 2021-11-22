var today = new Date();
var day = today.getDate();
var month = today.getMonth();
var year = today.getFullYear();

if(day<10)
  day = '0' + day

today = 'Дата и время: ' + month + '-' + day + '-' + year
console.log(today)
