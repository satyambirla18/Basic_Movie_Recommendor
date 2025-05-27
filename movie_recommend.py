import streamlit as st
import pandas as pd
import pickle
st.title("Movie Recommendator")

def recommend(movie):
    movie_idx = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_idx]
    movies_list = sorted(list(enumerate(distances)),reverse = True, key = lambda x:x[1])[1:6]
    recommend_movies = []
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)
    return recommend_movies

movies_dict = pickle.load(open('movies_dict.pkl','rb'))

similarity = pickle.load(open('similarity.pkl','rb'))

movies = pd.DataFrame(movies_dict)

# Dropdown
selected_movie_name = st.selectbox(
    'Enter Movie Names',
    movies['title'].values)

# Button
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)