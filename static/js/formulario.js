const formulario = document.getElementById('formalumno');
const inputs=document.querySelectorAll('#formalumno input');
const expresiones = {
 
    telefono:/[0-9]{8}/
}
var Fn = {
	// Valida el rut con su cadena completa "XXXXXXXX-X"
	validaRut : function (rutCompleto) {
		if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test( rutCompleto ))
			return false;
		var tmp 	= rutCompleto.split('-');
		var digv	= tmp[1]; 
		var rut 	= tmp[0];
		if ( digv == 'K' ) digv = 'k' ;
		return (Fn.dv(rut) == digv );
	},
	dv : function(T){
		var M=0,S=1;
		for(;T;T=Math.floor(T/10))
			S=(S+T%10*(9-M++%6))%11;
		return S?S-1:'k';
	}
}

const validarFormularioReact= (e) =>{
    switch (e.target.name){
        case"rut":
            if (Fn.validaRut((e.target.value))){
                document.getElementById('id_rut').classList.remove('is-invalid')
            } else {
                document.getElementById('id_rut').classList.add('is-invalid')
            }      
        break;
       

        case"telefono":
        if(e.target.value){
            if (expresiones.telefono.test(e.target.value)){
                document.getElementById('id_telefono').classList.remove('is-invalid')
            }else{
                document.getElementById('id_telefono').classList.add('is-invalid')
            }
            break;
        }else{
            document.getElementById('id_telefono').classList.remove('is-invalid')
        }
        break;
    }
}
inputs.forEach((input)=>{
    input.addEventListener('keyup', validarFormularioReact)

    input.addEventListener('blur',validarFormularioReact)
    input.addEventListener('change',validarFormularioReact)
    
})
function validateForm1() {
    //Registrar alumno
    console.log("validateform1 registalumn ");

    var inputss = document.getElementById("formalumno").elements;
    var rut =inputss[1];
    var nombre =inputss[2];
    var paterno =inputss[3];
    var materno =inputss[4];
    var genero =inputss[5];
    var curso =inputss[6];
    var apod =inputss[7];
    var cel =inputss[9];
    var fecha =inputss[10];
    console.log(inputss);    

    var errores = 0 ;
    if (rut.value == ""|| rut.value==null) {
        console.log("rut vacio");
        rut.classList.add('is-invalid');
        errores= errores+1;
    }else{
        rut.classList.remove('is-invalid');
    }
    if(Fn.validaRut((rut.value))){
        rut.classList.remove('is-invalid');
    }else{
        rut.classList.add('is-invalid'); 
        errores= errores+1;
 
    }
    if (nombre.value == ""|| nombre.value==null) {
        console.log("nombre vacio");
        nombre.classList.add('is-invalid');
        errores= errores+1;
    }else{
        nombre.classList.remove('is-invalid');
    }
    if (paterno.value == ""|| paterno.value==null) {
        console.log("paterno vacio");
        paterno.classList.add('is-invalid');
        errores= errores+1;
    }else{
        paterno.classList.remove('is-invalid');
    }
    if (materno.value == ""|| materno.value==null) {
        console.log("materno vacio");
        materno.classList.add('is-invalid');
        errores= errores+1;
    }else{
        materno.classList.remove('is-invalid');
    }
    if (genero.value == ""|| genero.value==null) {
        console.log("genero vacio");
        genero.classList.add('is-invalid');
        errores= errores+1;
    }else{
        genero.classList.remove('is-invalid');
    }
    if (curso.value == ""|| curso.value==null) {
        console.log("curso vacio");
        curso.classList.add('is-invalid');
        errores= errores+1;
    }else{
        curso.classList.remove('is-invalid');
    }
    if (apod.value == ""|| apod.value==null) {
        console.log("apod vacio");
        apod.classList.add('is-invalid');
        errores= errores+1;
    }else{
        apod.classList.remove('is-invalid');
    }
    if (expresiones.telefono.test(cel.value)){
        cel.classList.remove('is-invalid')
    }else{
        if (cel.value==""){ 
            cel.classList.remove('is-invalid')
        }else{
            console.log("Error teleofono")
            cel.classList.add('is-invalid')
            errores= errores+1;
        }
        
    }
    if (fecha.value == ""|| fecha.value==null) {
        console.log("fecha vacio");
        fecha.classList.add('is-invalid');
        errores= errores+1;
    }else{
        fecha.classList.remove('is-invalid');
    }
    if(errores!=0){   
        console.log("Error lol");
        erroresdiv.classList.remove('d-none');
        return false;
    }else{      
        erroresdiv.classList.add('d-none');
    }       
    
} 
function validateForm2() {
    console.log("validateform2 editalumnd")
    var inputss = document.getElementById("formalumno").elements;
    var nombre =inputss[1];
    var paterno =inputss[2];
    var materno =inputss[3];
    var genero =inputss[4];
    var apod =inputss[5];
    var estado =inputss[6];
    var cel =inputss[8];
    var fecha =inputss[9];
    var errores = 0 ;
    
    if (nombre.value == ""|| nombre.value==null) {
        console.log("nombre vacio");
        nombre.classList.add('is-invalid');
        errores= errores+1;
    }else{
        nombre.classList.remove('is-invalid');
    }
    if (paterno.value == ""|| paterno.value==null) {
        console.log("paterno vacio");
        paterno.classList.add('is-invalid');
        errores= errores+1;
    }else{
        paterno.classList.remove('is-invalid');
    }
    if (materno.value == ""|| materno.value==null) {
        console.log("materno vacio");
        materno.classList.add('is-invalid');
        errores= errores+1;
    }else{
        materno.classList.remove('is-invalid');
    }
    if (genero.value == ""|| genero.value==null) {
        console.log("genero vacio");
        genero.classList.add('is-invalid');
        errores= errores+1;
    }else{
        genero.classList.remove('is-invalid');
    }
    if (apod.value == ""|| apod.value==null) {
        console.log("apod vacio");
        apod.classList.add('is-invalid');
        errores= errores+1;
    }else{
        apod.classList.remove('is-invalid');
    }
    if (estado.value == ""|| estado.value==null) {
        console.log("estado vacio");
        estado.classList.add('is-invalid');
        errores= errores+1;
    }else{
        estado.classList.remove('is-invalid');
    }
    if (expresiones.telefono.test(cel.value)){
        cel.classList.remove('is-invalid')
    }else{
        if (cel.value==""){ 
            cel.classList.remove('is-invalid')
        }else{
            console.log("Error teleofono")
            cel.classList.add('is-invalid')
            errores= errores+1;
        }
    }
    if (fecha.value == ""|| fecha.value==null) {
        console.log("fecha vacio");
        fecha.classList.add('is-invalid');
        errores= errores+1;
    }else{
        fecha.classList.remove('is-invalid');
    }
    
    if(errores!=0){   
        console.log("Error lol");
        erroresdiv.classList.remove('d-none');
        return false;
    }else{      
        erroresdiv.classList.add('d-none');
    }       
    
}      
function validateForm3() {
    console.log("validateform3 registapod")
    var inputss = document.getElementById("formalumno").elements;
    console.log(inputss);
    var nombre =inputss[1];
    var paterno =inputss[2];
    var materno =inputss[3];
    var rut =inputss[4];
    var correo =inputss[5];
    var cel =inputss[6];
    var errores = 0 ;
    if (nombre.value == ""|| nombre.value==null) {
        console.log("nombre vacio");
        nombre.classList.add('is-invalid');
        errores= errores+1;
    }else{
        nombre.classList.remove('is-invalid');
    }
    if (paterno.value == ""|| paterno.value==null) {
        console.log("paterno vacio");
        paterno.classList.add('is-invalid');
        errores= errores+1;
    }else{
        paterno.classList.remove('is-invalid');
    }
    if (materno.value == ""|| materno.value==null) {
        console.log("materno vacio");
        materno.classList.add('is-invalid');
        errores= errores+1;
    }else{
        materno.classList.remove('is-invalid');
    }
    if (rut.value == ""|| rut.value==null) {
        console.log("rut vacio");
        rut.classList.add('is-invalid');
        errores= errores+1;
    }else{
        rut.classList.remove('is-invalid');
    }
    if(Fn.validaRut((rut.value))){
        rut.classList.remove('is-invalid');
    }else{
        rut.classList.add('is-invalid'); 
        errores= errores+1;
 
    }
    if (correo.value == ""|| correo.value==null) {
        console.log("correo vacio");
        correo.classList.add('is-invalid');
        errores= errores+1;
    }else{
        correo.classList.remove('is-invalid');
    }
    if (expresiones.telefono.test(cel.value)){
        cel.classList.remove('is-invalid')
    }else{
        if (cel.value==""){ 
            cel.classList.remove('is-invalid')
        }else{
            console.log("Error teleofono")
            cel.classList.add('is-invalid')
            errores= errores+1;
        }
    }
    
    if(errores!=0){   
        console.log("Error lol");
        erroresdiv.classList.remove('d-none');
        return false;
    }else{      
        erroresdiv.classList.add('d-none');
    }       

    
}         

function validateForm4() {
    console.log("validatform4 Editar apod")
    var inputss = document.getElementById("formalumno").elements;
    console.log(inputss);
    var nombre =inputss[1];
    var paterno =inputss[2];
    var materno =inputss[3];
    var correo =inputss[4];
    var cel =inputss[5];
    var errores = 0 ;
    if (nombre.value == ""|| nombre.value==null) {
        console.log("nombre vacio");
        nombre.classList.add('is-invalid');
        errores= errores+1;
    }else{
        nombre.classList.remove('is-invalid');
    }
    if (paterno.value == ""|| paterno.value==null) {
        console.log("paterno vacio");
        paterno.classList.add('is-invalid');
        errores= errores+1;
    }else{
        paterno.classList.remove('is-invalid');
    }
    if (materno.value == ""|| materno.value==null) {
        console.log("materno vacio");
        materno.classList.add('is-invalid');
        errores= errores+1;
    }else{
        materno.classList.remove('is-invalid');
    }

    if (correo.value == ""|| correo.value==null) {
        console.log("correo vacio");
        correo.classList.add('is-invalid');
        errores= errores+1;
    }else{
        correo.classList.remove('is-invalid');
    }
    if (expresiones.telefono.test(cel.value)){
        cel.classList.remove('is-invalid')
    }else{
        if (cel.value==""){ 
            cel.classList.remove('is-invalid')
        }else{
            console.log("Error teleofono")
            cel.classList.add('is-invalid')
            errores= errores+1;
        }
    }
    
    if(errores!=0){   
        console.log("Error lol");
        erroresdiv.classList.remove('d-none');
        return false;
    }else{      
        erroresdiv.classList.add('d-none');
    }       

   
}         
