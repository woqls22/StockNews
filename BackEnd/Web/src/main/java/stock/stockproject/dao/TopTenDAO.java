package stock.stockproject.dao;

import stock.stockproject.dto.TopTenDTO;

import java.util.List;

public interface TopTenDAO {
    public List<TopTenDTO> get_topten() throws Exception;
}
