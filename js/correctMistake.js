 function correct(string){
	
    let correct = string.split('');
    let stringCorrect = [];
    for (var i=0; i < correct.length; i++) {
        if (correct[i] === '0') {
            stringCorrect.push('O');
        }
        else if (correct[i] === '1') {
            stringCorrect.push('I');
        }
        else if (correct[i] === '5') {
            stringCorrect.push('S');
        }
        else {
            stringCorrect.push(correct[i]);
        }

        
        }
    return stringCorrect.join('');
    }

 


