from modules import *
import constants.constants as const
from threading import Thread
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    import_y_n = input(const.PLEASE_INSTALL_PIP_TEXT)
    if import_y_n.lower() == "y":
        import os
        os.system("pip install bs4")
        os.system("pip install requests")
    else:
        exit()


class main(object):
    def __init__(
            self: object,
            SEARCH_STRING:str,
            AMOUNT_OF_WEBSITES_TO_SEND_FORMS_TO:int,
            FORM_NAME:str,
            FORM_EMAIL:str,
            FORM_PHONE:str,
            FORM_COMMENT:str,
            websites,
            console
            ) -> None:
        """
        This function is used to initialize the class.
        """
        self.SEARCH_STRING = SEARCH_STRING
        self.AMOUNT_OF_WEBSITES_TO_SEND_FORMS_TO = AMOUNT_OF_WEBSITES_TO_SEND_FORMS_TO
        self.FORM_NAME = FORM_NAME
        self.FORM_EMAIL = FORM_EMAIL
        self.FORM_PHONE = FORM_PHONE
        self.FORM_COMMENT = FORM_COMMENT
        self.SearchStartNum = 0
        self.websites = websites
        self.SuccessfullForms = 0
        self.FailedForms = 0
        self.console = console

    def main(self: object) -> None:
        """
        This is a main method in the main class.

        Args:
            self: The object.

        Returns:
            None.
        """
        temp = Collect_websites(
            SEARCH_STRING=self.SEARCH_STRING,
            SearchStartNum=self.SearchStartNum,
            AMOUNT_OF_WEBSITES_TO_SEND_FORMS_TO=self.AMOUNT_OF_WEBSITES_TO_SEND_FORMS_TO,
            websites=self.websites,
        ).collect_and_append_websites()
        websites = temp[0]
        self.url = temp[1]
        Thread(Submit_forms(
            formname=self.FORM_NAME,
            formemail=self.FORM_EMAIL,
            formphone=self.FORM_PHONE,
            formcomment=self.FORM_COMMENT,
            websites=websites,
            url=self.url,
            console=self.console).main()).start()




