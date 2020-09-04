package stock.stockproject.Controller;


import java.util.List;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import stock.stockproject.dao.NewsDAO;

import stock.stockproject.dto.NewsDTO;

import java.util.List;


@RestController
@MapperScan(basePackages="stock.stockproject.dao")
@ResponseBody
public class NewsController {
    @Autowired
    private NewsDAO newsDAO;//NewsDAO bean을 자동으로 주입

    @RequestMapping(value="/news")
    public List<NewsDTO> update() throws Exception {
        List<NewsDTO> Top20Newses =newsDAO.getTop20();
        return Top20Newses;
    }

}
