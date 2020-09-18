package stock.stockproject.dto;

public class PredictDTO {
    public String company;
    public String Codes;
    public String Prices;
    public String Volumes;
    public String DIVs;
    public String BPS;
    public String PER;
    public String EPS;
    public String PBR;
    public String model1;
    public String model2;
    public String result;

    public PredictDTO(String companies, String codes, String prices, String volumes, String DIVs, String BPS, String PER, String EPS, String PBR, String model1, String model2, String result) {
        company = companies;
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
        return company;
    }

    public String getCodes() {
        return Codes;
    }

    public String getPrices() {
        return Prices;
    }

    public String getVolumes() {
        return Volumes;
    }

    public String getDIVs() {
        return DIVs;
    }

    public String getBPS() {
        return BPS;
    }

    public String getPER() {
        return PER;
    }

    public String getEPS() {
        return EPS;
    }

    public String getPBR() {
        return PBR;
    }

    public String getModel1() {
        return model1;
    }

    public String getModel2() {
        return model2;
    }

    public String getResult() {
        return result;
    }

    public void setCompanies(String companies) {
        company = companies;
    }

    public void setCodes(String codes) {
        Codes = codes;
    }

    public void setPrices(String prices) {
        Prices = prices;
    }

    public void setVolumes(String volumes) {
        Volumes = volumes;
    }

    public void setDIVs(String DIVs) {
        this.DIVs = DIVs;
    }

    public void setBPS(String BPS) {
        this.BPS = BPS;
    }

    public void setPER(String PER) {
        this.PER = PER;
    }

    public void setEPS(String EPS) {
        this.EPS = EPS;
    }

    public void setPBR(String PBR) {
        this.PBR = PBR;
    }

    public void setModel1(String model1) {
        this.model1 = model1;
    }

    public void setModel2(String model2) {
        this.model2 = model2;
    }

    public void setResult(String result) {
        this.result = result;
    }

}
