import pickle
import time
import streamlit as st
import requests

# ── Page Setup ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="CineFlow - Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# ── Dark background + red headline CSS (minimal) ─────────────────────────────
st.markdown("""
<style>
/* Dark background */
.stApp { background-color: #0d0d0d; color: #ffffff; }
[data-testid="stHeader"] { background-color: #0d0d0d; }

/* Red headline */
h1 { color: #e50914 !important; }

/* Dark selectbox */
div[data-baseweb="select"] > div {
    background-color: #1a1a1a !important;
    border: 1px solid #444 !important;
    color: #fff !important;
}
div[data-baseweb="select"] * { color: #fff !important; }
div[data-baseweb="menu"]    { background-color: #1a1a1a !important; }

/* Dark button */
.stButton > button {
    background-color: #e50914 !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
}
.stButton > button:hover { background-color: #b20710 !important; }

/* White text for captions and labels */
p, label, .stCaption, .stText { color: #cccccc !important; }
</style>
""", unsafe_allow_html=True)

# ── TMDB fetch with retry ────────────────────────────────────────────────────
API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

def fetch_details(movie_id, retries=3):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    for attempt in range(retries):
        try:
            resp = requests.get(url, timeout=10)
            data = resp.json()
            poster_path = data.get('poster_path')
            poster = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None
            rating = round(data.get('vote_average', 0), 1)
            year   = data.get('release_date', 'N/A')[:4]
            return poster, rating, year
        except Exception:
            if attempt < retries - 1:
                time.sleep(1)
    return None, "N/A", "N/A"

# ── Recommend function ───────────────────────────────────────────────────────
def recommend(movie):
    index     = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    names, posters, ratings, years = [], [], [], []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        poster, rating, year = fetch_details(movie_id)
        names.append(movies.iloc[i[0]].title)
        posters.append(poster)
        ratings.append(rating)
        years.append(year)
    return names, posters, ratings, years

# ── Load model ───────────────────────────────────────────────────────────────
@st.cache_resource(show_spinner=False)
def load_model():
    mv  = pickle.load(open('movie_list.pkl', 'rb'))
    sim = pickle.load(open('similarity.pkl', 'rb'))
    return mv, sim

movies, similarity = load_model()

# ── UI ───────────────────────────────────────────────────────────────────────
st.title("🎬 CineFlow")
st.caption("AI-Powered Movie Recommender System")
st.divider()

selected_movie = st.selectbox(
    "🔍 Search or select a movie:",
    sorted(movies['title'].values),
    index=None,
    placeholder="Type a movie name..."
)

if selected_movie:
    sel_id = int(movies[movies['title'] == selected_movie].iloc[0].movie_id)
    sel_poster, sel_rating, sel_year = fetch_details(sel_id)

    # ── Selected movie card ──────────────────────────────────────────────────
    st.subheader("🎥 Selected Movie")
    c1, c2 = st.columns([1, 4])
    with c1:
        if sel_poster:
            st.image(sel_poster, width=180)
        else:
            st.info("Poster not available")
    with c2:
        st.markdown(f"## {selected_movie}")
        st.markdown(f"⭐ **Rating:** {sel_rating} / 10")
        st.markdown(f"📅 **Year:** {sel_year}")
        st.markdown(" ")
        show_rec = st.button("🍿 Show Recommendations")

    st.divider()

    # ── Recommendations ──────────────────────────────────────────────────────
    if show_rec:
        with st.spinner("Finding movies you'll love..."):
            names, posters, ratings, years = recommend(selected_movie)

        st.subheader("✨ Recommended For You")
        cols = st.columns(5)
        for idx, col in enumerate(cols):
            with col:
                if posters[idx]:
                    st.image(posters[idx], use_container_width=True)
                else:
                    st.info("No poster")
                st.markdown(f"**{names[idx]}**")
                st.caption(f"⭐ {ratings[idx]}  |  📅 {years[idx]}")

