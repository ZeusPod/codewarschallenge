/* Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
 */


function XO(str){
    var x = 0;
    var o = 0;
    for(var i = 0; i < str.length; i++){
        if(str[i] === 'x' || str[i] === 'X'){
            x++;
        }
        if(str[i] === 'o' || str[i] === 'O'){
            o++;
        }
    }

    if(x === o){
        return true;
    }
    else{
        return false;
    }
}


mystring = "xoOxxo";
console.log(XO(mystring));