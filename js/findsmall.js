class SmallestIntegerFinder{
    findSmallestInt(args){
        args.sort((a,b)=>a-b);
        return args[0];
    }
}

lista = [78,56,232,12,8]

myorder = new SmallestIntegerFinder()
console.log(myorder.findSmallestInt(lista))
