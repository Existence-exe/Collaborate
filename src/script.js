const signup = document.getElementById('content-signup');
const login = document.getElementById('content-login');
const signupBtn = document.getElementById('switch-signup');
const loginBtn = document.getElementById('switch-login');
var view = 'signup';
var marginSignup = 5;
var marginLogin = 5;

function switchSignup(){
    view = 'signup';
    signupBtn.style.borderBottom = '2.5px solid rgb(24, 126, 221)';
    loginBtn.style.borderWidth = '0px';
}

function switchLogin(){
    view = 'login';
    loginBtn.style.borderBottom = '2.5px solid rgb(24, 126, 221)';
    signupBtn.style.borderWidth = '0px';
}

setInterval(function(){
    if(view == 'login'){
        if(marginSignup != -105){
            signup.style.marginLeft = marginSignup + '%';
            marginSignup -= 5;
            signup.style.marginRight = '105%';
        }

        if(marginLogin != -100){
            login.style.marginLeft = marginLogin + '%';
            marginLogin -= 5;
            login.style.marginRight = '105%';
        }
    }
}, 1);

setInterval(function(){
    if(view == 'signup'){
        if(marginSignup != 10){
            signup.style.marginLeft = marginSignup + '%';
            marginSignup += 5;
            signup.style.marginRight = '5%';
        }

        if(marginLogin != 10){
            login.style.marginLeft = marginLogin + '%';
            marginLogin += 5;
            login.style.marginRight = '5%';
        }
    }
}, 1);

const container = document.getElementById('container');
const colors = ['#e6f5ff', '#99d6ff', '#33adff', '#008ae6', '#005c99', '#002e4d', '#4db5ff'];

setInterval(function(){
    x = Math.floor(Math.random() * window.innerWidth);
    y = Math.floor(Math.random() * window.innerHeight);
    color = colors[Math.floor(Math.random() * 7)];

    elem = document.createElement('DIV');
    elem.className = 'circle';
    elem.style.position = 'fixed';
    elem.style.display = 'block';
    elem.style.width = '1px';
    elem.style.height = '1px';
    elem.style.marginLeft = x + 'px';
    elem.style.marginTop = y + 'px';
    elem.style.backgroundColor = color;
    elem.style.borderRadius = '50%';
    elem.style.opacity = '0.8';

    container.appendChild(elem);
}, 200);

setInterval(function(){
    circles = document.getElementsByClassName('circle');

    for(let i = 0; i < circles.length; i++){
        elem = circles[i];
        elem.style.opacity = String(parseFloat(elem.style.opacity) - 0.05);
        elem.style.width = String(parseFloat(elem.style.width.slice(0, -2)) + 10.0) + 'px';
        elem.style.height = String(parseFloat(elem.style.height.slice(0, -2)) + 10.0) + 'px';
        elem.style.marginLeft = String(parseFloat(elem.style.marginLeft.slice(0, -2)) - 5.0) + 'px';
        elem.style.marginTop = String(parseFloat(elem.style.marginTop.slice(0, -2)) - 5.0) + 'px';

        if(parseFloat(elem.style.opacity) < 0.1){
            elem.remove();
        }
    }
}, 50);