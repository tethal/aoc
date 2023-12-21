use std::collections::HashSet;
use std::ops::Range;
use itertools::Itertools;

fn parse(src: &str) -> (Vec<i64>, Vec<Vec<(Range<i64>, i64)>>) {
    let mut lines = src.lines();
    let seeds: Vec<i64> = lines.next().unwrap().split_once(":").unwrap().1.split_whitespace().map(|n| n.parse().unwrap()).collect();
    let maps = lines
        .group_by(|y| match y.chars().next() { Some(c) => c.is_digit(10), None => false })
        .into_iter()
        .filter_map(|(x, y)| if x { Some(y) } else { None })
        .map(|it| {
            it.map(|l| {
                let (dst, src, len) = l.split_whitespace().map(|n| n.parse::<i64>().unwrap()).next_tuple().unwrap();
                (src..src + len, dst - src)
            }).collect_vec()
        })
        .collect_vec();
    (seeds, maps)
}

pub fn part1(src: &str) -> i64 {
    let (seeds, maps) = parse(src);
    seeds
        .iter()
        .map(|s|
            maps
                .iter()
                .fold(*s, |v, map|
                    map
                        .iter()
                        .filter(|(src_range, _)| src_range.contains(&v))
                        .next()
                        .map(|(_, delta)| v + delta)
                        .unwrap_or(v)
                )
        )
        .min()
        .unwrap()
}

pub fn part2(src: &str) -> i64 {
    let (seeds, maps) = parse(src);
    let mut ranges = seeds.iter().tuples().map(|(a, b)| *a..*a + *b).collect::<HashSet<_>>();

    for map in maps {
        let mut new_ranges = HashSet::new();
        for (b, delta) in map {
            let old_ranges = ranges;
            ranges = HashSet::new();
            for a in old_ranges {
                if b.start <= a.start {
                    if b.end >= a.end {
                        new_ranges.insert(a.start + delta..a.end + delta);
                    } else if b.end > a.start {
                        new_ranges.insert(a.start + delta..b.end + delta);
                        ranges.insert(b.end..a.end);
                    } else {
                        ranges.insert(a);
                    }
                } else if b.start < a.end {
                    if b.end >= a.end {
                        new_ranges.insert(b.start + delta..a.end + delta);
                        ranges.insert(a.start..b.start);
                    } else {
                        new_ranges.insert(b.start + delta..b.end + delta);
                        ranges.insert(a.end..b.start);
                        ranges.insert(b.end..a.end);
                    }
                } else {
                    ranges.insert(a);
                }
            }
        }
        new_ranges.iter().for_each(|r| { ranges.insert(r.clone()); });
    }
    ranges.iter().map(|r| r.start).min().unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    const EXAMPLE: &str = indoc! {"
        seeds: 79 14 55 13

        seed-to-soil map:
        50 98 2
        52 50 48

        soil-to-fertilizer map:
        0 15 37
        37 52 2
        39 0 15

        fertilizer-to-water map:
        49 53 8
        0 11 42
        42 0 7
        57 7 4

        water-to-light map:
        88 18 7
        18 25 70

        light-to-temperature map:
        45 77 23
        81 45 19
        68 64 13

        temperature-to-humidity map:
        0 69 1
        1 0 69

        humidity-to-location map:
        60 56 37
        56 93 4
    "};

    #[test]
    fn part1_test() {
        assert_eq!(35, part1(EXAMPLE))
    }

    #[test]
    fn part2_test() {
        assert_eq!(46, part2(EXAMPLE))
    }
}
