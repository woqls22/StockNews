import React, {useState, useEffect} from 'react'
import { Input } from 'antd';
import axios from 'axios';

const { Search } = Input;


function SearchInput({SetLoading, SetPrediction}) {
    const [keyword, SetKeyword] = useState(null);
    useEffect(() => {
        const fetchData = async () => {
            // console.log(`keyword => ${keyword}`);
            try {
                const response = await axios.get(`api/prediction?company=${keyword}`);
                // console.log(`response, reponse.data, prediction`);
                // console.log(response, response.data, response.data[0]);
                if (!response.data.length) {
                    if(keyword) {
                        throw "search fail"
                    }
                    return
                }
                SetPrediction(response.data[0]);
                SetLoading(true);
            } catch (msg) {
                alert(msg);
            }
        };
        fetchData();
    }, [keyword])


    const onSearch = (value) => {
        if(!value) {
            return;
        }
        SetKeyword(value);
    }
    return (
        <>
            <Search
                placeholder="찾고자 하는 기업명을 입력하세요."
                style={{ width: `100%`, margin: 0 }}
                size="large"
                enterButton
                onSearch={onSearch}
                autoFocus
            />
        </>
    )
}

export default SearchInput;