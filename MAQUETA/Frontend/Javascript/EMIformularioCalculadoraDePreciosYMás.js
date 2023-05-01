let peso = document.getElementById("peso")
let DNI = document.getElementById("DNI")
let DNI2 = document.getElementById("DNI2")
let precio = document.getElementById("precio")
let contador;
let contador2;
let contador3;

peso.addEventListener('keypress', (event) => {
    event.preventDefault()
    peso.value = peso.value.substring(0, 2) 
    
    let codigoKey = event.keyCode 
    let valorKey = String.fromCharCode(codigoKey)
     console.log(valorKey)
    
    let valor = parseInt(valorKey) 
    
    if(valor) {peso.value += valor}
    else if (valor || valorKey === "0") { (peso.value += valor);
    }
    
})

DNI.addEventListener('keypress', (event) => {
    event.preventDefault()
    DNI.value = DNI.value.substring(0, 7) 
    
    let codigoKey = event.keyCode 
    let valorKey = String.fromCharCode(codigoKey)
     console.log(valorKey)
    
    let valor = parseInt(valorKey) 
    
    if(valor) {DNI.value += valor}
    else if (valor || valorKey === "0") { (DNI.value += valor);
    }
    
})

DNI2.addEventListener('keypress', (event) => {
    event.preventDefault()
    DNI2.value = DNI2.value.substring(0, 7) 
    
    let codigoKey = event.keyCode 
    let valorKey = String.fromCharCode(codigoKey)
     console.log(valorKey)
    
    let valor = parseInt(valorKey) 
    
    if(valor) {DNI2.value += valor}
    else if (valor || valorKey === "0") { (DNI2.value += valor);
    }
    
})

function enviarCalculo(){

    contador = 0
    contador = peso.value.length
    if (contador == 0){
        peso.value=""
        peso.placeholder="¡Vacio! Pon hasta 3 dígitos"
        precio.placeholder="Error"
        return false;}

    else {
        peso.value =""
        peso.placeholder="Peso kg"
        precio.placeholder="Calculando"
        console.log('Calculando');
        return false;}
}

function enviarRegistro(){
    
    contador = 0
    contador2 = 0
    contador3 = 0
    contador = peso.value.length
    contador2 = DNI.value.length
    contador3 = DNI2.value.length

    if (contador != 0 && contador2 == 8 && contador3 == 8){
        DNI.value = ""
        DNI2.value = ""
        peso.value = ""
        DNI.placeholder = "DNI destinatario"
        DNI2.placeholder = "DNI remitente"
        peso.placeholder = "Peso kg"
        console.log('Enviando Registro');
        return false;}
    else if (contador == 0 && contador2 == 8 && contador3 == 8){
        peso.value=""
        peso.placeholder="¡Vacio! Pon hasta 3 dígitos"
        console.log('Algo salió mal');
        return false;}

    else if (contador != 0 && contador2 == 0 && contador3 == 0){
        DNI.value=""
        DNI.placeholder="¡Vacio! Pon 8 dígtos"
        DNI2.value=""
        DNI2.placeholder="¡Vacio! Pon 8 dígtos"
        console.log('Algo salió mal');
        return false;}
    else if (contador == 0 && contador2 == 0 && contador3 == 0){
        peso.value=""
        peso.placeholder="¡Vacio! Pon hasta 3 dígitos"
        DNI.value=""
        DNI.placeholder="¡Vacio! Pon 8 dígtos"
        DNI2.value=""
        DNI2.placeholder="¡Vacio! Pon 8 dígtos"
        console.log('Algo salió mal');
        return false;}

    else if (contador != 0 && contador2 == 8 && contador3 == 0){
        DNI2.value=""
        DNI2.placeholder="¡Vacio! Pon 8 dígtos"
        console.log('Algo salió mal');
        return false;}
    else if (contador == 0 && contador2 == 8 && contador3 == 0){
        peso.value=""
        peso.placeholder="¡Vacio! Pon hasta 3 dígitos"
        DNI2.value=""
        DNI2.placeholder="¡Vacio! Pon 8 dígtos"
        console.log('Algo salió mal');
        return false;}
    else if (contador != 0 && contador2 == 0 && contador3 == 8){
        DNI.value=""
        DNI.placeholder="¡Vacio! Pon 8 dígtos"
        console.log('Algo salió mal');
        return false;}
    else if (contador == 0 && contador2 == 0 && contador3 == 8){
        DNI.value=""
        DNI.placeholder="¡Vacio! Pon 8 dígtos"
        peso.value=""
        peso.placeholder="¡Vacio! Pon hasta 3 dígitos"
        console.log('Algo salió mal');
        return false;}

    else if (contador != 0 && contador2 == 0 && contador3 < 8){
        DNI.value=""
        DNI.placeholder="¡Vacio! Pon 8 dígtos"
        DNI2.value=""
        DNI2.placeholder="Pon 8 dígtos"
        console.log('Algo salió mal');
        return false;}
    else if (contador == 0 && contador2 == 0 && contador3 < 8){
        peso.value=""
        peso.placeholder="¡Vacio! Pon hasta 3 dígitos"
        DNI.value=""
        DNI.placeholder="¡Vacio! Pon 8 dígtos"
        DNI2.value=""
        DNI2.placeholder="Pon 8 dígtos"
        console.log('Algo salió mal');
        return false;}
    else if (contador != 0 && contador2 < 8 && contador3 == 0){
        DNI.value=""
        DNI.placeholder="Pon 8 dígtos"
        DNI2.value=""
        DNI2.placeholder="¡Vacio! Pon 8 dígtos"
        console.log('Algo salió mal');
        return false;}
    else if (contador == 0 && contador2 < 8 && contador3 == 0){
        peso.value=""
        peso.placeholder="¡Vacio! Pon hasta 3 dígitos"
        DNI.value=""
        DNI.placeholder="Pon 8 dígtos"
        DNI2.value=""
        DNI2.placeholder="¡Vacio! Pon 8 dígtos"
        console.log('Algo salió mal');
        return false;}

    else if (contador != 0 && contador2 == 8 && contador3 < 8){
        DNI2.value=""
        DNI2.placeholder="Pon 8 dígtos"
        console.log('Algo salió mal');
        return false;}
    else if (contador == 0 && contador2 == 8 && contador3 < 8){
        peso.value=""
        peso.placeholder="¡Vacio! Pon hasta 3 dígitos"
        DNI2.value=""
        DNI2.placeholder="Pon 8 dígtos"
        console.log('Algo salió mal');
        return false;}
    else if (contador != 0 && contador2 < 8 && contador3 == 8){
        DNI.value=""
        DNI.placeholder="Pon 8 dígtos"
        console.log('Algo salió mal');
        return false;}
    else if (contador == 0 && contador2 < 8 && contador3 == 8){
        peso.value=""
        peso.placeholder="¡Vacio! Pon hasta 3 dígitos"
        DNI.value=""
        DNI.placeholder="Pon 8 dígtos"
        console.log('Algo salió mal');
        return false;}    

    else if (contador != 0 && contador2 < 8 && contador3 < 8){
        DNI.value=""
        DNI.placeholder="Pon 8 dígtos"
        DNI2.value=""
        DNI2.placeholder="Pon 8 dígtos"
        console.log('Algo salió mal');
        return false;}
    else if (contador == 0 && contador2 < 8 && contador3 < 8){
        peso.value=""
        peso.placeholder="¡Vacio! Pon hasta 3 dígitos"
        DNI.value=""
        DNI.placeholder="Pon 8 dígtos"
        DNI2.value=""
        DNI2.placeholder="Pon 8 dígtos"
        console.log('Algo salió mal');
        return false;} 
}