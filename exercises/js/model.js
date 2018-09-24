//Exercise 2: model.js: Create Item and ShoppingList classes 
//Author: Hans Larson
//Date: 9/23/2018

class Item {
    constructor(name, quantity, price, store, section, priority, purchased=false) {
        this._name = name;
        this._quantity = quantity;
        this._price = price;
        this._store = store;
        this._section = section;
        this._priority = priority;
        this._purchased = purchased;
    }
    get purchased() {
        return this._purchased;
    }
    set purchased(p) {
        console.log("Error");
    }

}

class ShoppingList {
    constructor() {
        this._items = [];
    }
    addItem(i) {
        this._items.push(i);
    }
    cleanList() {
        //for (var i = 0; i < items.length; i++)
        this._items.splice(0, this._items.length);
    }
    emptyList() {
        this._items = [];
    }
}

let shop = new ShoppingList();
shop.addItem("milk");
console.log(shop);
shop.cleanList();
console.log(shop);

shop.addItem("food");
console.log(shop);
shop.emptyList();
console.log(shop);