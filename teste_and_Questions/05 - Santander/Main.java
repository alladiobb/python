import java.util.HashMap;
import java.util.Map;

public class Main {
    public static int sockMerchant(int n, int[] ar) {
        Map<Integer, Integer> socks = new HashMap<>();
        int pairs = 0;
        for (int sock : ar) {
            if (socks.containsKey(sock)) {
                socks.put(sock, socks.get(sock) + 1);
                if (socks.get(sock) % 2 == 0) {
                    pairs++;
                }
            } else {
                socks.put(sock, 1);
            }
        }
        return pairs;
    }

    public static void main(String[] args) {
        int n = 7;
        int[] ar = {1, 2, 1, 2, 1, 3, 2, 1, 3, 2};
        int result = sockMerchant(n, ar);
        System.out.println(result);
    }
}