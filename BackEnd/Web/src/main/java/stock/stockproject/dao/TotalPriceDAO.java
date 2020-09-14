package stock.stockproject.dao;

import stock.stockproject.dto.TotalPriceDTO;

import java.util.List;

public interface TotalPriceDAO {
    public List<TotalPriceDTO> get_total_prices() throws Exception;
}
