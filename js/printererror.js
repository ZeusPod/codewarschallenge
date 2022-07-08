function printerError(s) {
    s.toLowerCase()
    let large= s.length
    let list_s = s.split()
    let compare = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    let result = list_s.map((letter)=>{
        let count =  0
        if(letter in compare){
            pass
        }
        else{
            count +=1
        }
        return 
    })
}


console.log(printerError("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))