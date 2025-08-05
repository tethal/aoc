package y2016;

import java.security.MessageDigest;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import static util.Util.checkResult;
import static util.Util.readInput;

public class D05 {

    private static final MessageDigest md5;

    static {
        try {
            md5 = MessageDigest.getInstance("MD5");
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    static String part1(String src) {
        return IntStream
                .iterate(0, i -> i + 1)
                .mapToObj(i -> src + i)
                .map(s -> md5.digest(s.getBytes()))
                .filter(b -> b[0] == 0 && b[1] == 0 && (b[2] & 0xf0) == 0)
                .map(b -> Integer.toHexString(b[2] & 0xf))
                .limit(8)
                .collect(Collectors.joining());
    }

    static String part2(String src) {
        char[] result = new char[8];
        int done = 0;
        int i = 0;
        while (done != 8) {
            byte[] digest = md5.digest((src + i++).getBytes());
            if (digest[0] == 0 && digest[1] == 0 && (digest[2] & 0xf0) == 0) {
                int pos = digest[2] & 0xf;
                if (pos < 8 && result[pos] == '\0') {
                    result[pos] = Character.forDigit((digest[3] & 0xf0) >> 4, 16);
                    done++;
                }
            }
        }
        return new String(result);
    }

    public static void main(String[] args) {
        checkResult(part1("abc"), "18f47a30");
        checkResult(part2("abc"), "05ace8e3");

        String input = readInput(2016, 5);
        System.out.println(part1(input));
        System.out.println(part2(input));
    }
}
