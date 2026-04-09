import pickle
import streamlit as st

def recommend(movie):
    if movie not in movies['title'].values:
        return []

    index = movies[movies['title'] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movies = []

    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies


st.title("🎬 Movie Recommender System")

movies = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Select a movie",
    movie_list
)

if st.button("Show Recommendation"):
    recommendations = recommend(selected_movie)

    for i, movie in enumerate(recommendations, start=1):
        st.write(f"{i}. {movie}")