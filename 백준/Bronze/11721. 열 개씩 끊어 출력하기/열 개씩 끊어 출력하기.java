import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        for(int i = 0 ; i < line.length() ; i+=10) {
            if(i+10 > line.length()) {
                System.out.println(line.substring(i));
            } else {
                System.out.println(line.substring(i,i+10));
            }
        }
    }
}