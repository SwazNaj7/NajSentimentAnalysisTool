from flask import Flask, render_template, request, redirect, url_for
from main import analyze_sentiment, get_sentiment_emoji, get_article

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def run_app():
    output = ''

    if request.method == 'POST':
        user_input = request.form.get('input_type')
        input_text = request.form.get('textbox')

        if user_input == 'text':
            sentiment_score = analyze_sentiment(input_text)
            sentiment_emoji = get_sentiment_emoji(sentiment_score)
            output = f"Sentiment Analysis Score: {sentiment_score}\n Sentiment Rating: {sentiment_emoji}"

        elif user_input == 'article':
            website = input_text
            article_text = get_article(website)

            if article_text is None:
                output = "Failed to retrieve the article. Please check the URL."
            else:
                sentiment_score = analyze_sentiment(article_text)
                sentiment_emoji = get_sentiment_emoji(sentiment_score)
                output = f"Sentiment Analysis Score: {sentiment_score}\n Sentiment Rating: {sentiment_emoji}"

    return render_template('index.html', output=output)

@app.route('/article_input', methods=['GET', 'POST'])
def article_input():
    return render_template('article_input.html')

if __name__ == "__main__":
    app.run(debug=True)
