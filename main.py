import pandas as pd
import numpy as np
import streamlit as st 
import os
from dotenv import load_dotenv
load_dotenv()
news_api_key = os.getenv('NEWS_API')