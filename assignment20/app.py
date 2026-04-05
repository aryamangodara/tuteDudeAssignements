import streamlit as st
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ========================
# Page Configuration
# ========================
st.set_page_config(
    page_title="📚 Book Recommendation System",
    page_icon="📖",
    layout="wide"
)

st.title("📚 Book Recommendation System")
st.markdown("### Content-Based Recommendations using TF-IDF + Cosine Similarity")

# ========================
# Download NLTK Resources
# ========================
@st.cache_resource
def download_nltk():
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)

download_nltk()

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# ========================
# NLP Preprocessing Function
# ========================
def nlp_preprocess(text):
    if not isinstance(text, str):
        return ""
    
    text = text.lower()
    text = re.sub(r'http[s]?://\S+|www\.\S+', '', text)
    text = re.sub(r'\S+@\S+\.\S+', '', text)
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    text = ' '.join(text.split())
    
    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]
    lemmatized = [lemmatizer.lemmatize(word) for word in words]
    
    return ' '.join(lemmatized)

# ========================
# Load and Preprocess Data
# ========================
@st.cache_data
def load_and_preprocess_data():
    df = pd.read_csv("books.csv", engine='python', on_bad_lines='skip')
    
    # Filter English books
    if 'language_code' in df.columns:
        df = df[df['language_code'] == 'eng'].copy()
    else:
        st.warning("No 'language_code' column found. Using all books.")
    
    # Create a combined 'features' column from available text columns
    df = df.copy()
    
    # Use columns that actually exist in your CSV
    text_columns = []
    if 'title' in df.columns:
        text_columns.append(df['title'])
    if 'authors' in df.columns:
        text_columns.append(df['authors'])
    if 'features' in df.columns:           # In case it exists
        text_columns.append(df['features'])
    
    # Combine them into one text column for better recommendations
    df['combined_text'] = pd.concat(text_columns, axis=1).fillna('').agg(' '.join, axis=1)
    
    # Apply preprocessing
    df['final_clean_text'] = df['combined_text'].apply(nlp_preprocess)
    
    # Keep only necessary columns for display
    keep_cols = ['bookID', 'title', 'authors']
    if 'features' in df.columns:
        keep_cols.append('features')
    
    df = df[keep_cols + ['final_clean_text', 'combined_text']].copy()
    
    return df

df = load_and_preprocess_data()

# ========================
# Build TF-IDF and Cosine Similarity
# ========================
@st.cache_resource
def build_recommender(_df):
    tfidf = TfidfVectorizer(
        max_features=5000,
        ngram_range=(1, 2),
        stop_words='english',
        min_df=2
    )
    
    tfidf_matrix = tfidf.fit_transform(_df['final_clean_text'])
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    return tfidf, cosine_sim

tfidf_vectorizer, cosine_sim_matrix = build_recommender(df)

# ========================
# Recommendation Function
# ========================
def recommend_books(selected_title, top_n=5):
    matching = df[df['title'] == selected_title]
    if matching.empty:
        return None
    idx = matching.index[0]
    
    sim_scores = list(enumerate(cosine_sim_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n + 1]
    
    book_indices = [i[0] for i in sim_scores]
    
    recommendations = df.iloc[book_indices][['title', 'authors']].copy()
    recommendations['similarity_score'] = [round(score[1] * 100, 2) for score in sim_scores]
    
    return recommendations

# ========================
# Streamlit UI
# ========================

col1, col2 = st.columns([3, 1])

with col1:
    st.subheader("Select a Book")
    selected_book = st.selectbox(
        "Choose a book to get similar recommendations:",
        options=df['title'].tolist(),
        index=0
    )

with col2:
    st.subheader("Number of Recommendations")
    top_n = st.slider("How many recommendations?", min_value=3, max_value=10, value=5)

if st.button("🔍 Get Recommendations", type="primary", use_container_width=True):
    with st.spinner("Finding similar books..."):
        recommendations = recommend_books(selected_book, top_n=top_n)
    
    if recommendations is None:
        st.error("Book not found!")
    else:
        st.success(f"**Recommendations for:** {selected_book}")
        
        for i, row in recommendations.iterrows():
            with st.container(border=True):
                col_a, col_b = st.columns([4, 1])
                with col_a:
                    st.write(f"**{row['title']}**")
                    st.caption(f"by {row['authors']}")
                with col_b:
                    st.metric("Match", f"{row['similarity_score']}%")
        
        st.balloons()

# ========================
# Sidebar
# ========================
with st.sidebar:
    st.header("About")
    st.info("This app creates recommendations by combining **title + authors** (and features if available) "
            "into a single text, then uses TF-IDF + Cosine Similarity.")
    
    st.subheader("Dataset Info")
    st.write(f"**Total Books Loaded:** {len(df):,}")
    
    if st.checkbox("Show Sample Data"):
        st.dataframe(
            df[['title', 'authors', 'final_clean_text']].head(5),
            use_container_width=True,
            hide_index=True
        )

st.caption("Fixed version | Features column error resolved")