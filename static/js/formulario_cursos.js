const formularioA = document.getElementById('finishA');
formularioA.addEventListener('submit',(e)=>{  
    old = document.getElementById('fasemestre_old').value;
    nueva = document.getElementById('fasemestre_new').value;
    if (old == ''){
        e.preventDefault();
        document.getElementById('fasemestre_old').classList.add('is-invalid')
    }else{
        document.getElementById('fasemestre_old').classList.remove('is-invalid')
    }
    if (nueva == ''){
        e.preventDefault();
        document.getElementById('fasemestre_new').classList.add('is-invalid')
    }else{
        document.getElementById('fasemestre_new').classList.remove('is-invalid')
    }

})
const formularioS = document.getElementById('finishS');
formularioS.addEventListener('submit',(e)=>{  
    old = document.getElementById('fssemestre_old').value;
    nueva = document.getElementById('fssemestre_new').value;
    if (old == ''){
        e.preventDefault();
        document.getElementById('fssemestre_old').classList.add('is-invalid')
    }else{
        document.getElementById('fssemestre_old').classList.remove('is-invalid')
    }
    if (nueva == ''){
        e.preventDefault();
        document.getElementById('fssemestre_new').classList.add('is-invalid')
    }else{
        document.getElementById('fssemestre_new').classList.remove('is-invalid')
    }

})
inputAño = document.getElementById('añoInput');
inputAño.oninput = function () {
    if (this.value.length > 4) {
        this.value = this.value.slice(0,4); 
    }
}