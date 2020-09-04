package stock.stockproject.Controller;

import java.util.List;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import stock.stockproject.dao.HistodyDAO;
import stock.stockproject.dto.HistoryDTO;

import java.util.List;
@RestController
@ResponseBody
@MapperScan(basePackages="stock.stockproject.dao")
public class HistoryController {
    @Autowired
    private HistodyDAO histodyDao;//UserDAO bean을 자동으로 주입

    @RequestMapping("/histories")
    public List<HistoryDTO> histories(@RequestParam(value="company", defaultValue = "-")String companyname) throws Exception {
        final HistoryDTO param = new HistoryDTO(companyname, null, null,null,null,null);
        final List<HistoryDTO> NewsList = histodyDao.getHistory(param);
        return NewsList;
    }
}
