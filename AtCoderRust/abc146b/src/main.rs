use std::io::*;
use std::str::FromStr;
use std::char;

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
    let n: u32 = read();
    let s: String = read();
    let new_s: String = s.as_str().chars().map(|c| convert(&c, n)).collect();
    println!("{}", new_s);
}

fn convert(c: &char, offset: u32) -> char{
    let i: u32 = *c as u32;
    char::from_u32((i + offset - 65) % 26 + 65).unwrap()
}
