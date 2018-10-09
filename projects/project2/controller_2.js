var stores = ['Fareway', 'Ace Hardware', 'Caseys', 'The Hatchery', 'Amundsens']
var sections = ['Produce', 'Meats', 'Cereal', 'Canned Goods', 'Frozen Foods', 'Dairy', 'Liquor', 'Tools', 'Clothing']

var shoppingModel = new ShoppingList()
var myView = new ShoppingView(shoppingModel)

$checkbox = $('.Checked');
function checkArray(){
    var chkArray = [];
    chkArray = $.map($checkbox, function(el){
        if(el.checked) { return el.id };
    });
    console.log(chkArray);
}

function clickedon() {
    let rowcolids = ['itemname', 'qty', 'store', 'category', 'price', 'priority']
    let vals = {};
    for (let cid of rowcolids) {
        vals[cid] = document.getElementById(cid).value;
    }
    let it = new Item(vals.itemname, vals.qty, vals.priority, vals.store, vals.category, vals.price)
    shoppingModel.addItem(it)
}

function clickedOnSave() {
    let savedcols = localStorage.getItem('test');
    savedcols = savedcols ? JSON.parse(savedcols) : [];
    localStorage.setItem('test', JSON.stringify(shoppingModel));
    console.log(JSON.stringify(shoppingModel));
    //let test = localStorage.getItem('test');
    //console.log(test)
    // for (let row of shoppingModel) {
    //     for (let item of row) {
    //         localStorage.setItem('savedcols', JSON.stringify(shoppingmodel));
    //     }
    // }


}

function clickedOnRemPurch() {
    //when button is clicked, look for rows that are checked
    //table = document.getElementById('shoppinglist');
    //query = document.querySelector('tr');
    query = document.querySelectorAll('tr');
    console.log(query);
    //console.log(table);
    //console.log(tab.length);
    for (let trow of query[1:]) {
        if (trow.checked == true){
            console.log(trow);
        }
        
    }


    //localStorage.removeItem('test'.Checked);
    //myView.deleteAllRows(document.getElementById('shoppinglist').checked);
}
    //get id of row
    //list of items
    //go to shopping model, delete certain item
    //call redrawList, pass it new shopping model


function clickedOnRemAll() {
    localStorage.removeItem('test');
    myView.deleteAllRows(document.getElementById('shoppinglist'));
    //let savedcols = localStorage.getItem('test');
    //savedcols = savedcols ? localStorage.removeItem(shoppingModel) : [];
}


function populateSelect(selectId, sList) {
    let sel = document.getElementById(selectId, sList)
    for (let s of sList) {
        let opt = document.createElement("option")
        opt.value = s
        opt.innerHTML = s
        sel.appendChild(opt)
    }
}

$(document).ready(function () {
    populateSelect('store', stores)
    populateSelect('category', sections)
})