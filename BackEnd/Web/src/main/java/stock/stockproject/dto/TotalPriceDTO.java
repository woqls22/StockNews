package stock.stockproject.dto;

public class TotalPriceDTO {
    public String name;
    public String Price;
    public String Fluctuation;

    public TotalPriceDTO(String name, String price, String fluctuation) {
        this.name = name;
        Price = price;
        Fluctuation = fluctuation;
    }

    public String getName() {
        return name;
    }

    public String getPrice() {
        return Price;
    }

    public String getFluctuation() {
        return Fluctuation;
    }
}
