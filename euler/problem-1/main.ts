function sum_of_multiples(limit:number): number {
    let total_sum: number = 0
    for (let index = 0; index < limit; index++) {
        if (Math.floor(index % 3) === 0 || Math.floor(index % 5) === 0)  {
            total_sum = total_sum + index    
        }
    }
    return total_sum
}

console.log(sum_of_multiples(1000))