import React from 'react'
import { Progress } from 'antd';

function PredictedScore({score, upDown}) {
    // console.log({upDown});
    return (
        <>
            { 
            (upDown===1)?
            <Progress type="circle" percent={score} format={() => `▲상승`} width={150} status="exception" />  
            :
            <Progress type="circle" percent={score} format={() => `▼하락` } width={150}
            />
            }
        </>
    )
}

export default PredictedScore
