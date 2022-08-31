import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

st.title("Summarizer")

input_article = st.text_area("Enter article")

if st.button('Create Summary'):
    st.header(input_article)