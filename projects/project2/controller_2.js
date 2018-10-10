var stores = ['Fareway', 'Ace Hardware', 'Caseys', 'The Hatchery', 'Amundsens']
var sections = ['Produce', 'Meats', 'Cereal', 'Canned Goods', 'Frozen Foods', 'Dairy', 'Liquor', 'Tools', 'Clothing']

var shoppingModel = new ShoppingList()
var myView = new ShoppingView(shoppingModel)


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

}

function clickedOnRemPurch() {
    //when button is clicked, look for rows that are checked
    //table = document.getElementById('shoppinglist');
    //query = document.querySelector('tr');
    query = document.querySelectorAll('tr');
    console.log(query);
    //console.log(table);
    //console.log(tab.length);
    for (let trow of query) {
        if ('checkbox' == query.type && true == query.checked){
            console.log(query);
        }
        
    }
    //localStorage.removeItem('test'.Checked);
    //myView.deleteAllRows(document.getElementById('shoppinglist').checked);


}

function clickedOnRemAll() {
    localStorage.removeItem('test');
    myView.deleteAllRows(document.getElementById('shoppinglist'));
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