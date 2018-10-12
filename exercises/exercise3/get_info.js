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
    var inputPlus = +input + +1;
    var inputMinus = input-1;
    var number = await Promise.all([getData(`http://numbersapi.com/${input}?json`)]);
    var numberAbove = await Promise.all([getData(`http://numbersapi.com/${inputPlus}?json`)]);
    var numberBelow = await Promise.all([getData(`http://numbersapi.com/${inputMinus}?json`)]);

    console.log(input);
    console.log(numberBelow[0].text);
    console.log(number[0].text);
    console.log(numberAbove[0].text);
    
    document.getElementById("displayBelow").innerHTML = numberBelow[0].text;
    document.getElementById("displayNumber").innerHTML = number[0].text;
    document.getElementById("displayAbove").innerHTML = numberAbove[0].text;
    
    //let i = document.createElement('div');
    //i.getElementById("display").classList.add('row');
}

