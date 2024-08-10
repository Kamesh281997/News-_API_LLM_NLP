
from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional
import pandas as pd
from newsapi import NewsApiClient

# Initialize FastAPI
app = FastAPI()

newsapi = NewsApiClient(api_key='5b46d50c9aa44816b1eda337ec1b3871')
# Define request models
class TopHeadlinesRequest(BaseModel):
    keywords: str
    country: Optional[str] = None
    category: Optional[str] = None
    source: Optional[str] = None

@app.get("/top-headlines")
def get_top_headlines(
    keywords: str,
    search_category: Optional[str] = None,
    country: Optional[str] = None
):
    top_headlines = newsapi.get_top_headlines(
        q=keywords,
        category=search_category,
        language='en',
        country=country
    )
    df = pd.DataFrame(top_headlines['articles'])
    return df.to_dict(orient='records')

@app.get("/top-headlines-by-source-keyword")
def get_top_headlines_by_source_keyword(
    keywords: str,
    source: str
):
    top_headlines = newsapi.get_top_headlines(
        q=keywords,
        language='en',
        sources=source
    )
    df = pd.DataFrame(top_headlines['articles'])
    return df.to_dict(orient='records')

@app.get("/top-headlines-by-source")
def get_top_headlines_by_source(
    source: str
):
    top_headlines = newsapi.get_top_headlines(
        language='en',
        sources=source
    )
    df = pd.DataFrame(top_headlines['articles'])
    return df.to_dict(orient='records')

@app.get("/top-headlines-by-category")
def get_top_headlines_by_category(
    keywords: str,
    search_category: str
):
    top_headlines = newsapi.get_top_headlines(
        q=keywords,
        category=search_category,
        language='en'
    )
    df = pd.DataFrame(top_headlines['articles'])
    return df.to_dict(orient='records')

@app.get("/top-headlines-by-country")
def get_top_headlines_by_country(
    keywords: str,
    country: str
):
    top_headlines = newsapi.get_top_headlines(
        q=keywords,
        language='en',
        country=country
    )
    df = pd.DataFrame(top_headlines['articles'])
    return df.to_dict(orient='records')

@app.get("/get_everything")
def get_everything(
    keywords= None,
    source: Optional[str] = None,
    from_date: Optional[str] = None,
    to: Optional[str] = None,
    lang: Optional[str] = None,
    sort_by: Optional[str] = None,
    page: Optional[int] = 1
):
    # Handle default values and optional parameters
    if keywords is None:
        keywords = ''  # Or some default value
    if source is None:
        source = ''  # Or some default value
    if from_date is None:
        from_date = '2000-01-01'  # Or some default value
    if to is None:
        to = '2024-12-31'  # Or some default value
    if lang is None:
        lang = 'en'  # Or some default value
    if sort_by is None:
        sort_by = 'publishedAt'  # Or some default value

    # Call the newsapi function
    all_articles = newsapi.get_everything(
        q=keywords,
        sources=source,
        from_param=from_date,
        to=to,
        language=lang,
        sort_by=sort_by,
        page=page
    )
    # print("all_articles:",all_articles)
    # Convert to DataFrame and return as dict
    df = pd.DataFrame(all_articles)
    df_articles = pd.DataFrame(all_articles['articles'])
    df_source = pd.DataFrame(df_articles['source'])
    # Extract the keys of the dictionaries
    keys = set()
    for item in df_articles['source']:
        keys.update(item.keys())

    # Create new columns based on the keys
    for key in keys:
        df_articles[key] = df_articles['source'].apply(lambda x: x.get(key, None))

    # Drop the original 'info' column
    df_articles = df_articles.drop('source', axis=1)

    

    # pd.DataFrame(df_articles.drop('source',axis=1,inplace=True))
    total_result=df['totalResults'][0]
  
    df_articles.to_csv("all_articles.csv")
    df_source.to_csv("source.csv")
    df_articles.to_csv("df_exclude_csv.csv")
    print("total_result:",total_result)
    return df.to_dict(orient='records')
# http://127.0.0.1:8000/get_everything?keywords=business&from_date=2024-08-01&to=2024-08-09&lang=en&sort_by=relevancy&page=2
# q=keywords,
#                     sources=source,
#                     category=search_category,
#                     language='en',
#                     country=country
# /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2017-12-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)

# # /v2/top-headlines/sources
# sources = newsapi.get_sources()