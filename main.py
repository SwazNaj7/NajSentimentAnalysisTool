from textblob import TextBlob
from newspaper import Article
import sys

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

def main():
    while True:
        user_input = input('Enter "article" for an article, "text" for text input, or "exit" to quit: ')
        
        if user_input == 'article':
            website = input('Give article link: ')
            article_text = get_article(website)
            
            if article_text is None:
                print("Failed to retrieve the article. Please check the URL.")
                
            else:
                sentiment_score = analyze_sentiment(article_text)
                sentiment_emoji = get_sentiment_emoji(sentiment_score)
                
                print(f"\n\n\nSentiment Analysis Score: {sentiment_score}")
                print(f"Sentiment Rating: {sentiment_emoji}\n\n")
                
        elif user_input == 'text':
            while True:
                text = input("Enter your text, type 'main' to go back: ")
                
                if text.lower() == 'main':
                    break
                
                article_text = text
                sentiment_score = analyze_sentiment(article_text)
                sentiment_emoji = get_sentiment_emoji(sentiment_score)
                
                print(f"\n\n\nSentiment Analysis Score: {sentiment_score}")
                print(f"Sentiment Rating: {sentiment_emoji}\n\n")
                
        elif user_input == 'exit':
            sys.exit()
            
        else:
            print("Invalid input. Please enter 'article', 'text', or 'exit'.")

if __name__ == "__main__":
    main()
