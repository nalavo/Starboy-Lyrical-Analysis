# ⭐️The Weeknd - Starboy Lyrics Analysis

I built this using Streamlit to create an interactive web app that analyzes word frequency and sentiment across the entire album. 

## What it does

### Word Trend Analysis
- Shows you the most used words across the whole album
- You can filter by individual songs to see what words dominate each track
- Automatically cleans out the boring stuff like "the", "and", "hahaha", etc.
- Gives you clean, easy-to-read charts

### Sentiment Analysis  
- Breaks down lyrics into positive vs negative emotions
- Green bars = happy/positive words
- Red bars = sad/negative words
- You can filter by just positive or just negative words
- Works for the whole album or individual songs

## How to run it

### What you need
- Python 3.7+

### Setup
1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/starboy-analysis.git
   cd starboy-analysis
   ```

2. Install the packages:
   ```bash
   pip install streamlit pandas matplotlib textblob nltk
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

4. Open your browser to the URL it shows (usually http://localhost:8501)

## How to use it

### Word Trend Tab
1. Pick a song from the dropdown (or leave it on "All Songs")
2. Look at the chart - longer bars = more frequent words
3. Check the table below for exact numbers

### Sentiment Tab  
1. Choose a song (or "All Songs")
2. Pick your filter: All, Good, or Bad emotions
3. Green bars = positive words, red bars = negative
4. The legend explains the colors

## Technical stuff

### How it processes the data
- Strips out punctuation and makes everything lowercase
- Removes common words like "the", "and", "is"
- Filters out non-lyrical stuff like "chorus", "verse", "hahaha"
- Uses regex to catch laughter words and vowel-only words

### What counts as positive vs negative
- **Positive**: love, feel, great, shine, real, good, etc.
- **Negative**: pain, hate, hurt, devil, dead, fight, etc.

### Built with
- **Streamlit** - makes the web interface
- **Pandas** - handles the data
- **Matplotlib** - creates the charts
- **TextBlob** - does sentiment analysis
- **NLTK** - natural language processing

## Project files
```
starboy-analysis/
├── app.py              # The main app
├── lyrics_sentiment.csv # The lyrics data
├── utils.py            # Helper functions
├── README.md           # This file
└── .gitignore          # Tells git what to ignore
```

## Why I built this
I wanted to see what patterns emerge when you analyze The Weeknd's lyrics. Which words does he repeat? What emotions dominate each song? Etc. Etc.

Great for:
- Music analysis projects
- Learning data visualization
- Understanding sentiment analysis
- Just geeking out over The Weeknd's lyrics

Feel free to fork this, add features, or use it as inspiration for your own projects!

