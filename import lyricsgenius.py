import lyricsgenius
import pandas as pd
import time
import textwrap
from textblob import TextBlob

# Replace with your Genius token
GENIUS_API_TOKEN = "5Necz_0upwaiR3zP-wWu69SlsN3wZ8QBah0B3fUtN5omc8SYFcIy7fsXa1wBlnJD"
genius = lyricsgenius.Genius(GENIUS_API_TOKEN, timeout=15, retries=3)
genius.skip_non_songs = True
genius.excluded_terms = ["(Remix)", "(Live)"]

# Starboy Album Tracklist
starboy_tracks = [
    "Starboy",
    "Party Monster",
    "False Alarm",
    "Reminder",
    "Rockin'",
    "Secrets",
    "True Colors",
    "Stargirl Interlude",
    "Sidewalks",
    "Six Feet Under",
    "Love To Lay",
    "A Lonely Night",
    "Attention",
    "Ordinary Life",
    "Nothing Without You",
    "All I Know",
    "Die for You",
    "I Feel It Coming"
]

# Fetch lyrics and store in a list
lyrics_data = []

for track in starboy_tracks:
    print(f"Fetching: {track}")
    try:
        song = genius.search_song(track, "The Weeknd")
        if song and song.lyrics:
            lyrics_data.append({
                "title": track,
                "lyrics": song.lyrics.replace("\n", " ")
            })
        time.sleep(1)  # Respect API rate limit
    except Exception as e:
        print(f"❌ Error with {track}: {e}")

# ✅ Save to CSV
df = pd.DataFrame(lyrics_data)
df.to_csv("lyrics.csv", index=False)
print("\n✅ Lyrics saved to lyrics.csv")

# Wrap lyrics for readability

df = pd.read_csv("lyrics.csv")

def wrap_lyrics(lyrics, width=80):
    if pd.isna(lyrics):
        return ""
    return "\n".join(textwrap.wrap(lyrics, width=width))

df["lyrics"] = df["lyrics"].apply(wrap_lyrics)
df.to_csv("lyrics_wrapped.csv", index=False, encoding="utf-8")
print("✅ Wrapped lyrics saved to lyrics_wrapped.csv")

# Sentiment analysis

def get_sentiment(lyrics):
    if pd.isna(lyrics) or not lyrics.strip():
        return None
    blob = TextBlob(lyrics)
    return blob.sentiment.polarity

df["sentiment"] = df["lyrics"].apply(get_sentiment)
df.to_csv("lyrics_sentiment.csv", index=False, encoding="utf-8")
print("✅ Sentiment analysis saved to lyrics_sentiment.csv")
