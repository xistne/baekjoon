import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while(true) {
            String line = br.readLine();
            if(line == null) break;
            String[] strArr = line.split(" ");
            if(strArr[0].equals("0") && strArr[1].equals("0")) {
                break;
            }
            System.out.println(Integer.parseInt(strArr[0]) + Integer.parseInt(strArr[1]));
        }

    }
}