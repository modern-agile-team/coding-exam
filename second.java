import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) throws ParseException {
		
		Scanner sc = new Scanner(System.in);
		
		String strDate = sc.nextLine();
		
		SimpleDateFormat originFormat = new SimpleDateFormat("HH:mm:ss");
		SimpleDateFormat newFormat_si = new SimpleDateFormat("HH");
		SimpleDateFormat newFormat_bun = new SimpleDateFormat("mm");
		SimpleDateFormat newFormat_cho = new SimpleDateFormat("ss");
		
		
		Date orginDate = originFormat.parse(strDate);
		
		String newDate1 = newFormat_si.format(orginDate);
		String newDate2 = newFormat_bun.format(orginDate);
		String newDate3 = newFormat_cho.format(orginDate);
		
		System.out.println(newDate1+"시"+newDate2+"분"+newDate3+"초");
	}
}
