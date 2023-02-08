var number = [1,2,3,5,6,8,9]

function pipeFix(number){
  let result = []
  lastn = number[number.length-1]
  for (let index = number[0]; index <=lastn ; index++) {
       result.push(index)
  }
	return result			
}



console.log(pipeFix(number))
