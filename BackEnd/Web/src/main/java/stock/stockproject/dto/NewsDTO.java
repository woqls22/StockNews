package stock.stockproject.dto;

public class NewsDTO {
    private int rank = 0;
    private String company= "";
    private String headline= "";
    private String text= "";
    private String url= "";
    private String news_info= "";
    public int getRank() {
        return rank;
    }
    public void setRank(int rank) {
        this.rank = rank;
    }
    public void setCompany(String company) {
        this.company = company;
    }
    public void setHeadline(String headline) {
        this.headline = headline;
    }
    public void setText(String text) {
        this.text = text;
    }
    public void setUrl(String url) {
        this.url = url;
    }
    public void setNews_info(String news_info) {
        this.news_info = news_info;
    }
    public String getCompany() {
        return company;
    }
    public String getHeadline() {
        return headline;
    }
    public String getText() {
        return text;
    }
    public String getUrl() {
        return url;
    }
    public String getNews_info() {
        return news_info;
    }
    public NewsDTO(int rank, String company, String headline, String text, String url, String news_info) {
        this.rank = rank;
        this.company = company;
        this.headline = headline;
        this.text = text;
        this.url = url;
        this.news_info = news_info;
    }
}
