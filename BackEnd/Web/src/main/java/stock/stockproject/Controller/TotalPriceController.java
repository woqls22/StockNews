package stock.stockproject.Controller;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import stock.stockproject.dao.TotalPriceDAO;

import stock.stockproject.dto.TotalPriceDTO;
import java.util.List;

@RestController
@MapperScan(basePackages="stock.stockproject.dao")
@ResponseBody
public class TotalPriceController {
    @Autowired
    private TotalPriceDAO pricedao;//NewsDAO bean을 자동으로 주입

    @RequestMapping("/totalprices")
    public List<TotalPriceDTO> getprice() throws Exception {
        final  List<TotalPriceDTO> PriceList = pricedao.get_total_prices();
        return PriceList;
    }
}
