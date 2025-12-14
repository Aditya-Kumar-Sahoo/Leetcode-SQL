import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;

    public int numberOfWays(String corridor) {
        List<Integer> seats = new ArrayList<>();

        for (int i = 0; i < corridor.length(); i++) {
            if (corridor.charAt(i) == 'S') {
                seats.add(i);
            }
        }

        int totalSeats = seats.size();
        if (totalSeats == 0 || totalSeats % 2 != 0) return 0;

        long ways = 1;

        // Iterate over boundaries between seat pairs
        for (int i = 2; i < totalSeats; i += 2) {
            int prevSecondSeat = seats.get(i - 1);
            int nextFirstSeat = seats.get(i);

            int plantsBetween = nextFirstSeat - prevSecondSeat - 1;
            ways = (ways * (plantsBetween + 1)) % MOD;
        }

        return (int) ways;
    }
}
