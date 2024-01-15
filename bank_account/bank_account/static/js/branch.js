 function enableBranch(answer){
    console.log(answer.value);
    if (answer.value == 1){
        document.getElementById('Trivandrum').classList.remove('d_none');
    }
    elif(answer.value == 2) {
        document.getElementById('Kollam').disabled = false

    }
    };