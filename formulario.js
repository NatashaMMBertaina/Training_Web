const para = document.querySelector('.p1');


let intentosCount = 1;

function rta() {
    let mensaje1 = '';
    let mensaje2 = '';
    let mensaje3 = '';
    let mensaje4 = '';

    if (document.getElementById('senoidal1').checked){
        mensaje1 = 'Correct!';
    } else {
        mensaje1 = 'Ooh!! This is not the displayed function.';
    }

    if (document.getElementById('creciente2').checked){
        mensaje2 = 'Correct!';
    } else {
        mensaje2 = 'Ooh!! This is not the displayed function.';
    }

    if (document.getElementById('cuadrada3').checked){
        mensaje3 = 'Correct!';
    } else {
        mensaje3 = 'Ooh!! This is not the displayed function.';
    }

    if (document.getElementById('decreciente4').checked){
        mensaje4 = 'Correct!';
    } else {
        mensaje4 = 'Ooh!! This is not the displayed function.';
    }

    para.textContent('Question 1:' + mensaje1 + '<br>Question 2:' + mensaje2 + '<br>Question 3:' + mensaje3 + 'Question 4:' + mensaje4);
}