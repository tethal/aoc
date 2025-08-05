package y2016;

import java.util.Arrays;
import java.util.Map;

import static java.util.Map.entry;
import static util.Util.checkResult;
import static util.Util.readInput;

public class D02 {
    private static final String TABLE = "124123513362157426843695487759876998";

    static int part1(String src) {
        int pos = 5;
        int result = 0;
        for (String line : src.split("\r?\n")) {
            pos = line.chars().reduce(pos, (p, c) -> TABLE.charAt((p - 1) * 4 + "URDL".indexOf(c)) - '0');
            result = result * 10 + pos;
        }
        return result;
    }

    private static final Map<Character, String> TABLE2 = Map.ofEntries(
            entry('1', "1131"),
            entry('2', "2362"),
            entry('3', "1472"),
            entry('4', "4483"),
            entry('5', "5655"),
            entry('6', "27A5"),
            entry('7', "38B6"),
            entry('8', "49C7"),
            entry('9', "9998"),
            entry('A', "6BAA"),
            entry('B', "7CDA"),
            entry('C', "8CCB"),
            entry('D', "BDDD")
    );

    static String part2(String src) {
        char pos = '5';
        StringBuilder result = new StringBuilder();
        for (String line : src.split("\r?\n")) {
            for (int i = 0; i < line.length(); i++) {
                pos = TABLE2.get(pos).charAt("URDL".indexOf(line.charAt(i)));
            }
            result.append(pos);
        }
        return result.toString();
    }

    boolean isTriangle(int[] sides) {
        Arrays.sort(sides);
        return sides[0] + sides[1] > sides[2];
    }

    public static void main(String[] args) {
        String sample = """
                ULL
                RRDDD
                LURDL
                UUUUD
                """;
        checkResult(part1(sample), 1985);
        checkResult(part2(sample), "5DB3");

        String input = readInput(2016, 2);
        System.out.println(part1(input));
        System.out.println(part2(input));
    }
}
