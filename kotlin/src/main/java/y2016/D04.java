package y2016;

import java.util.Collections;
import java.util.TreeMap;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import static util.Util.checkResult;
import static util.Util.readInput;

public class D04 {

    record Room(String name, int sectorId, String checksum) {
        static final Pattern PATTERN = Pattern.compile("(.*)-(\\d+)\\[(.*)]");

        static Room parse(String line) {
            Matcher matcher = PATTERN.matcher(line);
            if (!matcher.matches()) {
                throw new IllegalArgumentException(line);
            }
            return new Room(matcher.group(1), Integer.parseInt(matcher.group(2)), matcher.group(3));
        }

        boolean isRealRoom() {
            return checksum.equals(calcChecksum(name));
        }

        String decryptedName() {
            return decrypt(name, sectorId);
        }
    }

    static String calcChecksum(String name) {
        int[] freq = new int[26];
        name.chars().filter(c -> c != '-').forEach(c -> freq[c - 'a']++);
        TreeMap<Integer, String> map = new TreeMap<>(Collections.reverseOrder());
        for (char c = 'a'; c <= 'z'; c++) {
            map.merge(freq[c - 'a'], String.valueOf(c), String::concat);
        }
        return String.join("", map.values()).substring(0, 5);
    }

    static String decrypt(String name, int sectorId) {
        return name.chars()
                .map(c -> c == '-' ? ' ' : (c + sectorId + 33) % 26 + 'a')
                .collect(
                        () -> new StringBuilder(name.length()),
                        (sb, c) -> sb.append((char) c),
                        StringBuilder::append)
                .toString();
    }

    static int part1(String src) {
        return src.lines()
                .map(Room::parse)
                .filter(Room::isRealRoom)
                .mapToInt(Room::sectorId)
                .sum();
    }

    static int part2(String src) {
        return src.lines()
                .map(Room::parse)
                .filter(Room::isRealRoom)
                .filter(r -> r.decryptedName().contains("northpole"))
                .mapToInt(Room::sectorId)
                .findFirst()
                .getAsInt();
    }

    public static void main(String[] args) {
        checkResult(calcChecksum("aaaaa-bbb-z-y-x"), "abxyz");
        checkResult(decrypt("qzmt-zixmtkozy-ivhz", 343), "very encrypted name");
        String sample = """
                aaaaa-bbb-z-y-x-123[abxyz]
                a-b-c-d-e-f-g-h-987[abcde]
                not-a-real-room-404[oarel]
                totally-real-room-200[decoy]
                """;
        checkResult(part1(sample), 1514);

        String input = readInput(2016, 4);
        System.out.println(part1(input));
        System.out.println(part2(input));
    }
}
