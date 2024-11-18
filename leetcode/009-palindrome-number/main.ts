function isPalindrome(x: number): boolean {
	if(x < 0) {
		return false
	}
	let aux: number = x
	let digit: number = 0
	let reversed: number = 0
	while(aux != 0){
		digit = aux % 10
		aux = Math.floor(aux / 10)
		reversed = reversed * 10 + digit
	}
	if(x - reversed === 0) {
		return true
	}
	return false
}

console.log(isPalindrome(121))
console.log(isPalindrome(-121))
console.log(isPalindrome(10))