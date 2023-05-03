import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class BJ12933_오리 {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {
        char[] quack = br.readLine().toCharArray();
        char[] sequence = {'q', 'u', 'a', 'c', 'k'};
        boolean[] isVisited = new boolean[quack.length];

        if (quack[0] != 'q' || quack.length % 5 != 0) {
            System.out.println(-1);
            return;
        }

        int num = 0;
        int duck = 0;
        for (int i = 0; i < quack.length; i++) {
            ArrayList<Character> temp = new ArrayList<>();
            for (int j = i; j < quack.length; j++) {
                if (!isVisited[j] && sequence[num % 5] == quack[j]) {
                    num++;
                    temp.add(quack[j]);
                    isVisited[j] = true;
                }
            }
            System.out.println(temp);

            num = 0;
            if (!temp.isEmpty()) {
                if (temp.size() % 5 != 0) {
                    System.out.println(-1);
                    return;
                }
                duck++;
            }
        }
        System.out.println(duck);
    }

//    public static void main(String[] args) throws IOException {
//        String quack = br.readLine();
//        String[] new_quack = quack.split("");
//        List<String> sequence = Arrays.asList("q", "u", "a", "c", "k");
//        Queue<String> queue = new LinkedList<>();
//        queue.addAll(Arrays.asList(new_quack));
//
//        System.out.println(queue);
//        int num = 0;
//        int duck = 1;
//        int time = 0;
//        int len = queue.size();
//        while (!queue.isEmpty()) {
//            time += 1;
//            if (time >= len) {
//                duck = -1;
//                break;
//            }
//
//            String one = queue.poll();
//            if (sequence.get(num % 5).equals(one)) {
//                num += 1;
//            } else {
//                queue.add(one);
//                if (num % 5 == 4) duck += 1;
//            }
//        }
//        System.out.println(duck);
//    }
}