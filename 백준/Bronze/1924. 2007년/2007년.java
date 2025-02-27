import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {
    public static void main(String[] args) throws IOException {
        int[] arrDay = {0,31,28,31,30,31,30,31,31,30,31,30,31};
        String[] arrDaysOfWeek = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        int sum = 0;

        for (int i = 0; i < x; i++) {
            sum += arrDay[i];
        }
        sum += y;
        System.out.println(arrDaysOfWeek[sum%7]);
    }
}