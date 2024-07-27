
import pandas as pd
def get_top_headlines(newsapi,search_category: str,keywords:str,country:str):
    
    top_headlines = newsapi.get_top_headlines(q=keywords,                                   
                                          category=search_category,
                                          language='en',
                                          country=country)
    df=pd.DataFrame(top_headlines['articles'])
    print(df)
  
    
def get_top_headlines_by_source_keyword(newsapi,keywords:str,source:str):
    
    top_headlines = newsapi.get_top_headlines(q=keywords,                                   
                                          language='en',
                                          sources=source)
    df=pd.DataFrame(top_headlines['articles'])
    print(df)
  
def get_top_headlines_by_source(newsapi,source:str):
    
    top_headlines = newsapi.get_top_headlines(                                  
                                          language='en',
                                          sources=source)
    df=pd.DataFrame(top_headlines['articles'])
    print(df)
    
def get_top_headlines_by_category(newsapi,search_category: str,keywords:str):
    
    top_headlines = newsapi.get_top_headlines(q=keywords,                                   
                                          category=search_category,
                                          language='en'
                                          )
    df=pd.DataFrame(top_headlines['articles'])
    print(df)
    
def get_top_headlines_by_country(newsapi,keywords:str,country:str):
    
    top_headlines = newsapi.get_top_headlines(q=keywords,                                   
                                          language='en',
                                          country=country)
    df=pd.DataFrame(top_headlines['articles'])
    print(df)
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