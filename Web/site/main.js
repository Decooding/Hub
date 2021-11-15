const MenuBtn = document.querySelector('.menu');
const log = document.querySelector('.login');
let menuOpn = false;
let rec = false;
MenuBtn.addEventListener('click',() =>{
  if(!menuOpn){
    MenuBtn.classList.toggle('_open');
    menuOpn = true;
  } else {
    MenuBtn.classList.remove('_open');
    menuOpn = false;
  }
})
log.addEventListener('click', () =>{
  if(!rec){
    log.classList.toggle('log_clk');
    rec = true;
  } else{
    log.classList.remove('log_clk');
    rec = false;
  }
})
