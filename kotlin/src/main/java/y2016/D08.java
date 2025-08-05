package y2016;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

import static util.Util.checkResult;
import static util.Util.readInput;

public class D08 {

    interface Command {
        void apply(boolean[][] pixels);
    }

    record RectCommand(int width, int height) implements Command {
        @Override
        public void apply(boolean[][] pixels) {
            for (int y = 0; y < height; y++) {
                for (int x = 0; x < width; x++) {
                    pixels[y][x] = true;
                }
            }
        }
    }

    record RotateRowCommand(int y, int amount) implements Command {
        @Override
        public void apply(boolean[][] pixels) {
            int width = pixels[0].length;
            boolean[] row = pixels[y];
            boolean[] newRow = new boolean[width];
            for (int x = 0; x < width; x++) {
                newRow[(x + amount) % width] = row[x];
            }
            pixels[y] = newRow;
        }
    }

    record RotateColumnCommand(int x, int amount) implements Command {
        @Override
        public void apply(boolean[][] pixels) {
            int height = pixels.length;
            boolean[] column = new boolean[height];
            for (int y = 0; y < height; y++) {
                column[y] = pixels[y][x];
            }
            for (int y = 0; y < height; y++) {
                pixels[(y + amount) % height][x] = column[y];
            }
        }
    }

    static final Pattern RE = Pattern.compile("(rect (\\d+)x(\\d+))|(rotate column x=(\\d+) by (\\d+))|(rotate row y=(\\d+) by (\\d+))");

    static Command parseCommand(String src) {
        Matcher m = RE.matcher(src);
        if (m.matches()) {
            if (m.group(1) != null) {
                return new RectCommand(Integer.parseInt(m.group(2)), Integer.parseInt(m.group(3)));
            } else if (m.group(4) != null) {
                return new RotateColumnCommand(Integer.parseInt(m.group(5)), Integer.parseInt(m.group(6)));
            } else if (m.group(7) != null) {
                return new RotateRowCommand(Integer.parseInt(m.group(8)), Integer.parseInt(m.group(9)));
            }
        }
        throw new IllegalArgumentException("Invalid command: " + src);
    }
    
    static int part1(int w, int h, String src) {
        boolean[][] pixels = new boolean[h][w];
        src.lines().map(D08::parseCommand).forEach(command -> command.apply(pixels));
        int count = 0;
        for (boolean[] row : pixels) {
            for (boolean pixel : row) {
                if (pixel) {
                    count++;
                    System.out.print("#");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
        return count;
    }

    public static void main(String[] args) {
        String SAMPLE = """
                rect 3x2
                rotate column x=1 by 1
                rotate row y=0 by 4
                rotate column x=1 by 1
                """;

        checkResult(part1(7, 3, SAMPLE), 6);

        String input = readInput(2016, 8);
        System.out.println(part1(50, 6, input));
    }
}
