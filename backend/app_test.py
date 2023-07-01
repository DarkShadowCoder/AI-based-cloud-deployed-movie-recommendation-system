from flask import Flask, render_template, request, flash, jsonify, url_for




####################################################################
#################      Programme Backend       ################
#####################################################################


def GetMoviesByGenres(movies_df, genre):
	# Returns a list of all movies and movie IDs for a particular genre. 
	# It is called whenever a user changes the "Movie Genre" drop-down box

	movies_of_type = movies_df[movies_df['genres'].str.contains(genre)].sort_values('title')
	movie_ids = list(movies_of_type['movieId'].values)
	movie_titles = [str(x)[0:50] for x in list(movies_of_type['title'].values)]
  
	return (movie_ids, movie_titles)


def GetRecommendedMovies(ratings_df , movies_df , user_history_movie_ids):
    movie_df = pd.read_csv(movies_dir / "movies.csv")

    # Let us get a user and see the top recommendations.
    user_id = df.userId.sample(1).iloc[0]
    movies_watched_by_user = df[df.userId == user_id]
    movies_not_watched = movie_df[
        ~movie_df["movieId"].isin(movies_watched_by_user.movieId.values)
    ]["movieId"]
    movies_not_watched = list(
        set(movies_not_watched).intersection(set(movie2movie_encoded.keys()))
    )
    movies_not_watched = [[movie2movie_encoded.get(x)] for x in movies_not_watched]
    user_encoder = user2user_encoded.get(user_id)
    user_movie_array = np.hstack(
        ([[user_encoder]] * len(movies_not_watched), movies_not_watched)
    )
    ratings = model.predict(user_movie_array).flatten()
    top_ratings_indices = ratings.argsort()[-10:][::-1]
    recommended_movie_ids = [
        movie_encoded2movie.get(movies_not_watched[x][0]) for x in top_ratings_indices
    ]

    print("Showing recommendations for user: {}".format(user_id))
    print("====" * 9)
    print("Movies with high ratings from user")
    print("----" * 8)
    top_movies_user = (
        movies_watched_by_user.sort_values(by="rating", ascending=False)
        .head(5)
        .movieId.values
    )
    movie_df_rows = movie_df[movie_df["movieId"].isin(top_movies_user)]
    for row in movie_df_rows.itertuples():
        print(row.title, ":", row.genres)

    print("----" * 8)
    print("Top 10 movie recommendations")
    print("----" * 8)
    recommended_movies = movie_df[movie_df["movieId"].isin(recommended_movie_ids)]
    for row in recommended_movies.itertuples():
        print(row.title, ":", row.genres)



app  = Flask(__name__)
@app.route('/')
def api():
    return(
        {"userId":"1",
        "title":"Flask React Application",
        "completed":False}
    )

if __name__ == '__main__':
    app.run(debug=True)