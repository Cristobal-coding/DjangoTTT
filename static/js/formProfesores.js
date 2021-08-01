var rut=document.getElementById('rut');
var nombre=document.getElementById('nombre');
var paterno=document.getElementById('paterno');
var materno=document.getElementById('materno');
var error=document.getElementById('error');
error.style.color ='red';
function enviarForm(){
    var mensajesError = [];
    console.log('Enviando Form...')
    if(nombre.value === null || nombre.value ===''){
        mensajesError.push('Ingrese un nombre');
    }
    if(rut.value === null || rut.value ===''){
        mensajesError.push('Ingrese un rut');
    }
    error.innerHTML=mensajesError.join(', ');
    return false;
}
