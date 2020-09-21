import { Spin } from 'antd';
import axios from 'axios';
import React, { useEffect, useState } from 'react'
import RankingItem from './RangkingItem';

function ShowRankingItems() {
    const [items, setItem] = useState('');
    const [searchLoading, setSearchLoading] = useState(false);

    useEffect(() => {
        const fetchData = async () => {
            setSearchLoading(true);
            try {
                const response = await axios.get('api/topten');
                setItem(response.data);
            } catch (e) {
            alert(e);
            }
            setSearchLoading(false);
        };
        fetchData();
    }, [])
    
    if (searchLoading) {
        return <Spin tip="Loading..." size="middle" style = {{marginTop:'150px', marginLeft:'50%'}}/>
    }

    if (!items) {
        return null;
    }
    return (
        <ul className = "rangking-list">
            {items.map((item, index) => (
                    <RankingItem key={index} item={item} index={index} />
            ))}
        </ul>
    )
    
}

export default ShowRankingItems
