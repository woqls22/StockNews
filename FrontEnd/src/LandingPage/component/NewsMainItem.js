import React from 'react'

const NewsItem = ({ article }) => {
    const  {headline, text, url, news_info} = article;
    return (
        <>
            <a href={url} className ="title">{headline}</a>
            <a href={url} className ="content">{text}</a>
            <span>{news_info}</span>
        </>
    )
}

export default NewsItem
