use std::io::*;
use std::str::FromStr;


fn read<T: FromStr>() -> T {
    let stdin = stdin();
    let stdin = stdin.lock();
    let token: String = stdin
        .bytes()
        .map(|c| c.expect("failed to read char") as char)
        .skip_while(|c| c.is_whitespace())
        .take_while(|c| !c.is_whitespace())
        .collect();
    token.parse().ok().expect("failed to parse token")
}

fn main() {
    let n: usize = read();
    let v: Vec<(i32, i32)> = (0..n).map(|_| (read(), read())).collect();
    let mut ret = 0.0;
    for i in 0..n {
        for j in i+1..n{
            ret += dist(&v[i], &v[j]) as f64;
        }
    }
    let n_factorial = factorial(n) as f64;
    let offset = 2.0 * factorial(n-1) as f64;
    println!("{}", (offset * ret) / n_factorial);
}

fn dist(a: &(i32,i32), b: &(i32, i32)) -> f64{
    (((a.0 - b.0).pow(2) + (a.1 - b.1).pow(2)) as f64).sqrt()
}

fn factorial(n: usize) -> usize {
    if n == 0 {
        1
    } else {
        n * factorial(n - 1)
    }
}