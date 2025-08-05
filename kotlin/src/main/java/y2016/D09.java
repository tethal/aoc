package y2016;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

import static util.Util.checkResult;
import static util.Util.readInput;

public class D09 {

    static final Pattern RE = Pattern.compile("\\((\\d+)x(\\d+)\\)");

    static long calcDecompressedLength(String src, boolean recurse) {
        long result = 0;
        Matcher matcher = RE.matcher(src);
        int i = 0;
        while (matcher.find(i)) {
            result += matcher.start() - i;
            int length = Integer.parseInt(matcher.group(1));
            int repeat = Integer.parseInt(matcher.group(2));
            i = matcher.end();
            result += repeat * (recurse ? calcDecompressedLength(src.substring(i, i + length), true) : length);
            i += length;
        }
        result += src.length() - i;
        return result;
    }

    static long part1(String src) {
        return calcDecompressedLength(src.replaceAll("\\s+", ""), false);
    }

    static long part2(String src) {
        return calcDecompressedLength(src.replaceAll("\\s+", ""), true);
    }

    public static void main(String[] args) {
        checkResult(part1("X(8x2)(3x3)ABCY"), 18L);
        checkResult(part2("X(8x2)(3x3)ABCY"), 20L);

        String input = readInput(2016, 9);
        System.out.println(part1(input));
        System.out.println(part2(input));
    }
}
