from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import numpy as np
import requests
import os 
app = Flask(__name__, template_folder='templates', static_folder='static')

# TMDb API Key
TMDB_API_KEY = os.getenv('TMDB_API_KEY')

# Load the data
try:
    movies_list = pickle.load(open('movies.pkl', 'rb'))
    movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    movies_df = pd.DataFrame(movies_dict)

    movies_titles = movies_df['title'].values.tolist()

    print(f"✓ Loaded {len(movies_titles)} movies")

except Exception as e:
    print(f"✗ Error loading pickle files: {e}")
    movies_titles = []


def fetch_movie_data(movie_id):
    """
    Fetch movie details from TMDb API using movie_id
    """

    try:

        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDB_API_KEY}"

        response = requests.get(url)

        if response.status_code != 200:
            return None

        data = response.json()

        poster_path = data.get("poster_path")

        poster_url = None

        if poster_path:
            poster_url = f"https://image.tmdb.org/t/p/w500/{poster_path}"

        return {
            "poster": poster_url,
            "overview": data.get("overview"),
            "rating": data.get("vote_average"),
            "release_date": data.get("release_date"),
            "runtime": data.get("runtime"),
            "genres": [genre["name"] for genre in data.get("genres", [])]
        }

    except Exception as e:
        print("TMDb Error:", e)
        return None


def get_recommendations(movie_name, num_recommendations=8):

    try:

        if movie_name not in movies_titles:
            return {"error": "Movie not found"}, 404

        movie_index = movies_titles.index(movie_name)

        distances = similarity[movie_index]

        movies_list_sorted = sorted(
            enumerate(distances),
            key=lambda x: x[1],
            reverse=True
        )[1:num_recommendations + 1]

        recommendations = []

        for idx, score in movies_list_sorted:

            if idx < len(movies_titles):

                title = movies_titles[idx]

                movie_id = movies_df.iloc[idx].movie_id

                movie_data = fetch_movie_data(movie_id)

                recommendations.append({
                    'title': title,
                    'movie_id': int(movie_id),
                    'similarity': round(score * 100, 1),
                    'poster': movie_data["poster"] if movie_data else None,
                    'rating': movie_data["rating"] if movie_data else None,
                    'release_date': movie_data["release_date"] if movie_data else None,
                    'runtime': movie_data["runtime"] if movie_data else None,
                    'genres': movie_data["genres"] if movie_data else [],
                    'overview': movie_data["overview"] if movie_data else None
                })

        selected_movie_id = movies_df.iloc[movie_index].movie_id

        selected_movie_data = fetch_movie_data(selected_movie_id)

        return {
            'selected_movie': movie_name,
            'selected_movie_id': int(selected_movie_id),
            'selected_poster': selected_movie_data["poster"] if selected_movie_data else None,
            'selected_rating': selected_movie_data["rating"] if selected_movie_data else None,
            'selected_overview': selected_movie_data["overview"] if selected_movie_data else None,
            'recommendations': recommendations
        }, 200

    except Exception as e:
        return {"error": str(e)}, 500


@app.route('/')
def index():
    return render_template('index.html', movies=movies_titles)


@app.route('/api/recommend', methods=['POST'])
def recommend():

    data = request.get_json()

    movie_name = data.get('movie_name', '')

    num_recommendations = data.get('num_recommendations', 6)

    result, status_code = get_recommendations(
        movie_name,
        num_recommendations
    )

    return jsonify(result), status_code


@app.route('/api/search', methods=['GET'])
def search():

    query = request.args.get('q', '').lower()

    if not query:
        return jsonify([])

    matches = [
        movie for movie in movies_titles
        if query in movie.lower()
    ][:10]

    return jsonify(matches)


@app.route('/api/movie/<int:movie_id>')
def get_movie(movie_id):

    movie_data = fetch_movie_data(movie_id)

    if not movie_data:
        return jsonify({"error": "Movie not found"}), 404

    return jsonify(movie_data)


@app.route('/api/movies', methods=['GET'])
def get_all_movies():
    return jsonify(movies_titles)


@app.route('/api/stats', methods=['GET'])
def stats():

    return jsonify({
        'total_movies': len(movies_titles),
        'tmdb_enabled': True
    })


if __name__ == '__main__':

    print("\n" + "=" * 50)
    print("🎬 CineMatch - Movie Recommender")
    print("=" * 50)
    print(f"✓ Movies loaded: {len(movies_titles)}")
    print("✓ TMDb Poster System Enabled")
    print("✓ Server starting on: http://localhost:5000")
    print("=" * 50 + "\n")

    app.run(debug=True)