import { Descriptions } from 'antd';
import React from 'react'


const PredictedResults = ({ prediction, SetScore, SetupDown }) => {
    console.log(prediction);
    if(!prediction) {
        return;
    }
    const item = {
        company: prediction.company, 
        codes: prediction.Codes, 
        prices: prediction.Prices, 
        volumes: prediction.Volumes,
        BPS: parseInt(prediction.BPS),
        PER: parseInt(prediction.PER),
        EPS: parseInt(prediction.EPS),
        PBR: parseInt(prediction.PBR),
        result: parseInt(prediction.result),
    }
    SetupDown(
        parseInt(prediction.model1)
    );
    SetScore(
        Math.round(
            ((item.result-40)/(67-40))*100
        ));
    return (
        <>
            <Descriptions title={item.company} bordered >
                {/* <Descriptions.Item label="기관코드">{item.codes}</Descriptions.Item> */}
                <Descriptions.Item label="종가">{Math.round(item.prices)}</Descriptions.Item>
                <Descriptions.Item label="거래량">{Math.round(item.volumes)}</Descriptions.Item>
                <Descriptions.Item label="BPS">{Math.round(item.BPS).toFixed(2)}</Descriptions.Item>
                <Descriptions.Item label="PER">{Math.round(item.PER).toFixed(2)}</Descriptions.Item>
                <Descriptions.Item label="EPS">{Math.round(item.EPS).toFixed(2)}</Descriptions.Item>
                <Descriptions.Item label="PBR">{Math.round(item.PBR).toFixed(2)}</Descriptions.Item>
            </Descriptions>,
        </>
    )
}

export default PredictedResults