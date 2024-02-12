import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    api_key = "your api key"  
    url = f"https://newsapi.org/v2/top-headlines?sources=bbc-news,google-news-in,cnn,fox-news,the-new-york-times,the-hindu,inia-today,ndtv,the-times-of-india,hondustan-times,the-indian-express,zee-news,news18,buisness-today&apiKey={api_key}"
    res = requests.get(url)
    news = res.json()["articles"]
    return render_template('index.html', news=news)
@app.route('/sports.popular')
def index1():
    api_key = "your api key"  
    url1 = f"https://newsapi.org/v2/everything?q=apple&from=2023-01-27&to=2023-01-27&sortBy=popularity&apiKey={api_key}"
    res = requests.get(url1)
    news = res.json()["articles"]
    return render_template('index.html', news=news)
@app.route('/sports2.popular')
def index2():
    api_key = "your api key"  
    url2 = f"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey={api_key}"
    res = requests.get(url2)
    news = res.json()["articles"]
    return render_template('index.html', news=news)
@app.route('/sports3.popular')
def index3():
    api_key = "your api key"  
    url3 = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={api_key}"
    res = requests.get(url3)
    news = res.json()["articles"]
    return render_template('index.html', news=news)
@app.route('/sports4.popular')
def index4():
    api_key = "your api key"  
    url4 = f"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey={api_key}"
    res = requests.get(url4)
    news = res.json()["articles"]
    return render_template('index.html', news=news)
@app.route('/sports5.popular')
def index5():
    api_key = "your api key"  
    url5 = f"https://newsapi.org/v2/top-headlines?country=us&category=sports&apiKey={api_key}"
    res = requests.get(url5)
    news = res.json()["articles"]
    return render_template('index.html', news=news)
if __name__ == '__main__':
    app.run(debug=True)