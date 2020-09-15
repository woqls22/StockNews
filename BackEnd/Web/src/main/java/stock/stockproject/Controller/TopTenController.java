package stock.stockproject.Controller;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;
import stock.stockproject.dao.TopTenDAO;

import stock.stockproject.dto.TopTenDTO;
import java.util.List;

@RestController
@MapperScan(basePackages="stock.stockproject.dao")
@ResponseBody
public class TopTenController {
    @Autowired
    private TopTenDAO toptendao;//NewsDAO bean을 자동으로 주입

    @RequestMapping("/topten")
    public List<TopTenDTO> updateTopTen() throws Exception {
        final  List<TopTenDTO> ToptenList = toptendao.get_topten();
        return ToptenList;
    }
}
