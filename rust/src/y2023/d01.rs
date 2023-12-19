
fn sum_calibration_values<F>(src: &str, extract_digit: F) -> u32
    where F: Fn(&str, usize, char) -> Option<u32>
{
    src.lines().map(|line| {
        let first = line.char_indices().filter_map(|(pos, c)| extract_digit(line, pos, c)).next();
        let last = line.char_indices().rev().filter_map(|(pos, c)| extract_digit(line, pos, c)).next();
        first.unwrap() * 10 + last.unwrap()
    }).sum()
}

pub fn part1(src: &str) -> u32 {
    sum_calibration_values(src, |_, _, c| c.to_digit(10))
}

pub fn part2(src: &str) -> u32 {
    fn extract_spelled_digit(s: &str) -> Option<u32> {
        const DIGITS: [&'static str; 9] = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"];
        (1..10).find_map(|i| if s.starts_with(DIGITS[i - 1]) {Some(i as u32)} else {None})
    }
    sum_calibration_values(src, |line, pos, c| c.to_digit(10).or_else(|| extract_spelled_digit(&line[pos..])))
}

#[cfg(test)]
mod tests {
    use super::*;
    use indoc::indoc;

    #[test]
    fn part1_test() {
        assert_eq!(
            142,
            part1(indoc! {"
                1abc2
                pqr3stu8vwx
                a1b2c3d4e5f
                treb7uchet
            "}));
    }

    #[test]
    fn part2_test() {
        assert_eq!(
            281,
            part2(indoc! {"
                two1nine
                eightwothree
                abcone2threexyz
                xtwone3four
                4nineeightseven2
                zoneight234
                7pqrstsixteen
            "}));
    }
}
