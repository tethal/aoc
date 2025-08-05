package y2016;

import java.util.List;
import java.util.stream.Collector;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import static util.Util.checkResult;
import static util.Util.readInput;

public class D06 {

    static Collector<Character, StringBuilder, String> charJoiner() {
        return Collector.of(StringBuilder::new, StringBuilder::append, StringBuilder::append, StringBuilder::toString);
    }

    static String getColumn(List<String> rows, int col) {
        return rows.stream().map(s -> s.charAt(col)).collect(charJoiner());
    }

    static Stream<String> transpose(Stream<String> src) {
        List<String> rows = src.toList();
        int columnCount = rows.get(0).length();
        return IntStream.range(0, columnCount).mapToObj(col -> getColumn(rows, col));
    }

    static char mostFrequentChar(String src) {
        int[] freq = new int[26];
        src.chars().forEach(c -> freq[c - 'a']++);
        int maxIndex = IntStream.range(0, 26).reduce((a, b) -> freq[a] > freq[b] ? a : b).orElseThrow();
        return (char) (maxIndex + 'a');
    }

    static String part1(String src) {
        return transpose(src.lines()).map(D06::mostFrequentChar).collect(charJoiner());
    }

    static char leastFrequentChar(String src) {
        int[] freq = new int[26];
        src.chars().forEach(c -> freq[c - 'a']++);
        int maxIndex = IntStream.range(0, 26).reduce((a, b) -> freq[a] < freq[b] ? a : b).orElseThrow();
        return (char) (maxIndex + 'a');
    }

    static String part2(String src) {
        return transpose(src.lines()).map(D06::leastFrequentChar).collect(charJoiner());
    }

    static String part1alt(Stream<String> lines) {
        int[] freq = new int[26 * 8];
        lines.forEach(line -> {
            assert line.length() == 8;
            for (int i = 0; i < 8; i++) {
                freq[line.charAt(i) - 'a' + i * 26]++;
            }
        });
        char[] result = new char[8];
        for (int i = 0; i < 8; i++) {
            int maxFreq = 0;
            for (int j = 0; j < 26; j++) {
                if (freq[i * 26 + j] > maxFreq) {
                    maxFreq = freq[i * 26 + j];
                    result[i] = (char) (j + 'a');
                }
            }
        }
        return new String(result);
    }

    public static void main(String[] args) {
        String SAMPLE = """
                eedadn
                drvtee
                eandsr
                raavrd
                atevrs
                tsrnev
                sdttsa
                rasrtv
                nssdts
                ntnada
                svetve
                tesnvt
                vntsnd
                vrdear
                dvrsen
                enarar
                """;

        checkResult(part1(SAMPLE), "easter");
//        checkResult(part2(SAMPLE), "advent");

        String input = readInput(2016, 6);
        System.out.println(part1(input));
        System.out.println(part1alt(input.lines()));
        System.out.println(part2(input));
    }
}
