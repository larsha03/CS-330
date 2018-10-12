/* jshint esversion: 6 */
/* jshint node: true */
'use strict';



async function getData(url) {
    return fetch(url)
        .then(response => response.json())
        // .then(json => console.log(json))
        .catch(error => console.log(error));
}
/*
async function populate() {
    let [number] = await Promise.all([
        getData('http://numbersapi.com/random/year?json')]);

    console.log(number);
   
}
*/
async function clickedOn(){
    var input = document.getElementById('input_num').value;
    var input1 = +input + +1;
    var input2 = input-1;
    var number = await Promise.all([getData(`http://numbersapi.com/${input}?json`)]);
    var number1 = await Promise.all([getData(`http://numbersapi.com/${input1}?json`)]);
    var number2 = await Promise.all([getData(`http://numbersapi.com/${input2}?json`)]);

    
    console.log(input);
    console.log(number);
    console.log(number1);
    console.log(number2);

    document.getElementById
}

