from typing import Generator

import requests
from bs4 import BeautifulSoup


def extract_html(url: str) -> BeautifulSoup:
    with requests.Session() as sess:
        resp = sess.get(url)
        if resp.ok:
            return BeautifulSoup(resp.content, "html.parser")

        raise IOError(f"Unable to get response with status code: {resp.status_code}")


def extract_tags(soup: BeautifulSoup) -> Generator:
    for tag_data in soup.findAll(["h1", "p", "li"], {
        "class": lambda x: x and ("pw-post-body-paragraph" in x.split() or "ka" in x.split() or "jm" in x.split())}):
        yield tag_data.text


def get_text_blocks(url: str):
    soup = extract_html(url)
    blocks = list(extract_tags(soup))
    return blocks


def get_medium_text(url):
    soup = extract_html(url)
    blocks = list(extract_tags(soup))
    return "\n".join(blocks)


if __name__ == "__main__":
    url = "https://medium.com/@ritikjain51/timeseries-anomaly-detection-6f5052cf03e6"
    blocks = get_text_blocks(url)
    print(blocks)
