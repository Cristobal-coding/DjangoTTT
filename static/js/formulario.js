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
const validarFormulario= (e) =>{
    switch (e.target.name){
        case"rut":
            if (Fn.validaRut((e.target.value))){
                document.getElementById('id_rut').classList.remove('is-invalid')
            } else {
                document.getElementById('id_rut').classList.add('is-invalid')
            }      
        break;
        case"nombre":
            if (e.target.value){
                document.getElementById('id_nombre').classList.remove('is-invalid')
            }else{
                document.getElementById('id_nombre').classList.add('is-invalid')

            }
        break;
        case"apellido_paterno":
            if (e.target.value){
                document.getElementById('id_apellido_paterno').classList.remove('is-invalid')
            }else{
                document.getElementById('id_apellido_paterno').classList.add('is-invalid')
            }
        break;
        case"apellido_materno":
        if (e.target.value){
            document.getElementById('id_apellido_materno').classList.remove('is-invalid')
        }else{
            document.getElementById('id_apellido_materno').classList.add('is-invalid')
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
    input.addEventListener('keyup', validarFormulario)

    input.addEventListener('blur',validarFormulario)
    
})

