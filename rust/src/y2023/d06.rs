use itertools::Itertools;

fn solve(time: i64, dist: i64) -> i64 {
    let mut cnt = 0;
    for h in 0..=time {
        if (time - h) * h > dist { cnt += 1}
    }
    cnt
}

fn solve2(time: i64, dist: i64) -> i64 {
    let d = ((time * time - 4 * dist) as f64).sqrt();
    let x1 = ((time as f64 - d) / 2.0 + 0.001).ceil() as i64;
    let x2 = ((time as f64 + d) / 2.0 - 0.001).floor() as i64;
    return x2 - x1 + 1;
}

pub fn part1(src: &str) -> i64 {
    let (times, distances) = src
        .lines()
        .map(|line|
            line
                .split_once(':')
                .unwrap()
                .1
                .split_whitespace()
                .map(|s| s.parse::<i64>().unwrap())
                .collect_vec()
        )
        .next_tuple().unwrap();
    times.iter()
        .zip(distances)
        .map(|(t, d)| solve2(*t, d))
        .product()
}

pub fn part2(src: &str) -> i64 {
    let (t, d) = src.lines().map(|line| line.split_once(':').unwrap().1.replace(" ", "").parse::<i64>().unwrap()).next_tuple().unwrap();
    solve2(t, d)
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    const EXAMPLE: &str = indoc! {"
        Time:      7  15   30
        Distance:  9  40  200
    "};

    #[test]
    fn part1_test() {
        assert_eq!(288, part1(EXAMPLE))
    }

    #[test]
    fn part2_test() {
        assert_eq!(71503, part2(EXAMPLE))
    }
}
