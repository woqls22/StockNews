package stock.stockproject.dao;
import stock.stockproject.dto.PredictDTO;

import java.util.List;
public interface PredictDAO {
    List<PredictDTO>  getPrediction(PredictDTO param) throws Exception;
}
