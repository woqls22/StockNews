package stock.stockproject.dto;
import java.util.List;
public class PriceDTO {
    private String Company;
    private String DATE_INFO;
    private String END_PRICE;
    private String START_PRICE;
    private String HIGHEST;
    private String LOWEST;
    private String VOLUME;

    public PriceDTO(String company, String DATE_INFO, String END_PRICE, String START_PRICE, String HIGHEST, String LOWEST, String VOLUME) {
        Company = company;
        this.DATE_INFO = DATE_INFO;
        this.END_PRICE = END_PRICE;
        this.START_PRICE = START_PRICE;
        this.HIGHEST = HIGHEST;
        this.LOWEST = LOWEST;
        this.VOLUME = VOLUME;
    }

    public String getCompany() {
        return Company;
    }

    public String getDATE_INFO() {
        return DATE_INFO;
    }

    public String getEND_PRICE() {
        return END_PRICE;
    }

    public String getSTART_PRICE() {
        return START_PRICE;
    }

    public String getHIGHEST() {
        return HIGHEST;
    }

    public String getLOWEST() {
        return LOWEST;
    }

    public String getVOLUME() {
        return VOLUME;
    }
}
