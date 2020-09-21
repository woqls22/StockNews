import React from 'react'
import { Typography } from 'antd';

const RankingItem = ({ item, index }  ) => {
    const companies = item.companies;
    const result = item.result;
    const label = (item.model1 == '1') ? '▲상승':'▼하락';
    const ranking = index;

    return (
        <li>
            <Typography.Paragraph>{ranking+1}.  {companies} {label}, 예측 지수: {result}</Typography.Paragraph>
        </li>
    )
}

export default RankingItem