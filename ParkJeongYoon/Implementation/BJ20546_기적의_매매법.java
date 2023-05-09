import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 준현(BNP): 한 번 산 주식은 절대 팔지 않는다. 살 수 있는 최대로 구매함.
 * 성민(33 매매법): 전량 매수 매도, 3일 째 상승하면 전량 매도, 3일 째 하락하면 전량 매수
 * (현금 + 1월 14일의 주가 × 주식 수)로 계산
 */

public class BJ20546_기적의_매매법 {

    private static int n;
    private static int[] stock = new int[14];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 14; i++) {
            stock[i] = Integer.parseInt(st.nextToken());
        }
        int joon = joonHyun();
        int sung = sungMin();

        if (joon > sung) System.out.println("BNP");
        if (joon < sung) System.out.println("TIMING");
        if (joon == sung) System.out.println("SAMESAME");
    }

    private static int joonHyun() {
        int asset = n;
        int count = 0;

        for (int s : stock) {
            if (asset == 0) break;
            count += asset / s;
            asset %= s;
        }
        return stock[stock.length - 1] * count + asset;
    }

    private static int sungMin() {
        int asset = n;
        int count, down, up;
        count = down = up = 0;

        for (int i = 1; i < 14; i++) {
            if (stock[i] > stock[i-1]) {
                down = 0;
                up += 1;
            } else if (stock[i] < stock[i-1]) {
                up = 0;
                down += 1;
            } else {
                up = down = 0;
            }

            if (up == 3 && count != 0) {
                asset += count * stock[i];
                count = 0;
                up = down = 0;
            }
            if (down >= 3) {
                count += asset / stock[i];
                asset %= stock[i];
            }
        }
        return stock[stock.length - 1] * count + asset;
    }
}
