use std::collections::HashSet;

use itertools::Itertools;

enum Tile {
    Part(usize),
    Symbol(char),
    Empty,
}

struct Schematic {
    grid: Vec<Vec<Tile>>,
    part_numbers: Vec<u32>,
}

impl Schematic {
    fn parse(src: &str) -> Schematic {
        let mut part_numbers = vec![];

        let mut convert_tile = |number: &mut Option<usize>, c: char| -> Option<Tile> {
            match c {
                '0'..='9' => {
                    let d = c.to_digit(10).unwrap();
                    let i = *number.get_or_insert_with(|| {
                        part_numbers.push(0);
                        part_numbers.len() - 1
                    });
                    part_numbers[i] = 10 * part_numbers[i] + d;
                    Some(Tile::Part(i))
                }
                '.' => {
                    *number = None;
                    Some(Tile::Empty)
                }
                _ => {
                    *number = None;
                    Some(Tile::Symbol(c))
                }
            }
        };

        Schematic {
            grid: src
                .lines()
                .map(|line| line
                    .chars()
                    .scan(None, &mut convert_tile)
                    .collect())
                .collect(),
            part_numbers,
        }
    }

    fn get_neighbours(&self, x: usize, y: usize) -> impl Iterator<Item = usize> + '_ {
        (x-1..=x+1).cartesian_product(y-1..=y+1)
            .filter_map(move |(xx, yy)| match self.grid[yy][xx] { Tile::Part(i) => Some(i), _ => None})
    }

    fn symbols(&self) -> impl Iterator<Item = (usize, usize, char)> + '_ {
        self.grid
            .iter()
            .enumerate()
            .flat_map(|(y, r)| r
                .iter()
                .enumerate()
                .filter_map(move |(x, t)| match t { Tile::Symbol(c) => Some((x, y, *c)), _ => None }))
    }
}

pub fn part1(src: &str) -> u32 {
    let schema = Schematic::parse(src);

    schema
        .symbols()
        .flat_map(|(x, y, _)| schema.get_neighbours(x, y))
        .unique()
        .map(|i| schema.part_numbers[i])
        .sum()
}

pub fn part2(src: &str) -> u32 {
    let schema = Schematic::parse(src);

    schema
        .symbols()
        .filter(|(_, _, c)| *c == '*')
        .map(|(x, y, _)| HashSet::<_>::from_iter(schema.get_neighbours(x, y)))
        .filter(|s| s.len() == 2)
        .map(|s| s.iter().map(|i| schema.part_numbers[*i]).product::<u32>())
        .sum()
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    const EXAMPLE: &str = indoc! {"
        467..114..
        ...*......
        ..35..633.
        ......#...
        617*......
        .....+.58.
        ..592.....
        ......755.
        ...$.*....
        .664.598..
    "};

    #[test]
    fn part1_test() {
        assert_eq!(4361, part1(EXAMPLE))
    }

    #[test]
    fn part2_test() {
        assert_eq!(467835, part2(EXAMPLE))
    }
}
