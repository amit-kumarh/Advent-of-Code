use std::{
    fs::File,
    io::{BufRead, BufReader},
};

fn main() {
    let p2 = true;
    let f = File::open("/home/amit/Documents/code/advent_of_code/2023/1/1.in")
        .expect("couldn't read file");

    let ans: u32 = BufReader::new(f)
        .lines()
        .filter_map(|l| l.ok())
        .map(|mut l| {
            if p2 {
                l = l
                    .replace("one", "o1e")
                    .replace("two", "t2o")
                    .replace("three", "t3e")
                    .replace("four", "f4r")
                    .replace("five", "f5e")
                    .replace("six", "s6x")
                    .replace("seven", "s7n")
                    .replace("eight", "e8t")
                    .replace("nine", "n9e");
            }

            let mut digits = l.chars().filter(|c| c.is_numeric());
            let first = digits.next().expect("no first digit").to_digit(10).unwrap();
            let last = match digits.last() {
                Some(c) => c.to_digit(10).unwrap(),
                None => first,
            };
            dbg!(first, last);
            format!("{first}{last}")
                .parse::<u32>()
                .expect("should be number")
        })
        .sum();

    println!("{ans}")
}
