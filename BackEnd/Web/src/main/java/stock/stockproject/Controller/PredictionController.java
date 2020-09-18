package stock.stockproject.Controller;
import java.util.List;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import stock.stockproject.dao.PredictDAO;
import stock.stockproject.dto.PredictDTO;
@RestController
@ResponseBody
@MapperScan(basePackages="stock.stockproject.dao")
public class PredictionController {
    @Autowired
    private PredictDAO predictionDao;

    @RequestMapping("/api/prediction")
    public List<PredictDTO>predictions(@RequestParam(value = "company", defaultValue = "-") String company_name) throws Exception{
        final PredictDTO param = new PredictDTO(company_name,null,null,null,null,null,null,null,null,null,null,null);
        final List<PredictDTO> result = predictionDao.getPrediction(param);
        return result;
    }
}
