use std::io;

fn main() {
    let mut r = String::new();
    // io::stdin().read_line(&mut r).expect("Failed to read line");
    io::stdin().read_line(&mut r).ok();
    let r: u32 = r.trim().parse().unwrap();
    println!("{}", r*r);
}
