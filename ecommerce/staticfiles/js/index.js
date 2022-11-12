// hamburger menu 

let hamburger = document.querySelector('.hamburger');
const navLink = document.querySelector('.nav-link');
const crossIcon = document.querySelector('.cross-icon')

if(hamburger) {
    hamburger.addEventListener('click', (e) => {
        navLink.style.display = 'block';
    });
};

if(crossIcon) {
    crossIcon.addEventListener('click', (a) => {
        navLink.style.display = 'none';
    });
};

// signup page validation

const form = document.getElementById('form');
const email = document.getElementById('email');
const password = document.getElementById('password');
const repeatPassword = document.getElementById('repeatPassword');
const checkbox = document.getElementById('checkbox');
const emailValidation = document.getElementById('emailValidation');
const passwordStrnth = document.getElementById('passwordStrnth');
const matchPassword = document.getElementById('matchPassword');
const sumbitBtn = document.getElementById('submit');

form.addEventListener('submit', (e) => {
    e.preventDefault();
   
});
email.addEventListener('keypress', (event) => {
    let emailValue = event.target.value;
    if(emailValue) {
        
    } else{
        emailValidation.innerHTML = 'email can\'t be empty';
    }
});
