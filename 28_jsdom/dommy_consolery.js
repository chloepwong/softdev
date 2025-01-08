// Team Mongoose :: Chloe Wong, Claire Song
// SoftDev pd5
// K28 -- Getting more comfortable with the dev console and the DOM
// 2025-01-07t
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
//checks that script has been loaded
console.log("AYO");

var i = "hello";
var j = 20;


//assign an anonymous fxn to a var
//sum of x and 30
var f = function(x) 
{
    var j=30;
    return j+x;
};


//instantiate an object
var o = { 'name' : 'Thluffy',
          age : 1024,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) { //function within function, also f(x)!
              return x+30;
          }
        };

//create a new node in the tree
var addItem = function(text)
{
    var list = document.getElementById("thelist"); //get list
    var newitem = document.createElement("li"); //create new list item
    newitem.innerHTML = text; //set inner HTML
    list.appendChild(newitem); //add new item to list
};

//prune a node from the tree
var removeItem = function(n)
{
    var listitems = document.getElementsByTagName('li'); //get list
    listitems[n].remove(); //remove item at index n
};

//color selected elements red
var red = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
	items[i].classList.add('red'); //adds red class to all list items
    }
};

//color a collection in alternating colors
var stripe = function()
{
    var items = document.getElementsByTagName("li");
    for(var i = 0; i < items.length; i++) {
	if (i%2==0) {
	    items[i].classList.add('red');
	} else {
	    items[i].classList.add('blue'); //indices with different parities get different color classes
	}
    }
};


//insert your implementations here for...
var fib = function(n) {
    if (n==0) {
        return(0);
    }
    else if (n==1) {
        return(1);
    } 
    else {
        return(fib(n-1)+fib(n-2));
    } 
}

var fact = function(n) { 
    if (n==1) {
        return 1;
    }
    else {
        return(n*fact(n-1))
    } 
};

var gcd = function(a, b) {
    if (b == 0) {
        return a;
    } 
    else {
        return gcd(b, a % b);
    }
};

console.log(fact(5))
console.log(fib(4))
console.log(gcd(6, 9))

// In addition to the style shown above,
//  you are encouraged to test drive the "arrow function syntax" as shown below.
//  Note anything notable.

const myFxn = (param1, param2) => { //doesn't require "function"
    var retVal = param1 + param2;
    return retVal;
};