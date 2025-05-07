import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample data for Collaborative Filtering (User Movie Ratings)
data = {
    'Movie1': [5, 4, 3, 0, 1],
    'Movie2': [4, 0, 0, 3, 2],
    'Movie3': [0, 4, 5, 4, 0],
    'Movie4': [0, 3, 0, 4, 5],
    'Movie5': [1, 0, 2, 4, 4],
}

# Sample Users
users = ['User1', 'User2', 'User3', 'User4', 'User5']
ratings_df = pd.DataFrame(data, index=users)

# Calculate Cosine Similarity between Users (Collaborative Filtering)
similarity_matrix = cosine_similarity(ratings_df.fillna(0))
similarity_df = pd.DataFrame(similarity_matrix, index=users, columns=users)

# Collaborative Filtering Recommendation Function
def recommend_movies(user, num_recommendations=3):
    similar_users = similarity_df[user].sort_values(ascending=False).drop(user)
    recommended_movies = []

    for similar_user in similar_users.index:
        similar_user_ratings = ratings_df.loc[similar_user]
        for movie, rating in similar_user_ratings.items():
            if rating > 0 and ratings_df.loc[user, movie] == 0:
                recommended_movies.append(movie)

    return list(set(recommended_movies))[:num_recommendations]

# Sample Movie Data for Content-Based Filtering (Genres)
movies = {
    'Movie1': 'Action Thriller',
    'Movie2': 'Action Drama',
    'Movie3': 'Thriller Mystery',
    'Movie4': 'Action Adventure',
    'Movie5': 'Drama Romance',
}

movies_df = pd.DataFrame(list(movies.items()), columns=['Movie', 'Genre'])

# TF-IDF Vectorization of Genres
tfidf = TfidfVectorizer(stop_words='english')
genre_matrix = tfidf.fit_transform(movies_df['Genre'])

# Cosine Similarity based on Genres
genre_similarity = cosine_similarity(genre_matrix, genre_matrix)
genre_similarity_df = pd.DataFrame(genre_similarity, index=movies_df['Movie'], columns=movies_df['Movie'])

# Content-Based Filtering Recommendation Function
def recommend_based_on_genre(movie, num_recommendations=3):
    similar_movies = genre_similarity_df[movie].sort_values(ascending=False)
    return list(similar_movies.index[1:num_recommendations + 1])  # Skip the movie itself

# -----------------------------
# 📥 User Interaction
# -----------------------------
print("🎬 Available Users:", users)
chosen_user = input("Enter a user (e.g., User1): ").strip().title()
if chosen_user not in users:
    print(f"❌ Invalid user: {chosen_user}. Please choose from: {users}")
    exit()

print("\n🎞️ Available Movies:", list(movies.keys()))
chosen_movie = input("Enter a movie (e.g., Movie1): ").strip().title()
if chosen_movie not in movies:
    print(f"❌ Invalid movie: {chosen_movie}. Please choose from: {list(movies.keys())}")
    exit()

# -----------------------------
# 🎯 Output Recommendations
# -----------------------------
print(f"\n📽️ Collaborative Filtering for {chosen_user}: {recommend_movies(chosen_user)}")
print(f"\n🎬 Content-Based Filtering for '{chosen_movie}': {recommend_based_on_genre(chosen_movie)}")