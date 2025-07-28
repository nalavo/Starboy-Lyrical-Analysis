import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter
from matplotlib.patches import Patch

# Make content full width
st.markdown("""
    <style>
        .block-container {
            max-width: 60vw !important;
            padding-left: 2vw;
            padding-right: 2vw;
        }
        .css-1lcbmhc, .css-1y4p8pa {
            width: 100% !important;
        }
        
        /* Table styling */
        .stDataFrame {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
            font-size: 17px !important;
            border-collapse: collapse !important;
            width: 100% !important;
            margin: 20px 0 !important;
            text-align: left !important;
        }
        
        .stDataFrame th, .stDataFrame td {
            text-align: left !important;
            padding: 13px 10px !important;
            border: 1px solid #333 !important;
            background-color: #000000 !important;
            color: #ffffff !important;
            font-size: 17px !important;
        }
        
        .stDataFrame th {
            font-weight: bold !important;
            padding: 15px 10px !important;
        }
        
        .stDataFrame tr:nth-child(even) {
            background-color: #111111 !important;
        }
        
        .stDataFrame tr:hover {
            background-color: #222222 !important;
        }
        
        /* General text styling */
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
            color: #ffffff !important;
            margin-bottom: 15px !important;
        }
        
        h1 { font-size: 3.2em !important; font-weight: bold !important; }
        h2 { font-size: 2.7em !important; font-weight: bold !important; }
        h3 { font-size: 2.2em !important; font-weight: bold !important; }
        
        /* Selectbox styling */
        .stSelectbox {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
            font-size: 19px !important;
            color: #ffffff !important;
        }
        
        /* General paragraph and text styling */
        p, div, span {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
            font-size: 19px !important;
            line-height: 1.6 !important;
            color: #ffffff !important;
        }
        
        /* Subheader styling */
        .css-1d391kg {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
            font-size: 2.2em !important;
            font-weight: bold !important;
            color: #ffffff !important;
            margin-bottom: 20px !important;
        }
        
        /* Background color for the entire app */
        .main .block-container {
            background-color: #000000 !important;
        }
        
        /* Streamlit elements styling */
        .stMarkdown {
            color: #ffffff !important;
        }
        
        .stSelectbox > div > div, .stSelectbox > div > div > div {
            background-color: #000000 !important;
            color: #ffffff !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("⭐️ The Weeknd - Starboy Lyrics Analysis")

# Load sentiment data
df = pd.read_csv("lyrics_sentiment.csv")

# Create tabs
tab1, tab2 = st.tabs(["Word Trend Analysis", "Sentiment Analysis"])

with tab1:
    st.subheader("Word Trend Analysis")
    
    # Add song filter for word trend
    selected_song_trend = st.selectbox("Filter by Song", ["All Songs"] + list(df["title"].unique()), key="trend_song_filter")
    
    def get_all_words(text):
        # Clean text and split into words
        text = re.sub(r'[^\w\s]', '', text.lower())
        words = text.split()
        
        # Remove common stop words and non-lyrical words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them', 'my', 'your', 'his', 'her', 'its', 'our', 'their', 'mine', 'yours', 'hers', 'ours', 'theirs', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should', 'may', 'might', 'can', 'must', 'shall', 'ought'}
        non_lyrical_words = {'chorus', 'verse', 'yeah', 'oh', 'uh', 'um', 'hmm', 'mmm', 'woah', 'whoa', 'ooh', 'ah', 'eh', 'huh', 'nuh', 'dun', 'gonna', 'wanna', 'gotta', 'lemme', 'gimme', 'cause', 'cuz', 'cos', 'bout', 'nothin', 'somethin', 'everythin', 'anythin', 'nobody', 'somebody', 'everybody', 'anybody', 'dont', 'cant', 'wont', 'aint', 'im', 'ive', 'youre', 'youve', 'hes', 'shes', 'its', 'were', 'theyre', 'theyve', 'weve', 'ive', 'youll', 'hell', 'shell', 'theyll', 'well'}
        
        # Filter words
        filtered_words = []
        for word in words:
            if (word not in stop_words and 
                word not in non_lyrical_words and 
                len(word) > 2 and
                not re.match(r'^h+a+$', word) and  # Remove "ha" repetitions
                not re.match(r'^[aeiou]+$', word) and  # Remove vowel-only words
                not re.match(r'^[ha]+$', word)):  # Remove "h" and "a" combinations
                filtered_words.append(word)
        
        return filtered_words
    
    # Get all words from lyrics based on song filter
    if selected_song_trend == "All Songs":
        all_words = []
        for lyrics in df['lyrics']:
            all_words.extend(get_all_words(str(lyrics)))
        chart_title = "Most Used Words in Starboy Album"
    else:
        song_lyrics = df[df["title"] == selected_song_trend]["lyrics"].values[0]
        all_words = get_all_words(str(song_lyrics))
        chart_title = f"Most Used Words in {selected_song_trend}"
    
    # Count word frequency and create chart
    word_counts = Counter(all_words)
    word_trend_df = pd.DataFrame(word_counts.most_common(20), columns=['Word', 'Count'])
    
    # Create horizontal bar chart
    fig2, ax2 = plt.subplots(figsize=(20, 12))
    ax2.barh(word_trend_df['Word'], word_trend_df['Count'], color='steelblue')
    ax2.set_xlabel('Count', fontsize=14)
    ax2.set_ylabel('Word', fontsize=14)
    ax2.set_title(chart_title, fontsize=16)
    ax2.tick_params(axis='y', labelsize=14)
    ax2.tick_params(axis='x', labelsize=12)
    ax2.invert_yaxis()
    
    st.pyplot(fig2, use_container_width=True)
    
    # Show the word trend table
    word_trend_df.index = range(1, len(word_trend_df) + 1)
    st.dataframe(word_trend_df)

with tab2:
    st.subheader("Sentiment Analysis")
    
    # Define strong sentiment words
    strong_words = [
        "pain", "heartbreak", "sadness", "numb", "broken", "hurt", "cry", "alone", "suffer", "regret", "lost", "cold", "silence", "drown", "fade", "dead", "inside",
        "love", "lust", "desire", "addicted", "crave", "touch", "feel", "temptation", "passion", "want", "kiss", "need", "intimacy", "vulnerable",
        "anger", "savage", "devil", "twisted", "demons", "hate", "enemy", "betrayal", "fight", "rage", "chaos",
        "emptiness", "detachment", "isolation", "hollow", "ghost", "empty", "numb", "faded", "distant", "gone", "echo", "cold", "shadows",
        "mental", "existential", "struggle", "overdose", "control", "mind", "sin", "fear", "trapped", "lost", "escape", "confused", "real", "fake", "identity", "paranoid",
        "shine", "great", "good", "bad", "kill", "sorry", "apologize"
    ]

    def filter_strong_words(text, strong_words):
        words = text.lower().split()
        return [w for w in words if w in strong_words]

    # Process lyrics for sentiment analysis
    df["filtered_words"] = df["lyrics"].apply(lambda x: filter_strong_words(str(x), strong_words))
    all_filtered_words = [word.capitalize() for words in df["filtered_words"] for word in words]
    word_freq = pd.Series(all_filtered_words).value_counts().reset_index()
    word_freq.columns = ["Word", "Count"]

    # Song and sentiment filtering
    selected_song = st.selectbox("Filter by Song", ["All Songs"] + list(df["title"].unique()))

    if selected_song == "All Songs":
        freq_table = word_freq
        chart_title = "Strong Sentiment Word Frequency (All Songs)"
    else:
        song_words = [word.capitalize() for word in filter_strong_words(str(df[df["title"] == selected_song]["lyrics"].values[0]), strong_words)]
        freq_table = pd.Series(song_words).value_counts().reset_index()
        freq_table.columns = ["Word", "Count"]
        chart_title = f"Strong Sentiment Word Frequency ({selected_song})"

    st.subheader(chart_title)

    # Define sentiment categories for color coding
    bad_words = set([
        "pain", "heartbreak", "sadness", "numb", "broken", "hurt", "cry", "alone", "suffer", "regret", "lost", "cold", "silence", "drown", "fade", "dead", "inside",
        "anger", "savage", "devil", "twisted", "demons", "hate", "enemy", "betrayal", "fight", "rage", "chaos", "kill",
        "emptiness", "detachment", "isolation", "hollow", "ghost", "empty", "numb", "faded", "distant", "gone", "echo", "cold", "shadows",
        "mental", "existential", "struggle", "overdose", "sin", "fear", "trapped", "lost", "escape", "confused", "fake", "paranoid", "bad"
    ])
    good_words = set([
        "love", "lust", "desire", "addicted", "crave", "touch", "feel", "temptation", "passion", "want", "kiss", "need", "intimacy", "vulnerable",
        "shine", "great", "good", "real", "control", "mind", "identity", "sorry", "apologize"
    ])

    sentiment_filter = st.selectbox("Filter by Sentiment", ["All", "Good", "Bad"])

    # Filter by sentiment
    if sentiment_filter == "Good":
        freq_table = freq_table[freq_table["Word"].str.lower().isin(good_words)]
    elif sentiment_filter == "Bad":
        freq_table = freq_table[freq_table["Word"].str.lower().isin(bad_words)]

    # Assign colors
    colors = []
    for word in freq_table["Word"].str.lower():
        if word in bad_words:
            colors.append("red")
        elif word in good_words:
            colors.append("green")
        else:
            colors.append("gray")

    # Create horizontal bar chart with legend
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.barh(freq_table["Word"], freq_table["Count"], color=colors)
    ax.set_xlabel("Count", fontsize=14)
    ax.set_ylabel("Word", fontsize=14)
    ax.tick_params(axis='y', labelsize=14)
    ax.tick_params(axis='x', labelsize=12)
    ax.invert_yaxis()
    
    # Add legend
    legend_elements = [
        Patch(facecolor='green', label='Positive'),
        Patch(facecolor='red', label='Negative')
    ]
    ax.legend(handles=legend_elements, loc='lower right')
    
    st.pyplot(fig, use_container_width=True)

    # Show the table
    freq_table.index = range(1, len(freq_table) + 1)
    st.dataframe(freq_table)
