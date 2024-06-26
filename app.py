import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_image(movie_id):
    response = requests.get('https://www.myapifilms.com/imdb/image/{}?token=9ae9799f-5462-434d-80ab-68462ba4cd6c'.format(movie_id))
    data = response.json()
    # st.text('https://www.myapifilms.com/imdb/image/{}?token=9ae9799f-5462-434d-80ab-68462ba4cd6c'.format(movie_id))
    # return data['urlPoster']

# this function will return 5 similar movies to the given movie
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_image(movie_id))

    return recommended_movies, recommended_movies_posters

movie_dict = pickle.load(open('movie_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select a Movie for Recommendations:",
    movies['title'].values)

if st.button("Recommend"):
    recommendations, posters = recommend(selected_movie_name)

    # col1, col2, col3, col4, col5 = st.columns(5)
    #
    # with col1:
    #     st.header(recommendations[0])
    #     st.image(posters[0])
    # with col2:
    #     st.header(recommendations[1])
    #     st.image(posters[1])
    # with col3:
    #     st.header(recommendations[2])
    #     st.image(posters[2])
    # with col4:
    #     st.header(recommendations[3])
    #     st.image(posters[3])
    # with col5:
    #     st.header(recommendations[4])
    #     st.image(posters[4])

    for recommended_movie in recommendations:
        st.write(recommended_movie)