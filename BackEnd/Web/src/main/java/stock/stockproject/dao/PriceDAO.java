package stock.stockproject.dao;

import stock.stockproject.dto.PriceDTO;

import java.util.List;

public interface PriceDAO {
    public List<PriceDTO> getprices(PriceDTO param) throws Exception;
}
