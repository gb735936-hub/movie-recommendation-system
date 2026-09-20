# 🎬 Movie Recommendation System

## 📌 Project Overview

The **Movie Recommendation System** is a machine learning and data analytics project designed to recommend movies to users based on movie characteristics and similarity.

The system analyzes movie information such as **genres, keywords, cast, crew, and other metadata** to identify movies that are similar to a movie selected by the user.

The main goal is to build a simple recommendation engine that can help users discover movies they may enjoy based on their existing preferences.

---

# 🎯 Project Objectives

- Build a content-based movie recommendation system
- Clean and preprocess movie metadata
- Extract useful features from movie information
- Convert textual information into numerical representations
- Calculate similarity between movies
- Recommend similar movies based on user selection
- Create an easy-to-use interface for getting recommendations
- Understand the practical application of machine learning in recommendation systems

---

# 🧠 Recommendation Approach

This project uses a **Content-Based Filtering** approach.

Instead of depending on ratings from other users, the system recommends movies based on the characteristics of the movie selected by the user.

For example:

```text
User selects:
The Dark Knight

        ↓

System analyzes:
Genre
Keywords
Cast
Director
Overview

        ↓

Similarity Calculation

        ↓

Recommended Movies
```

---

# 🔄 Project Workflow

```text
Movie Dataset
      ↓
Data Collection
      ↓
Data Cleaning
      ↓
Feature Selection
      ↓
Feature Engineering
      ↓
Text Processing
      ↓
Feature Vectorization
      ↓
Cosine Similarity
      ↓
Recommendation Engine
      ↓
User Interface
      ↓
Movie Recommendations
```

---

# 🛠️ Technologies Used

| Technology        | Purpose                                     |
| ----------------- | ------------------------------------------- |
| Python            | Development and data processing             |
| Pandas            | Data cleaning and manipulation              |
| NumPy             | Numerical operations                        |
| Scikit-learn      | Machine learning and similarity calculation |
| NLP               | Processing movie metadata                   |
| CountVectorizer   | Converting text into numerical vectors      |
| Cosine Similarity | Measuring movie similarity                  |
| Streamlit         | Interactive user interface                  |
| Jupyter Notebook  | Data exploration and experimentation        |
| Git & GitHub      | Version control                             |

---

# 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── 📁 data/
│   └── movies.csv
│
├── 📁 notebook/
│   └── movie_recommendation.ipynb
│
├── 📁 model/
│   ├── movie_list.pkl
│   └── similarity.pkl
│
├── 📁 app/
│   └── app.py
│
├── 📁 images/
│   └── movie_recommendation.png
│
├── 📄 requirements.txt
├── 📄 README.md
└── 📄 .gitignore
```

---

# 📊 Dataset

The dataset contains information about movies and their characteristics.

Depending on the dataset version, the following information can be included:

* Movie ID
* Movie title
* Genres
* Keywords
* Overview
* Cast
* Crew
* Director
* Production information
* Release information

The movie metadata is combined to create a feature representation for each movie.

---

# 🧹 1. Data Cleaning

The first step was to understand and clean the movie dataset.

### Data cleaning tasks included:

* Checking dataset shape
* Checking missing values
* Removing unnecessary columns
* Handling missing values
* Removing duplicate records
* Converting columns into appropriate formats
* Selecting relevant movie features

Example:

```python
import pandas as pd

movies = pd.read_csv("data/movies.csv")

print(movies.head())
print(movies.info())
print(movies.isnull().sum())

movies = movies.drop_duplicates()
```

---

# 🔍 2. Feature Selection

Relevant movie attributes were selected to determine similarity between movies.

Important features include:

```text
Genres
Keywords
Overview
Cast
Director
```

These features provide information about the content and characteristics of each movie.

---

# ⚙️ 3. Feature Engineering

The selected movie features are combined into a single text representation.

Example:

```python
movies["tags"] = (
    movies["genres"] + " " +
    movies["keywords"] + " " +
    movies["overview"] + " " +
    movies["cast"] + " " +
    movies["director"]
)
```

The combined text is then used to calculate similarities between movies.

---

# 📝 4. Text Vectorization

Machine learning algorithms cannot directly understand raw text.

Therefore, the movie tags are converted into numerical vectors using **CountVectorizer**.

Example:

```python
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(
    max_features=5000,
    stop_words="english"
)

vectors = cv.fit_transform(movies["tags"]).toarray()
```

The result is a numerical representation of each movie based on its textual features.

---

# 📐 5. Cosine Similarity

Cosine similarity is used to measure how similar two movie vectors are.

```python
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vectors)
```

The similarity score generally ranges from:

```text
0 → Completely different
1 → Highly similar
```

The system uses these similarity scores to find movies that are closest to the selected movie.

---

# 🤖 6. Recommendation Function

A recommendation function is created to find movies similar to the movie selected by the user.

Example:

```python
def recommend(movie):

    index = movies[movies["title"] == movie].index[0]

    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    for i in movie_list:
        print(movies.iloc[i[0]].title)
```

Example:

```python
recommend("The Dark Knight")
```

Possible output:

```text
The Dark Knight Rises
Batman Begins
Man of Steel
Iron Man
Watchmen
```

> The actual recommendations depend on the dataset and feature engineering used.

---

# 🎬 7. Recommendation Process

The recommendation process works as follows:

```text
User selects a movie
        ↓
Find movie index
        ↓
Retrieve similarity scores
        ↓
Sort movies by similarity
        ↓
Select top similar movies
        ↓
Display recommendations
```

---

# 🖥️ 8. Streamlit Application

A Streamlit interface can be used to make the recommendation system interactive.

The user selects a movie from a dropdown and clicks the recommendation button.

Example interface:

```text
╔══════════════════════════════════╗
║      🎬 Movie Recommendation     ║
╠══════════════════════════════════╣
║                                  ║
║ Select a Movie                   ║
║                                  ║
║ [ The Dark Knight           ▼ ]  ║
║                                  ║
║        [ Recommend ]              ║
║                                  ║
╚══════════════════════════════════╝
```

The application then displays the recommended movies.

---

# 🚀 Running the Project

## 1. Clone the Repository

```bash
git clone https://github.com/gb735936-hub/Movie-Recommendation-System.git
```

Navigate to the project:

```bash
cd Movie-Recommendation-System
```

---

## 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Run the Streamlit Application

```bash
streamlit run app/app.py
```

The application will open in your browser.

---

# 📋 Requirements

Example `requirements.txt`:

```text
pandas
numpy
scikit-learn
streamlit
```

---

# 📸 Application Preview

Add your application screenshot inside the `images` folder.

```markdown
![Movie Recommendation System](images/movie_recommendation.png)
```

---

# 💡 Example

### Input

```text
The Dark Knight
```

### Recommendation Process

```text
Movie Metadata
      ↓
Feature Combination
      ↓
Vectorization
      ↓
Cosine Similarity
      ↓
Similarity Ranking
```

### Output

```text
Recommended Movies:

1. The Dark Knight Rises
2. Batman Begins
3. Man of Steel
4. Watchmen
5. Iron Man
```

---

# 📊 Key Concepts Demonstrated

This project demonstrates practical understanding of:

* Data Cleaning
* Data Preprocessing
* Feature Engineering
* Natural Language Processing
* Text Vectorization
* Content-Based Filtering
* Cosine Similarity
* Machine Learning
* Recommendation Systems
* Python Programming
* Streamlit Application Development

---

# 🧠 What I Learned

Through this project, I learned how recommendation systems can use machine learning and text-based features to identify similarities between items.

The project helped me understand:

* How raw datasets are prepared for machine learning
* How textual data can be converted into numerical features
* How similarity metrics can be used for recommendations
* How recommendation engines work
* How to connect a machine learning model with a user interface
* How to build and present an end-to-end ML project

---

# 🔮 Future Improvements

The project can be improved by adding:

* ⭐ User rating-based recommendations
* 👤 Personalized recommendations
* 🔥 Trending movie recommendations
* 🎭 Genre-based filtering
* 📅 Release-year filtering
* ⭐ IMDb/TMDB ratings
* 👥 Collaborative filtering
* 🤖 Hybrid recommendation system
* 🎬 Movie posters using an API
* 🔎 Movie search functionality
* ☁️ Cloud deployment
* 📱 Improved Streamlit UI

---

# 🔐 Limitations

The current system is primarily **content-based**, meaning recommendations depend on movie metadata.

It does not fully understand individual user preferences unless those preferences are represented through the selected movie.

The quality of recommendations also depends on:

* Dataset quality
* Available movie metadata
* Feature engineering
* Similarity calculation

---

# 👨‍💻 Author

**Gourav Bhandari**

Data Analyst | Python | SQL | Power BI | Machine Learning

I'm interested in building practical projects that combine **data analytics, machine learning, and business problem-solving**.

---

# ⭐ Conclusion

The Movie Recommendation System demonstrates how machine learning and natural language processing can be used to build a practical recommendation engine.

The project follows an end-to-end workflow:

```text
Data
 ↓
Cleaning
 ↓
Feature Engineering
 ↓
Text Processing
 ↓
Vectorization
 ↓
Similarity Calculation
 ↓
Recommendation
 ↓
Interactive Application
```

This project strengthened my understanding of **Python, data preprocessing, NLP, machine learning, recommendation systems, and Streamlit application development.
