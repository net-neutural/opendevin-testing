from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    stories = get_top_stories()
    return render_template('index.html', stories=stories)

def get_top_stories():
    url = "https://news.ycombinator.com"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    stories = []

    for item in soup.select('.athing')[:5]:  # Get top 5 stories
        title_link = item.select_one('.titleline > a')
        if title_link:
            title = title_link.text
            link = title_link['href']
        else:
            title = "No title"
            link = "#"

        score_element = item.find_next_sibling('tr').select_one('.score')
        score = score_element.text.split()[0] if score_element else "0"

        author_element = item.find_next_sibling('tr').select_one('.hnuser')
        author = author_element.text if author_element else "Unknown"

        comments_element = item.find_next_sibling('tr').select_one('a:contains("comment")')
        comments = comments_element.text.split()[0] if comments_element else "0"

        stories.append({
            'title': title,
            'link': link,
            'score': score,
            'author': author,
            'comments': comments
        })

    return stories

if __name__ == '__main__':
    app.run(debug=True)