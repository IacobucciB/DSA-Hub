function sum_of_even_fibo(limit: number): number {
    let a: number = 1
    let b: number = 2
    let total: number = 0

    while (a <= limit) {
        if (Math.floor(a % 2) === 0) {
            total = total + a
        }
        let aux: number = a + b
        a = b
        b = aux
    }
    return total
}

let limit: number = 4000000
let res: number = sum_of_even_fibo(limit)
console.log(res);
