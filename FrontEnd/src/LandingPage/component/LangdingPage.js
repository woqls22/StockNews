import React, {useEffect, useState} from 'react';
import './LandingPage.css';
import kospi from "../../img/Kospi.jpg";
import kosdaq from "../../img/Kosdaq.jpg";
import NewsItem from './NewsItem';
import NewsMainItem from './NewsMainItem';
import { Spin } from 'antd';
import axios from 'axios';


function LandingPage() {
    const [articles, setArticle] = useState('');
    const [loading, setLoading] = useState(false);
    const [kosPrices, setKosPrices] = useState(0);
    useEffect(() => {
        const fetchData = async () => {
            setLoading(true);
            try {
                const responseArticles = await axios.get('api/news');
                setArticle(responseArticles.data);
                const responseKosPrices = await axios.get('api/totalprices');
                setKosPrices(responseKosPrices.data);
            } catch (e) {
            alert(e);
            }
            setLoading(false);
        };
        fetchData();
    }, [])
    
    if (loading) {
        return <Spin tip="Loading..." size="middle" style = {{marginTop:'200px'}}/>
    }


    if (!articles) {
        return null;
    }
    // console.log(articles.slice(0,1));
    return (
        <> 
        <div className = "landing">
            <div className = "big-board">
                <div className="stock-items" id="kospi">
                    <a>
                        코스피 지수
                        <em>KOSPI</em>
                    </a>
                    <span className="stock-num">
                        <a className = "data-realtime-trade-price">{kosPrices[0].Price}</a>
                    </span>
                    <img src={kospi}/>
                </div>
                <div className="stock-items" id="kosdaq">
                    <a>
                        코스닥 지수
                        <em>KOSDAQ</em>
                    </a>
                    <span className="stock-num">
                        <a className = "data-realtime-trade-price">{kosPrices[1].Price}</a>
                    </span>
                    <img src={kosdaq}/>
                </div>
            </div>
            <div className ="main">
                <div className ="recent-news">
                    <h4>최신 경제 뉴스</h4>
                    <div className = "picked-news-wrap">
                    <NewsMainItem key={articles.slice(0,1)[0].rank} article={articles.slice(0,1)[0]} />
                    </div>
                    <div className = "rest-news-wrap">
                        <ul className = "rest-news-left">
                            {articles.slice(1,6).map(article => (
                                <NewsItem key={article.rank} article={article} />
                            ))}
                        </ul>
                        <ul className = "rest-news-right">
                            {articles.slice(6,11).map(article => (
                                    <NewsItem key={article.rank} article={article} />
                            ))}
                        </ul>
                    </div>
                </div>
            </div>
            </div>
        </>
    )
}

export default LandingPage