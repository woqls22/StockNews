package stock.stockproject.Controller;


import org.mybatis.spring.annotation.MapperScan;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import stock.stockproject.dao.NewsDAO;
import stock.stockproject.dao.PriceDAO;

import stock.stockproject.dto.PriceDTO;

import java.util.List;


@RestController
@MapperScan(basePackages="stock.stockproject.dao")
@ResponseBody
public class PriceController {
    @Autowired
    private PriceDAO pricedao;//NewsDAO bean을 자동으로 주입

    @RequestMapping("/prices")
    public List<PriceDTO> getprice(@RequestParam(value="company", defaultValue = "")String company) throws Exception {
        final PriceDTO param = new PriceDTO(company, null, null,null,null,null, null);
        final  List<PriceDTO> PriceList = pricedao.getprices(param);
        return PriceList;
    }
}
