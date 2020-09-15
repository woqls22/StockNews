package stock.stockproject.dto;

public class TopTenDTO {
    String Companies;
    String Codes;
    String Prices;
    String Volumes;
    String DIVs;
    String BPS;
    String PER;
    String EPS;
    String PBR;
    String model1;
    String model2;
    Float result;

    public TopTenDTO(String companies, String codes, String prices, String volumes, String DIVs, String BPS, String PER, String EPS, String PBR, String model1, String model2, Float result) {
        Companies = companies;
        Codes = codes;
        Prices = prices;
        Volumes = volumes;
        this.DIVs = DIVs;
        this.BPS = BPS;
        this.PER = PER;
        this.EPS = EPS;
        this.PBR = PBR;
        this.model1 = model1;
        this.model2 = model2;
        this.result = result;
    }

    public String getCompanies() {
        return Companies;
    }

    public void setCompanies(String companies) {
        Companies = companies;
    }

    public String getCodes() {
        return Codes;
    }

    public void setCodes(String codes) {
        Codes = codes;
    }

    public String getPrices() {
        return Prices;
    }

    public void setPrices(String prices) {
        Prices = prices;
    }

    public String getVolumes() {
        return Volumes;
    }

    public void setVolumes(String volumes) {
        Volumes = volumes;
    }

    public String getDIVs() {
        return DIVs;
    }

    public void setDIVs(String DIVs) {
        this.DIVs = DIVs;
    }

    public String getBPS() {
        return BPS;
    }

    public void setBPS(String BPS) {
        this.BPS = BPS;
    }

    public String getPER() {
        return PER;
    }

    public void setPER(String PER) {
        this.PER = PER;
    }

    public String getEPS() {
        return EPS;
    }

    public void setEPS(String EPS) {
        this.EPS = EPS;
    }

    public String getPBR() {
        return PBR;
    }

    public void setPBR(String PBR) {
        this.PBR = PBR;
    }

    public String getModel1() {
        return model1;
    }

    public void setModel1(String model1) {
        this.model1 = model1;
    }

    public String getModel2() {
        return model2;
    }

    public void setModel2(String model2) {
        this.model2 = model2;
    }

    public Float getResult() {
        return result;
    }

    public void setResult(Float result) {
        this.result = result;
    }
}
