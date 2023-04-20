/**************** Validacion formulario carga **************/

const formC = document.getElementById('formC');
const Buton = document.getElementById('submit-carga');

const Codigo = document.getElementById('Codigo');
const Fecha = document.getElementById('Fecha');
const Hora = document.getElementById('Hora');
const Sucursal = document.getElementById('Sucursales')
const Vehiculos = document.getElementById('Vehiculos');

const completar = {
    Codigos: false,
    Fechas: false,
    Horas: false,
    Vehiculoss: false,
    Sucursaless: false
}

formC.addEventListener('submit', (e) => {
	e.preventDefault();
    validarForm()
})    
    
Codigo.addEventListener('change', (e) => {
      if(e.target.value .length > 0) completar.Codigos = true

})

Fecha.addEventListener('change', (e) => {
    if(e.target.value.checked = 'true') completar.Fechas = true

})

Hora.addEventListener('change', (e) => {
    if(e.target.value.checked = 'true') completar.Horas = true

})

Vehiculos.addEventListener('change', (e) => {
    if(e.target.checked = 'true') completar.Vehiculoss = true

})

Sucursales.addEventListener('change', (e) => {
    if(e.target.checked = 'true') completar.Sucursaless = true

})

const validarForm = () => {
    const formVal = Object.values(completar)
    const valid = formVal.findIndex(value => value == false)
    if (valid == -1) formC.reset()
    else alert("Debes llenar todos los campos");
}

/*********************  Validacion formulario descarga  *************************** */

const formD = document.getElementById('formD');
const buton = document.getElementById('submitLlegada');

const codigo = document.getElementById('codigo');
const fecha = document.getElementById('fecha');
const hora = document.getElementById('hora');
const sucursal = document.getElementById('sucursales')
const vehiculos = document.getElementById('vehiculos');

const campos = {
    codigo: false,
    fecha: false,
    hora: false,
    vehiculos: false,
    sucursales: false
}

formD.addEventListener('submit', (e) => {
	e.preventDefault();
    validateForm()
})    
    
codigo.addEventListener('change', (e) => {
      if(e.target.value .length > 0) campos.codigo = true

})

fecha.addEventListener('change', (e) => {
    if(e.target.value.checked = 'true') campos.fecha = true

})

hora.addEventListener('change', (e) => {
    if(e.target.value.checked = 'true') campos.hora = true

})

vehiculos.addEventListener('change', (e) => {
    if(e.target.checked = 'true') campos.vehiculos = true

})

sucursales.addEventListener('change', (e) => {
    if(e.target.checked = 'true') campos.sucursales = true

})

const validateForm = () => {
    const formVal = Object.values(campos)
    const valid = formVal.findIndex(value => value == false)
    if (valid == -1) formD.reset() 
    else alert("Debes llenar todos los campos");
}

/****************** Validacion formulario retiro  *********************/
const formR = document.getElementById('formR');
const butonR = document.getElementById('submit-retiro');
const cod = document.getElementById('retiro')

const llenar = {
    cod : false
}

formR.addEventListener('submit', (e) => {
	e.preventDefault();
    validateFormR()
}) 

cod.addEventListener('change', (e) => {
    if(e.target.value .length > 5) llenar.cod = true

})

const validateFormR = () => {
    const formVal = Object.values(llenar)
    const valid = formVal.findIndex(value => value == false)
    if (valid == -1) formR.reset()
    else alert("El codigo debe tener un minimo de 6 caracteres");
}