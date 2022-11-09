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
