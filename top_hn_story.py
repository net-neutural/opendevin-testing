import requests
from bs4 import BeautifulSoup

def get_top_story():
    url = "https://news.ycombinator.com"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes

    soup = BeautifulSoup(response.content, "html.parser")
    top_story = soup.select_one("table#hnmain tr.athing:nth-of-type(1)")

    if top_story:
        title_link = top_story.select_one("a.titlelink")
        title = title_link.text
        link = title_link["href"]
        score = top_story.find_next_sibling("tr").select_one("span.score").text.split()[0]
        return title, link, score
    else:
        return None, None, None

if __name__ == "__main__":
    title, link, score = get_top_story()
    if title:
        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Points: {score}")
    else:
        print("Could not find the top story.")