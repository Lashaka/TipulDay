import constants.constants as const
import requests
from bs4 import BeautifulSoup


class Collect_websites(object):
    def __init__(
        self,
        AMOUNT_OF_WEBSITES_TO_SEND_FORMS_TO: int,
        SEARCH_STRING: str,
        websites: list,
        SearchStartNum: int,
    ) -> None:
        self.SearchStartNum = SearchStartNum
        self.AMOUNT_OF_WEBSITES_TO_SEND_FORMS_TO = AMOUNT_OF_WEBSITES_TO_SEND_FORMS_TO
        self.SEARCH_STRING = SEARCH_STRING
        self.websites = websites

    def collect_and_append_websites(self: object) -> list:
        """
        Collects websites from the google search and appends them to a list named websites.

        Args:
            self: The class object.

        Returns:
            A list of websites.
        """
        self.SEARCH_STRING = self.SEARCH_STRING.replace(" ", "+")
        for i in range(self.AMOUNT_OF_WEBSITES_TO_SEND_FORMS_TO):
            url = f"https://www.google.com/search?q={self.SEARCH_STRING}&start={self.SearchStartNum}"
            response = requests.get(url, headers=const.HEADERS)
            soup = BeautifulSoup(response.text, "html.parser")
            for link in soup.find_all("a"):
                if link.get("href"):
                    self.websites.append(link.get("href"))
                    if "http" not in self.websites[-1]:
                        self.websites.remove(link.get("href"))
                    elif "google" in self.websites[-1]:
                        self.websites.remove(link.get("href"))
            self.SearchStartNum = self.SearchStartNum + 10
            
            return self.websites, url
