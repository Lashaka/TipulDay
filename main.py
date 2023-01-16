import collect_websites
import constants as const
import submit_forms
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
    def __init__(self: object) -> None:
        """
        This function is used to initialize the class.
        """
        ALL_CONSTANTS_IN_LIST = self.get_all_constants()
        self.SEARCH_STRING = ALL_CONSTANTS_IN_LIST[0]
        self.AMOUNT_OF_WEBSITES_TO_SEND_FORMS_TO = ALL_CONSTANTS_IN_LIST[1]
        self.FORM_NAME = ALL_CONSTANTS_IN_LIST[2]
        self.FORM_EMAIL = ALL_CONSTANTS_IN_LIST[3]
        self.FORM_PHONE = ALL_CONSTANTS_IN_LIST[4]
        self.FORM_COMMENT = ALL_CONSTANTS_IN_LIST[5]
        self.ADD_SPECIFIC_WEBSITES = ALL_CONSTANTS_IN_LIST[6]
        self.SearchStartNum = 0
        self.websites = []
        self.SuccessfullForms = 0
        self.FailedForms = 0

    def main(self: object) -> None:
        """
        This is a main method in the main class.

        Args:
            self: The object.

        Returns:
            None.
        """
        if self.ADD_SPECIFIC_WEBSITES:
            self.collect_specific_websites()
        temp = collect_websites.collect_websites(
            SEARCH_STRING=self.SEARCH_STRING,
            SearchStartNum=self.SearchStartNum,
            AMOUNT_OF_WEBSITES_TO_SEND_FORMS_TO=self.AMOUNT_OF_WEBSITES_TO_SEND_FORMS_TO,
            websites=self.websites,
        ).collect_and_append_websites()
        websites = temp[0]
        self.url = temp[1]
        submit_forms.submit_forms(
            formname=self.FORM_NAME,
            formemail=self.FORM_EMAIL,
            formphone=self.FORM_PHONE,
            formcomment=self.FORM_COMMENT,
            websites=websites,
            url=self.url).main()
    def collect_specific_websites(self) -> None:
        """
        This function collects the websites from the file and appends them to the websites list.

        :param self: The object.
        :param websites: The list of websites.
        :return: None
        """
        try:
            with open(const.TXT_FILE_TEXT, "ר") as file:
                for website in file:
                    self.websites.append(website.strip())
        except:
            print(const.COULD_NOT_ADD_THE_WEBSITE_TEXT)
            exit()

    def get_all_constants(self) -> list:
        alldata = __import__("user_settings_util").user_settings_util().get_all_data()
        print(alldata)
        return alldata


if __name__ == "__main__":
    main = main()
    main.main()
