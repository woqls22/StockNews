import React from 'react'

const NewsItem = ({ article }) => {
    const  {headline, text, url, news_info} = article;
    return (
        <li>
            <a href= {url} className ="content">{text}</a>
            <span>{news_info}</span>
        </li>
    )
}

export default NewsItem