from textblob import TextBlob
from newspaper import Article

def get_article(website):
    try:
        article = Article(website)
        article.download()
        article.parse()
        article.nlp()
        
        return article.summary
    
    except Exception as e:
        print(f"Error: {e}")
        return None

def analyze_sentiment(text):
    blob = TextBlob(text)
    
    polarity_analysis = blob.sentiment.polarity
    
    return polarity_analysis

def get_sentiment_emoji(polarity_analysis):
    emoji_mapping = {
        -1.0: ("Very Negative", "😡"),
        -0.5: ("Negative", "😟"),
        0.0: ("Neutral", "😐"),
        0.5: ("Positive", "😊"),
        1.0: ("Very Positive", "😄"),
    }
    
    closest_key = min(emoji_mapping.keys(), key=lambda key: abs(polarity_analysis - key))
    
    sentiment_category, sentiment_emoji = emoji_mapping[closest_key]
    
    return f"{sentiment_emoji} {sentiment_category}"
