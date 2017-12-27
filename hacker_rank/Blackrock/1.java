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
        String[] portfolios = line.split("\\|");
        Portfolio port = parsePortfolio(portfolios[0]);
        Portfolio bench = parsePortfolio(portfolios[1]);

        Map<String, Float> portAVs = port.getAVs();
        Map<String, Float> benchAVs = bench.getAVs();

        Map<String, Float> comparedNAVs = comparePercentageNAVs(portAVs, benchAVs);
        String difference = getDifference(comparedNAVs);
        System.out.println(difference);
    }
  }

  public static Portfolio parsePortfolio(String input) {
      String[] portfolioStr = input.split(":");
      String holdings[] = portfolioStr[1].split(";");

      Portfolio portfolio = new Portfolio();
      for (String holding: holdings) {
          portfolio.addHolding(parseHolding(holding));
      }

      return portfolio;
  }

  public static Holding parseHolding(String input) {
      String[] holding = input.split(",");
      return new Holding(
          holding[0],
          Integer.parseInt(holding[1]),
          Integer.parseInt(holding[2])
      );
  }

  public static class Portfolio {
      private List<Holding> holdings;

      public Portfolio() {
          this.holdings = new ArrayList<>();
      }

      public List<Holding> getHoldings() {
          return this.holdings;
      }

      public void addHolding(Holding holding) {
          this.holdings.add(holding);
      }

      private int getNAV() {
          int nav = 0;

          for (Holding holding: this.holdings) {
              nav += holding.getAV();
          }

          return nav;
      }

      private float calculatePercentageNAV(Holding holding) {
          return (float) holding.getAV() / this.getNAV();
      }

      public Map<String, Float> getAVs() {
          Map<String, Float> AVs = new HashMap<>();

          for (Holding holding: this.holdings) {
              AVs.put(holding.getTicker(), this.calculatePercentageNAV(holding));
          }

          return AVs;
      }
  }

  public static class Holding {
      private String ticker;
      private int quantity;
      private int price;

      public Holding(String ticker, int quantity, int price) {
          this.ticker = ticker;
          this.quantity = quantity;
          this.price = price;
      }

      public String getTicker() {
          return this.ticker;
      }

      public int getAV() {
          return this.quantity * this.price;
      }
  }

  public static Map<String, Float> comparePercentageNAVs(Map<String, Float> port, Map<String, Float> bench) {
      Map<String, Float> result = new TreeMap<>();

      for (Map.Entry<String, Float> entry : port.entrySet()) {
          if (bench.containsKey(entry.getKey())) {
              result.put(
                entry.getKey(),
                entry.getValue() - bench.get(entry.getKey())
              );
          }
          else {
              result.put(
                  entry.getKey(),
                  entry.getValue()
              );
          }
      }

      for (Map.Entry<String, Float> entry : bench.entrySet()) {
          if (!port.containsKey(entry.getKey())) {
              result.put(
                entry.getKey(),
                -entry.getValue()
              );
          }
      }

      return result;
  }

  public static String getDifference(Map<String, Float> difference) {
      List<String> result = new ArrayList<>();

      for (Map.Entry<String, Float> entry : difference.entrySet()) {
          // converting to percentage and formatting
          String formattedValue = String.format("%.2f", entry.getValue() * 100);
          result.add(entry.getKey() + ":" + formattedValue);
      }

      return String.join(",", result);
  }
}
