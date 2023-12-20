use std::cmp::max;

#[derive(Copy, Clone)]
struct Set {
    r: i32,
    g: i32,
    b: i32
}

struct Game {
    id: u32,
    sets: Vec<Set>
}

impl Set {
    fn parse(s: &str) ->Set {
        let mut result = Set {r: 0, g: 0, b: 0};
        for x in s.split(", ") {
            let (cnt_str, color) = x.split_once(" ").unwrap();
            let cnt: i32 = cnt_str.parse().unwrap();
            if color == "red" {
                result.r = cnt;
            }
            if color == "green" {
                result.g = cnt;
            }
            if color == "blue" {
                result.b = cnt;
            }
        }
        result
    }
}

impl Game {
    fn parse(s: &str) -> Game {
        let (a, b) = s.split_once(": ").unwrap();
        assert!(a.starts_with("Game "));
        Game {
            id: a[5..].parse().unwrap(),
            sets: b.split("; ").map(Set::parse).collect(),
        }
    }
}

pub fn part1(src: &str) -> u32 {
    src
        .lines()
        .map(Game::parse)
        .filter(|g| g.sets.iter().all(|s| s.r <= 12 && s.g <= 13 && s.b <= 14))
        .map(|g| g.id)
        .sum()
}

pub fn part2(src: &str) -> i32 {
    src
        .lines()
        .map(Game::parse)
        .map(|g| g.sets.iter().copied().reduce(|a, b| Set { r: max(a.r, b.r), g: max(a.g, b.g), b: max(a.b, b.b) }).unwrap())
        .map(|s| s.r * s.g * s.b)
        .sum()
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    const EXAMPLE: &str = indoc! {"
        Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
        Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
        Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
        Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    "};

    #[test]
    fn part1_test() {
        assert_eq!(8, part1(EXAMPLE))
    }

    #[test]
    fn part2_test() {
        assert_eq!(2286, part2(EXAMPLE))
    }
}
