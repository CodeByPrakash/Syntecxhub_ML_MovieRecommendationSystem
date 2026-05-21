# Movies4u - Movie Recommender System

A beautifully designed web application for discovering movie recommendations with a cinema-inspired dark luxury aesthetic, featuring real movie posters from TMDb.

## Preview
![Preview](https://github.com/CodeByPrakash/Syntecxhub_ML_MovieRecommendationSystem/raw/main/preview.png)
![Preview](https://github.com/CodeByPrakash/Syntecxhub_ML_MovieRecommendationSystem/raw/main/preview2.png)
## 🎬 Features

- **Smart Search**: Real-time autocomplete as you type
- **Movie Posters**: High-quality poster images from The Movie Database (TMDb)
- **AI-Powered Recommendations**: Get personalized movie suggestions based on your selection
- **Similarity Scores**: Each recommendation shows how closely matched it is to your choice
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Stunning UI**: Dark luxury theme with smooth animations and interactions
- **Poster Caching**: Efficient caching system to minimize API calls

## 📁 Project Structure

```
project/
├── app.py                 # Flask backend with API endpoints
├── templates/
│   └── index.html         # Main HTML frontend
├── movies.pkl             # Pickled movies list
├── movies_dict.pkl        # Pickled movies dictionary
└── similarity.pkl         # Pickled similarity matrix
```

## 🚀 Setup Instructions

### 1. **Get TMDb API Key** (Optional but Recommended)

To display movie posters, you'll need a free TMDb API key:

1. Go to [https://www.themoviedb.org/settings/api](https://www.themoviedb.org/settings/api)
2. Sign up for a free account (if you don't have one)
3. Go to Settings → API
4. Copy your API key

### 2. **Install Dependencies**

```bash
pip install flask pandas numpy requests
```

### 3. **Project Structure**

Create the following directory structure:
```
project/
├── app.py
├── templates/
│   └── index.html
├── movies.pkl
├── movies_dict.pkl
├── similarity.pkl
└── .env (optional)
```

### 4. **Set Up Environment Variables**

**Option A: Using Environment Variables (Recommended)**

Create a `.env` file in your project root:
```
TMDB_API_KEY=your_api_key_here
```

Then install python-dotenv:
```bash
pip install python-dotenv
```

And update the imports in `app.py`:
```python
from dotenv import load_dotenv
load_dotenv()
```

**Option B: Direct Configuration**

Edit `app.py` and replace:
```python
TMDB_API_KEY = os.getenv('TMDB_API_KEY', 'YOUR_TMDB_API_KEY_HERE')
```

With:
```python
TMDB_API_KEY = 'your_actual_api_key_here'
```

### 5. **Place the HTML file**

- Copy `index.html` to the `templates/` folder
- The Flask app will automatically serve it from there

### 6. **Run the Application**

```bash
python app.py
```

The app will start on `http://localhost:5000`

## 🖼️ Without TMDb API Key

The app will still work without an API key, but:
- Posters won't display (placeholder icons will show instead)
- All recommendations and search functionality will work normally
- You can add the API key later without restarting

## 🔌 API Endpoints

### GET `/`
- Returns the main HTML page

### POST `/api/recommend`
- **Description**: Get movie recommendations with posters
- **Body**: `{"movie_name": "Movie Title", "num_recommendations": 6}`
- **Response**: 
```json
{
  "selected_movie": "Movie Title",
  "selected_poster": "https://image.tmdb.org/t/p/w500/...",
  "recommendations": [
    {
      "title": "Recommended Movie 1",
      "similarity": 95.2,
      "poster": "https://image.tmdb.org/t/p/w500/..."
    }
  ]
}
```

### GET `/api/search?q=query`
- **Description**: Search for movies (autocomplete)
- **Response**: `["Movie 1", "Movie 2", ...]`

### GET `/api/poster/<movie_title>`
- **Description**: Get poster URL for a specific movie
- **Response**: 
```json
{
  "title": "Movie Title",
  "poster": "https://image.tmdb.org/t/p/w500/..."
}
```

### GET `/api/movies`
- **Description**: Get all available movies
- **Response**: `["Movie 1", "Movie 2", ...]`

## 🎨 Design Details

### Aesthetic
- **Theme**: Dark Luxury Cinema
- **Primary Colors**: Gold (#ffd700) + Hot Pink (#ff006e)
- **Typography**: 
  - Headers: `Cinzel` (elegant serif)
  - Body: `Inter` (clean sans-serif)
- **Effects**: 
  - Smooth animations and transitions
  - Backdrop blur effects
  - Gradient overlays
  - Staggered entrance animations

### Key Features
- Animated background with radial gradients
- Card hover effects with elevation
- Loading spinner with smooth rotation
- Error messaging with visual feedback
- Responsive grid layout
- Custom scrollbar styling

## 🔧 Customization

### Add Your TMDb API Key
Edit `app.py`:
```python
TMDB_API_KEY = 'your_api_key_here'
```

Or create a `.env` file:
```
TMDB_API_KEY=your_api_key_here
```

And import at the top of `app.py`:
```python
from dotenv import load_dotenv
load_dotenv()
```

### Change Colors
Edit the CSS variables in `index.html`:
```css
:root {
    --primary: #ffd700;           /* Main gold color */
    --accent: #ff006e;            /* Pink accent */
    --bg-dark: #0a0e27;           /* Dark background */
    --card-bg: #1a1f3a;           /* Card background */
}
```

### Modify Number of Recommendations
In `app.py`, change the default in `get_recommendations()`:
```python
def get_recommendations(movie_name, num_recommendations=6):
```

Or in the JavaScript fetch call in `index.html`:
```javascript
num_recommendations: 6  // Change this number
```

### Adjust Poster Image Size
In `app.py`, modify the poster URL size:
```python
POSTER_BASE_URL = 'https://image.tmdb.org/t/p/w500'  # Options: w92, w154, w185, w342, w500, w780
```

### Add Loading Message
In `index.html`, modify the button text before loading starts.

## 📱 Responsive Behavior

The design automatically adapts to different screen sizes:
- **Desktop** (1200px+): 3-column grid
- **Tablet** (768px-1200px): 2-column grid
- **Mobile** (<768px): Single column, optimized spacing

## 🐛 Troubleshooting

**Posters Not Showing**
- Verify your TMDb API key is correct and valid
- Check that `requests` library is installed: `pip install requests`
- The first search may take longer due to API calls; subsequent searches are cached
- TMDb API has rate limits (40 requests per 10 seconds)

**"Invalid API Key" Error**
- Make sure your `.env` file is in the same directory as `app.py`
- Check that there are no extra spaces in your API key
- Verify the API key from your TMDb account settings
- Restart the Flask app after changing the API key

**Movie not found in TMDb**
- Some movies may not be in TMDb database
- Try searching with alternate titles
- The poster will show a placeholder (🎬) if not found
- All recommendations will still work normally

**Pickle files not loading**
- Verify the file paths in `app.py` are correct
- Check that `movies.pkl`, `movies_dict.pkl`, and `similarity.pkl` exist in the project root
- Ensure the pickle files were created with compatible Python versions

**CORS issues**
- Not applicable for this setup (same-origin requests)
- If deploying to production, adjust CORS headers as needed

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production (Gunicorn)
```bash
pip install gunicorn
gunicorn app:app
```

### Production (Docker)
Create a `Dockerfile`:
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
```

Then:
```bash
docker build -t cinematch .
docker run -p 5000:5000 cinematch
```

## 📊 Dependencies

- **Flask**: Web framework
- **Pandas**: Data manipulation
- **NumPy**: Numerical computations
- **Python 3.8+**: Runtime

## 📝 Notes

- The similarity matrix is precomputed (likely using cosine similarity on movie features)
- The recommendation algorithm returns the most similar movies to the selected title
- All data processing happens server-side for security
- The frontend uses vanilla JavaScript (no frameworks for lightweight performance)

## 🎭 License

MIT License - Feel free to use and modify for your projects!

---

**Happy Watching! 🍿**
=======
# Syntecxhub_ML_MovieRecommendationSystem
