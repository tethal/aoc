use std::collections::HashSet;

fn win_count(line: &str) -> usize {
    let (a, b) = line.split_once(":").unwrap().1.split_once(" | ").unwrap();
    let aa = a.split_whitespace().map(|n| n.parse::<u32>().unwrap()).collect::<HashSet<_>>();
    let bb = b.split_whitespace().map(|n| n.parse::<u32>().unwrap()).collect::<HashSet<_>>();
    aa.intersection(&bb).count()
}

pub fn part1(src: &str) -> usize {
    src
        .lines()
        .map(win_count)
        .filter(|c| *c > 0)
        .map(|n| 2_usize.pow(n as u32 - 1))
        .sum()
}

pub fn part2(src: &str) -> usize {
    let mut cards: Vec<usize> = src.lines().map(win_count).collect();
    for i in (0..cards.len()).rev() {
        cards[i] = 1 + cards[i + 1..i + 1 + cards[i]].iter().sum::<usize>();
    }
    cards.iter().sum()
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    const EXAMPLE: &str = indoc! {"
        Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
        Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
        Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
        Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
        Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
        Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
    "};

    #[test]
    fn part1_test() {
        assert_eq!(13, part1(EXAMPLE))
    }

    #[test]
    fn part2_test() {
        assert_eq!(30, part2(EXAMPLE))
    }
}
