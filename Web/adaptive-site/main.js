const MenuBtn = document.querySelector('.menu');
const btn = document.querySelector('.post_btn');
const pop = document.querySelector('#popup');
let check = false;
let menuOpn = false;
MenuBtn.addEventListener('click',() =>{
  if(!menuOpn){
    MenuBtn.classList.toggle('_open');
    menuOpn = true;
  } else {
    MenuBtn.classList.remove('_open');
    menuOpn = false;
  }
})

btn.addEventListener('click',() =>{
  if(!check){
    popup.classList.toggle('logged');
    menuOpn = true;
  }
})
