import java.io.BufferedReader;
import java.io.InputStreamReader;


public class runSUTLoad {
	public static void runSUTLoad1(String testcases) {
	try {
		Runtime rt = Runtime.getRuntime();
		Process pr = rt.exec(testcases);
		BufferedReader input = new BufferedReader(
				new InputStreamReader(pr.getInputStream()));
		String line = null;
		
		while ((line = input.readLine()) != null) {
			System.out.println(line);
		}

		int exitVal = pr.waitFor();
		System.out.println("Exited with error code " + exitVal);

		} catch(Exception e) {
			System.out.println(e.toString());
			e.printStackTrace();
		}
	}
}
