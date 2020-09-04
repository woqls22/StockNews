package stock.stockproject.dto;

public class HistoryDTO {
    private String company;
    private String headline;
    private String text;
    private String url;
    private String news_info;
    private String Time;

    public HistoryDTO(String company, String headline, String text, String url, String news_info, String time) {
        this.company = company;
        this.headline = headline;
        this.text = text;
        this.url = url;
        this.news_info = news_info;
        Time = time;
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

    public String getTime() {
        return Time;
    }
}
