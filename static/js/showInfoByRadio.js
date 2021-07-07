var currentValue =0;

function handleClick(myRadio) {
    if (currentValue == 0){
        currentValue = myRadio.value;
        // myRadio.value = currentValue;
    }
    if(myRadio.value.indexOf('repitente') !== -1){
        document.getElementById(myRadio.value).classList.remove('d-none');
        document.getElementById(myRadio.value).classList.add('d-block');
        if (currentValue.indexOf('abandono') !== -1){
            document.getElementById(currentValue).classList.remove('d-block');
            document.getElementById(currentValue).classList.add('d-none');
        }
        if (currentValue.indexOf('error') !== -1){
            document.getElementById(currentValue).classList.remove('d-block');
            document.getElementById(currentValue).classList.add('d-none');
        }
    }
    if(myRadio.value.indexOf('abandono') !== -1){
        document.getElementById(myRadio.value).classList.remove('d-none');
        document.getElementById(myRadio.value).classList.add('d-block');
        if (currentValue.indexOf('repitente') !== -1){
            document.getElementById(currentValue).classList.remove('d-block');
            document.getElementById(currentValue).classList.add('d-none');
        }
        if (currentValue.indexOf('error') !== -1){
            document.getElementById(currentValue).classList.remove('d-block');
            document.getElementById(currentValue).classList.add('d-none');
        }
    }
    if(myRadio.value.indexOf('error') !== -1){     
        document.getElementById(myRadio.value).classList.remove('d-none');
        document.getElementById(myRadio.value).classList.add('d-block');
        if (currentValue.indexOf('abandono') !== -1){
            document.getElementById(currentValue).classList.remove('d-block');
            document.getElementById(currentValue).classList.add('d-none');
        }
        if (currentValue.indexOf('repitente') !== -1){
            document.getElementById(currentValue).classList.remove('d-block');
            document.getElementById(currentValue).classList.add('d-none');
        }
    }
    currentValue = myRadio.value;
    console.log(currentValue);
}

function clearAll(myButton) {
    currentValue= 0;
    rut = myButton.id;
    rep = 'radrepitente'+rut;
    aban = 'radabandono'+rut;
    err = 'raderror'+rut;
    radi2=document.getElementById(aban);
    radi3=document.getElementById(err);
    radi2.checked=false;
    radi3.checked=false;
    
    
    document.getElementById('abandono'+rut).classList.remove('d-block');
    document.getElementById('abandono'+rut).classList.add('d-none');
    
    document.getElementById('error'+rut).classList.remove('d-block');
    document.getElementById('error'+rut).classList.add('d-none');
    if (radi1 !=null){
        radi1=document.getElementById(rep);
        radi1.checked=false;
        document.getElementById('repitente'+rut).classList.remove('d-block');
        document.getElementById('repitente'+rut).classList.add('d-none');
    }
}
