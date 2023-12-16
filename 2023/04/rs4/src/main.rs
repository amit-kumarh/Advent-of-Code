use regex::Regex;
use std::{
    collections::{HashMap, HashSet},
    fs::File,
    io::{BufRead, BufReader},
};

fn main() {
    let f = File::open("/home/amit/Documents/code/advent_of_code/2023/4/4.in")
        .expect("couldn't read file");

    let mut file_len = 0;
    let mut p1 = 0;
    let mut copies: HashMap<usize, usize> = HashMap::new();
    let re = Regex::new(r"^.+: (?<elf>.*) \| (?<me>.*)").expect("hardcoded");
    for (i, line) in BufReader::new(f).lines().filter_map(|e| e.ok()).enumerate() {
        let caps = re.captures(&line).unwrap();
        let elf: HashSet<&str> = HashSet::from_iter(caps["elf"].split_whitespace());
        let me: HashSet<&str> = HashSet::from_iter(caps["me"].split_whitespace());

        let inter = elf.intersection(&me).count();
        if inter > 0 {
            p1 += 2_usize.pow((inter - 1) as u32)
        }

        for j in 0..inter {
            let curr = copies.get(&i).unwrap_or(&1).clone();
            *copies.entry(i + j + 1).or_insert(1) += curr
        }
        file_len += 1;
    }

    let mut p2 = 0;
    for card in 0..file_len {
        p2 += copies.get(&card).unwrap_or(&1);
    }

    println!("{}", p1);
    println!("{}", p2)
}
