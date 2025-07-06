# -*- coding: utf-8 -*-
import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?language=en-US".format(movie_id)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0ZTIxZjM1NWJmYTNiZmNiYjA5NzE2Y2Q1NTc4NGM5ZCIsIm5iZiI6MTc1MTc4OTU1OS4zMjYwMDAyLCJzdWIiOiI2ODZhMmZmNzJlNGYxMDAyNDI5YTNiOTYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0.dHi0qRxNz955nFORZcypPZViiMgKhHHyLMs-JAfA5nI"
    }

    response = requests.get(url, headers=headers)

    data = response.json()
    return "https://image.tmdb.org/t/p/original/"+ data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list =sorted(list(enumerate(distances)),reverse=True,key = lambda x : x[1])[1:6]


    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        #fetch poster
        recommended_movies_poster.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies,recommended_movies_poster
        
        
movies_dict = pickle.load(open("movies_dict.pkl",'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open("similarity.pkl",'rb'))


st.title('🎬 Movie Recommender System')

option = st.selectbox('Which movie to select',
                      movies['title'].values)

if st.button('Recommend'):
    names,poster = recommend(option)
    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
        
