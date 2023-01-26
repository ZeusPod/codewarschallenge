function lostMap(array) {
  let new_array =[]
	array.forEach(element => {
				new_array.push(element * 2)
	});
	return new_array			
}



console.log(lostMap(['2','4','6']))

