function mango(quantity, price){
    //por cada 2 mango se regala un mango
    return Math.floor(quantity / 3) * 2 * price + (quantity % 3) * price
}


let southAmericanCountries = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"]

for(let i=0; i< southAmericanCountries.length; i++){
    console.log(southAmericanCountries[i])
}