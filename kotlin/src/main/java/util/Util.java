package util;

import java.nio.file.Files;
import java.nio.file.Path;

public class Util {

    public static <T> void checkResult(T actual, T expected) {
        if (!actual.equals(expected)) {
            throw new AssertionError(actual + " != " + expected);
        }
    }

    public static String readInput(int y, int d) {
        try {
            return Files.readString(Path.of("in/y%d/%02d.txt".formatted(y, d)));
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
