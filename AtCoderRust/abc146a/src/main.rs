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
    let s: String = read();
    let ret = match s.as_str() {
        "SAT" => 1,
        "FRI" => 2,
        "THU" => 3,
        "WED" => 4,
        "TUE" => 5,
        "MON" => 6,
        "SUN" => 7,
        _ => 0
    };
    println!("{}", ret);
}
