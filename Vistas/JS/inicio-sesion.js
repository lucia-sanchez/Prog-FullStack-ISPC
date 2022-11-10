const usuariosValidos= [{usuario:'33.545.898',
                        password:'12345678' },

                        {usuario:'25.464.878',
                         password:'12345677' },

                        {usuario:'35.698.654',
                        password:'12345677'}, 

                        {usuario:'20.656.471',
                        password:'12345677'},

                        {usuario:'34.216.873',
                        password:'12345677'}];
//PARA VALIDAR SI EL USUARIO EXISTE DEBERIA BUSCARLO EN LA BASE DE DATOS
//COMO AÚN NO ESTA CONECTADA, LO BUSCA DENTRO DEL ARRAY DE USUARIOS VALIDOS

const usuario = document.getElementById('usuario');
const password = document.getElementById('password');
const form = document.getElementById('form');
const errorUsuario = document.getElementById('errorUsuario');
const errorPassword = document.getElementById('errorPassword');
const errorGeneral = document.getElementById('errorGeneral');
const success = document.getElementById('success');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    validarEmpty(usuario.value, usuario, errorUsuario, 'usuario');
    validarEmpty(password.value, password, errorPassword, 'contraseña');
    if(validarUsuario()){
        success.innerHTML = `<p class = "success"> Ingreso exitoso! </p>`;
    }else if (usuario.value.length != 0 && password.value.length != 0){
        errorGeneral.innerHTML = `<p class = "error">⚠ El usuario o contraseña ingresados son incorrectos</p>`;
    }
});
    function validarEmpty(valueInput, divInput, divError, nameInput){
        if(valueInput.length == 0){
            showError(divInput, divError, nameInput);     
        }else{
            hideError(divInput, divError);
        }
    }
function showError(divInput, divError, nameInput){
    divInput.style.border = '1px solid red';
    divError.innerHTML = `<p class = "error">⚠ Ingrese su ${nameInput}</p>`;
}
function hideError(divInput, divError){
    divInput.style.border = '1px solid black';
    divError.innerHTML = ``;
    
} 
function validarUsuario(){
    let usuarioValido = false;
    for(let i = 0; i < usuariosValidos.length; i++){
        if(usuario.value == usuariosValidos[i].usuario && password.value == usuariosValidos[i].password){
            usuarioValido = true;
        }
    }
    return usuarioValido;
}
