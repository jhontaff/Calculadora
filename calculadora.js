window.addEventListener('load', ()=> { /* Espera hasta que cargue el documento */
    // Se crean dos constantes (Una para buscar el display y la otra para los botones que quedan guardados 
    // en HTMLCollection)
    // querySelector para buscar un único elemento. getElementByClassName para tomar múltiples elementos con misma clase
    const display = document.querySelector('.calculator-display');
    const keypadButtons = document.getElementsByClassName('keypad-button'); 


    // Se crea otra constante para convertir el HTLMCollection en Array y poder iterar
    const keypadButtonsArray = Array.from(keypadButtons);
    
    // Se itera el nuevo array de botones
    keypadButtonsArray.forEach((button) => {
        // Se agrega el evento "click"
        button.addEventListener("click", ()=> {
            calculadora(button,display)
        })
    });
});

function calculadora (button, display) {
    //innerHTML para el texto que posee cada botón en el HTML
    switch (button.innerHTML){
        case "C":
            borrar (display);
            break;
        case "=":
            calcular (display);
            break;
        default:
            actualizar(display,button);
            break;
    }
}

function calcular (display) {
    display.innerHTML = eval(display.innerHTML); /* Toma el string, lo resuelve y los guarda en el innerHTML del display */
}

function actualizar (display,button) {
    if (display.innerHTML == 0){
        display.innerHTML = "";
    }
    display.innerHTML += button.innerHTML
}

function borrar (display){
    display.innerHTML = 0
}