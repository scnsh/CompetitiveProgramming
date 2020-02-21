//refer to https://atcoder.jp/contests/abc146/submissions/9125164

use std::io::*;
use std::str::FromStr;
use std::char;

const MAX_INT: u64 = 1000000000;
const MIN_INT: u64 = 1;


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
    let a = read();
    let b = read();
    let xstr: String = read();
    let x = xstr.parse().unwrap();

    let (mut l, mut t) = (MIN_INT - 1, MAX_INT + 1);
    while t - l > 1 {
        let n = (l + t) / 2;
        if cost(a, b, n) <= x {
            l = n;
        } else {
            t = n;
        }
    }
    println!("{:?}", l)
}

fn cost(a: u64, b: u64, n: u64) -> u64 
{
    let d = n.to_string().len() as u64;
    a * n + b * d
}