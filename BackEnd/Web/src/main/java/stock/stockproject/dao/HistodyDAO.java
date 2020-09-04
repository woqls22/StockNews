package stock.stockproject.dao;

import stock.stockproject.dto.HistoryDTO;

import java.util.List;

public interface HistodyDAO {
    List<HistoryDTO> getHistory(HistoryDTO param) throws Exception;
}
