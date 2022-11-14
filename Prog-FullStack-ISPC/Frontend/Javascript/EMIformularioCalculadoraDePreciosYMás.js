let peso = document.getElementById("peso")
let DNI = document.getElementById("DNI")
let DNI2 = document.getElementById("DNI2")

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
    console.log('Calculando');
    return false;
}

function enviarRegistro(){
    console.log('Enviando Registro');
    return false;
}