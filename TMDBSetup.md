# 🎬 CineMatch - Quick Start Guide with TMDb Integration

## 5-Minute Setup

### Step 1: Get Your TMDb API Key (2 minutes)

1. Visit: https://www.themoviedb.org/settings/api
2. Create a free account (or sign in)
3. Accept the terms and click "Create"
4. Choose "Developer" for API usage
5. Fill in the form:
   - App name: "CineMatch"
   - App usage: "Personal Use"
   - Accept terms and click "Submit"
6. Copy your **API Key (v3 auth)**

### Step 2: Configure Your Project (3 minutes)

**Option A: Using .env (Recommended)**

1. Create a file named `.env` in your project folder:
```
TMDB_API_KEY=your_copied_api_key_here
```

2. Install python-dotenv:
```bash
pip install python-dotenv
```

3. Your `app.py` already has the configuration ready!

**Option B: Direct in Code**

1. Open `app.py`
2. Find this line:
```python
TMDB_API_KEY = os.getenv('TMDB_API_KEY', 'YOUR_TMDB_API_KEY_HERE')
```

3. Replace with:
```python
TMDB_API_KEY = 'your_actual_api_key_here'
```

### Step 3: Run the App!

```bash
python app.py
```

Visit: `http://localhost:5000`

---

## File Structure

```
project/
├── app.py                    ← Flask backend (includes TMDb integration)
├── templates/
│   └── index.html            ← Beautiful frontend with poster display
├── movies.pkl                ← Your movie data
├── movies_dict.pkl           ← Movie dictionary
├── similarity.pkl            ← Similarity matrix
└── .env                      ← Your API key (optional but recommended)
```

---

## What You Get

✅ **Movie Posters** - High-quality images from TMDb  
✅ **Smart Search** - Autocomplete with poster preview  
✅ **Beautiful Cards** - Poster-based recommendation cards  
✅ **Selected Movie Display** - Shows the movie you selected with its poster  
✅ **Poster Caching** - API calls cached to minimize requests  
✅ **Fallback Placeholders** - Works without posters if API is down  

---

## Features Explained

### Poster Display
- **Selected Movie**: Large poster shown at the top with gradient effect
- **Recommendations**: 6 movie cards with posters (or 🎬 placeholder)
- **Hover Effects**: Poster zooms on hover for visual feedback
- **Responsive**: Posters adapt to screen size

### Smart Caching
- First search for a movie: Calls TMDb API, caches result
- Same movie searched again: Uses cached poster (instant)
- No internet? Placeholders show, recommendations still work

### Error Handling
- No API key? App works fine, just no posters
- Movie not found on TMDb? Placeholder used
- API rate limit hit? Falls back to placeholders

---

## API Response Example

When you search for a movie, the backend returns:

```json
{
  "selected_movie": "The Matrix",
  "selected_poster": "https://image.tmdb.org/t/p/w500/vgzOg1q2FwWVVGutZNUP6-J7IEp.jpg",
  "recommendations": [
    {
      "title": "The Matrix Reloaded",
      "similarity": 92.5,
      "poster": "https://image.tmdb.org/t/p/w500/..."
    },
    {
      "title": "The Matrix Revolutions",
      "similarity": 91.2,
      "poster": "https://image.tmdb.org/t/p/w500/..."
    }
  ]
}
```

---

## Customization

### Change Poster Size
In `app.py`:
```python
# Options: w92, w154, w185, w342, w500, w780
POSTER_BASE_URL = 'https://image.tmdb.org/t/p/w500'
```

### Disable Posters Temporarily
Set API key to empty:
```python
TMDB_API_KEY = ''
```

### Adjust Number of Recommendations
In `app.py`:
```python
def get_recommendations(movie_name, num_recommendations=6):  # Change 6
```

---

## Troubleshooting

**"No posters showing"**
- Check your API key is correct: https://www.themoviedb.org/settings/api
- Restart Flask app after setting API key
- Check your `.env` file is in the project root (same folder as `app.py`)

**"Movie not found"**
- Some movies may not be in TMDb database
- This is normal; recommendations still work!
- A placeholder (🎬) will show instead

**"API rate limit"**
- TMDb allows 40 requests per 10 seconds
- Caching helps minimize this
- Just wait a moment and try again

**"Connection error"**
- Check your internet connection
- TMDb might be temporarily down
- The app will still work without posters

---

## Next Steps

1. ✅ Run the app
2. ✅ Test with a popular movie (e.g., "The Matrix")
3. ✅ Try the autocomplete search
4. ✅ Check out the recommendations with posters!

**Questions?** Check the full README.md for more details.

---

**Enjoy discovering movies! 🎬🍿**