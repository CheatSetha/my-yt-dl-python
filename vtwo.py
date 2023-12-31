import requests
from bs4 import BeautifulSoup


def get_short_videos_in_channel(channel_url):
    # Send a GET request to the channel's videos page
    response = requests.get(channel_url)
    soup = BeautifulSoup(response.text, "html.parser")
    # find class= "css-1qb12g8-DivThreeColumnContainer eegew6e2"

    print(soup.find_all("div", class_="css-1qb12g8-DivThreeColumnContainer eegew6e2"))
    # for link in soup.findAll("a"):
    #     print(link.get("href"))


if __name__ == "__main__":
    channel_url = "https://www.tiktok.com/@paputi.uz"
    get_short_videos_in_channel(channel_url)
