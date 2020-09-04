package stock.stockproject.dao;

import stock.stockproject.dto.NewsDTO;

import java.util.List;

public interface NewsDAO {
    public List<NewsDTO> getTop20() throws Exception;
}
