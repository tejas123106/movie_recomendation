import pickle
import streamlit as st
import lzma   # ✅ IMPORTANT

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

# ✅ Load normal pickle
movies = pickle.load(open('model/movie_list.pkl', 'rb'))

# ✅ FIX: Load compressed LZMA file properly
with lzma.open('model/similarity_lzma.pkl', 'rb') as f:
    similarity = pickle.load(f)

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Select a movie",
    movie_list
)

if st.button("Show Recommendation"):
    recommendations = recommend(selected_movie)

    for i, movie in enumerate(recommendations, start=1):
        st.write(f"{i}. {movie}")