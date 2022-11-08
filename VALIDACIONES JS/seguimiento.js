/*SE UTILIZA UN ARRAY CON LOS CODIGOS DE ENVIO PARA ACCEDER A ELLOS. 
CUANDO SE CONECTE A LA BASE DE DATOS INGRESARÁ ALLÍ PARA BUSCARLOS.*/
const codigoEnvios = [360000641975900,  360000641975901,  360000641975902,  360000641975903,  360000641975900];

let fecha = new Date();
//capturamos los elementos y los guardamos en una constante
const seguimiento = document.querySelector("[name=seguimiento]");
const buscar = document.getElementById("buscar");
const errorCodigo = document.getElementById("errorCodigo");
const detalleEnvio = document.querySelector("#detalleEnvio");


//creamos un evento de escucha, que se activa al salir del campo
seguimiento.addEventListener("blur", (e) => {
    e.preventDefault();
    let codigo = seguimiento.value;
    validarCodigo(codigo, errorCodigo);
    if (validarCodigo()){
        showError(seguimiento, detalleEnvio);
    }else{
        hideError(seguimiento, detalleEnvio);
    }
    
});
    //validamos que solo ingresen numeros y sean 15 caracteres
    function validarCodigo (divInput, divError){
     if(divInput.length === 0){
        divError.innerHTML= `<p class = "error">Debes ingresar el número de seguimiento</p>`;
    }
    else if(divInput !== isNaN && divInput.length !== 15){
        divError.innerHTML= `<p class = "error">⚠ El código ingresado es incorrecto</p>`;
    }
}
buscar.addEventListener("click", (e) => {
    e.preventDefault();
    if(validarExistencia()){
        showError(seguimiento, detalleEnvio);
    }else{
        hideError(seguimiento, detalleEnvio);
    }
});
function showError(divInput,divError){
    divInput.style.border = '1px solid red';
    divError.innerHTML = `<p class = "error">El paquete se encuentra en el centro de distribución</p>`;
}
function hideError(divInput,divError){
    divInput.style.border = '1px solid black';
    divError.innerHTML = `<p class = "error">⚠ El paquete no se encuentra en nuestro sistema</p>`;
}
function validarExistencia(){
    let codigoValido = false;
    for(let i = 0; i < codigoEnvios.length; i++){
        if(seguimiento.value === codigoEnvios[i] ){
            usuarioValido = true;
        }
    }
    return codigoValido;
}