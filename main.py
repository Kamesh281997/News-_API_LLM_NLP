import pandas as pd
import numpy as np
import streamlit as st 
import os
from dotenv import load_dotenv
<<<<<<< HEAD
from utils.get_news_dataa import *
from newsapi import NewsApiClient
import asyncio

load_dotenv()
news_api_key = os.getenv('NEWS_API')

# Init
newsapi = NewsApiClient(api_key=news_api_key)
get_top_headlines(newsapi,"business","bbc-news","us")
get_top_headlines_by_source_keyword(newsapi,"Olympic","bbc-news")
get_top_headlines_by_source(newsapi,"bbc-news")
get_top_headlines_by_category(newsapi,"business","bbc-news")
get_top_headlines_by_country(newsapi,"bbc-news","us")
=======
load_dotenv()
news_api_key = os.getenv('NEWS_API')
>>>>>>> origin/feature
