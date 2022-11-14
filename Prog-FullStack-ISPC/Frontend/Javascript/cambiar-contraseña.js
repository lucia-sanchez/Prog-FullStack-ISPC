let usuariosPermitidos = ['33.545.898','25.464.878','35.698.654','20.656.471','34.216.873'];
                
//PARA VALIDAR SI EL USUARIO EXISTE DEBERIA BUSCARLO EN LA BASE DE DATOS
//COMO AÚN NO ESTA CONECTADA, LO BUSCA DENTRO DEL ARRAY DE USUARIOS VALIDOS

const user = document.getElementById('id-usuario');
const mail = document.getElementById('mail');
const userError = document.getElementById('userError');
const mensaje = document.getElementById('mensaje');
const ingresar = document.getElementById('ingresar');

ingresar.addEventListener('submit', (e) => {
    e.preventDefault();
    validarEmpty(user.value, user, userError, 'usuario');
    validarEmpty(mail.value, mail, mensaje, 'mail');
    validarUsuario(user.value);
    validarMail(mail.value);
    if(validarUser()){
        mensaje.innerHTML = ``;
    }else if (user.value.length != 0){
        userError.innerHTML = `<p class = "error">⚠ El usuario ingresado es incorrecto</p>`;
    }
    if(validarMail(mail.value) && validarUser()){
        mensaje.innerHTML = `<p class= "success"> Se ha enviado un e-mail para restablecer su contaseña</p>`;
    }
    else{
        mensaje.innerHTML = `<p class = "error">⚠ El mail ingresado es incorrecto</p>`;
    }
}); 
function validarEmpty(valueInput, divInput, divError, nameInput){
    if(valueInput.length === 0){
        showError(divInput, divError, nameInput);     
    }else{
        hideError(divInput, divError);
    }
}
/*function validarMail(mail){
    let expReg = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    let esValido = expReg.test(mail);
    if(esValido){
        return true;

    }
}*/
function validarMail( email ) 
{
    let regex = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email) ? true : false;
}

function showError(divInput, divError, nameInput){
divInput.style.border = '1px solid red';
divError.innerHTML = `<p class = "error">⚠ Ingrese su ${nameInput}</p>`;
}

function hideError(divInput, divError){
divInput.style.border = '1px solid black';
divError.innerHTML = ``;

} 
function validarUser(){
    let usuarioValido = false;
    for(let i = 0; i < usuariosPermitidos.length; i++){
        if(user.value == usuariosPermitidos[i]){
            usuarioValido = true;
        }
    }
    return usuarioValido;
}


