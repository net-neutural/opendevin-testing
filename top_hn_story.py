import requests
from bs4 import BeautifulSoup

def get_top_story():
    try:
        url = "https://news.ycombinator.com"
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        title_link = soup.select_one("span.titleline > a")
        if title_link:
            title = title_link.text
            link = title_link['href']
        else:
            return "Could not find title link", None, None

        score_element = soup.select_one("span.score")
        if not score_element:
            return "Could not find score element", None, None
        score = score_element.text.split()[0]

        return title, link, score

    except requests.exceptions.RequestException as e:
        return f"Error fetching Hacker News: {e}", None, None


if __name__ == "__main__":
    title, link, score = get_top_story()

    if isinstance(title, str) and title.startswith("Could not") or title.startswith("Error"):
        print(title)
    elif title:
        print(f"Title: {title}")
        print(f"Link: {link}")
        print(f"Points: {score}")