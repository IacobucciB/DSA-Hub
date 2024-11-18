function twoSum(nums: number[], target: number): number[] {
	let res: number[] = [];
	for(let i = 0; i < nums.length - 1; i++) {
		for(let j = i + 1; j < nums.length; j++) {
			if(nums[i] + nums[j] === target) {
				res[0] = i;
				res[1] = j;
				return res;
			}
		}
	}
	return res;
};

let nums: number[] = [2,7,11,15];
let target: number = 9;
let test: number[] = twoSum(nums, target);
console.log(test)