const formularioA = document.getElementById('formRazon');
formularioA.addEventListener('submit',(e)=>{  
    old = document.getElementById('semestre_old').value;
    nueva = document.getElementById('semestre_new').value;
    if (old == ''){
        e.preventDefault();
        document.getElementById('semestre_old').classList.add('is-invalid')
    }else{
        document.getElementById('semestre_old').classList.remove('is-invalid')
    }
    if (nueva == ''){
        e.preventDefault();
        document.getElementById('semestre_new').classList.add('is-invalid')
    }else{
        document.getElementById('semestre_new').classList.remove('is-invalid')
    }

})