use std::fs::read_to_string;

mod y2023;

fn main() {
    use y2023::d01::*;

    println!("{}", part1(read_to_string("../2023/in/01.txt").unwrap().as_str()));
    println!("{}", part2(read_to_string("../2023/in/01.txt").unwrap().as_str()));
}
