import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int result = 0;
        char[] ch = br.readLine().toCharArray();
        for (int i = 0; i < n; i++) {
            result += Integer.parseInt(String.valueOf(ch[i]));
        }
        System.out.println(result);
    }
}