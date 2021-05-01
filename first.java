import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		System.out.println("과목수");
		int cnt = sc.nextInt();
		int[] n = new int[cnt];
		

		int sum = 0;
		int avg = 0;

		for (int i = 0; i < n.length; i++) {
			System.out.println((i + 1) + "번째과목");
			n[i] = sc.nextInt();
		}
		for (int i = 0; i < n.length; i++) {
			sum += n[i];
		}
		avg = sum / cnt;
		System.out.println(sum / cnt);

	}
}
