import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.*;

public class Main {
  /**
   * Iterate through each line of input.
   */
  public static void main(String[] args) throws IOException {
    InputStreamReader reader = new InputStreamReader(System.in, StandardCharsets.UTF_8);
    BufferedReader in = new BufferedReader(reader);
    String line;
    while ((line = in.readLine()) != null) {
        String[] input = line.split("~");

        int loanAmount = Integer.parseInt(input[0]);
        int years = Integer.parseInt(input[1]);
        float interestRate = Float.parseFloat(input[2]) / 100;
        int downPayment = Integer.parseInt(input[3]);

        double monthlyPayment = calculateMonthlyPayment(loanAmount, years, interestRate, downPayment);
        int totalInterest = calculateTotalInterest(monthlyPayment, years, loanAmount, downPayment);

        System.out.format("$%.2f~$%d", monthlyPayment, totalInterest);
    }
  }

  public static double calculateMonthlyPayment(int loanAmount, int years, float interestRate, int downPayment) {
      double yearlyPayment = (interestRate * (loanAmount - downPayment)) / (1 - Math.pow(1 + interestRate, -years));
      return yearlyPayment / 12;  // convert to monthly payment
  }

  public static int calculateTotalInterest(double monthlyPayment, int years, int loanAmount, int downPayment) {
      double totalInterest = (monthlyPayment * years * 12) - loanAmount + downPayment;
      return (int) totalInterest;
  }
}
