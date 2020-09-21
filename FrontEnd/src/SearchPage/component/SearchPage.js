import React, {useState, useEffect} from 'react'
import { Row, Col, Typography} from 'antd';
import SearchInput from  './SearchInput';
import axios from 'axios';
import ShowPrediction from './ShowPrediction';
import './SearchPage.css';
import ShowRankingItems from './ShowRankingItems';

function SearchPage() {
    const [prediction, SetPrediction] = useState(null);
    const [loading, SetLoading] = useState(false);
    const [score , SetScore] = useState(0);
 
    return (
            <div className = 'search-container'>
                <div className = 'title'>
                    <Typography.Title style = {{ fontFamily: 'Caligraphy'}} level ={1}>
                        떡상 기원
                    </Typography.Title>
                </div>
                <div className = 'search-bar'>
                        <SearchInput SetLoading = {SetLoading} SetPrediction = {SetPrediction} />
                </div>
                <div>
                    {(!loading && !prediction)&&<ShowRankingItems />}
                </div>
                <div className = 'result'>
                    {(loading && prediction)&&<ShowPrediction prediction = {prediction} SetScore = {SetScore} score = {score} />}
                </div>
        </div>
    )
}

export default SearchPage