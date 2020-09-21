import { Col, Typography } from 'antd'
import React, { useState } from 'react'
import PredictedResults from './PredictedResults'
import PredictedScore from './PredictedScore'

function ShowPrediction({prediction, SetScore, score}) {
    const [upDown , SetupDown] = useState('null');
    return (
        <>
            <Typography.Title level={2}>분석 결과</Typography.Title>
            <PredictedResults prediction = {prediction} SetScore = {SetScore} SetupDown  = {SetupDown}/>
            <div className='score-container'>
                    <PredictedScore score = {score} upDown = {upDown}/>
                <div className='prediction-text'>
                    <br />
                    <br />
                    <Typography.Title level={2}>예측 지수: {score}%</Typography.Title>
                    <p>* 24시간 기준</p>
                </div>
            </div>
        </>
    )
}

export default ShowPrediction
