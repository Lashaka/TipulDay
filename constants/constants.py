##############################################
SEARCH_STRING_INPUT_TEXT = "the google search value to submit values into\n recommended 'leave details'/'leave a phone number/Contact restraunts(for restraunt forms submitting)' etc"
AMOUNT_OF_WEBSITES_TO_SEND_FORMS_TO_INPUT_TEXT = "Enter amount of websites to try to submit forums to:\n number of websites is this value x12, note that google has a limit of this search value so from a specific number there will be no change."
ADD_SPECIFIC_SEARCH_WEBSITE_TEXT = (
    "Do you want to add a specific website:\n 1. Yes\n 2. No"
)
ADD_SPECIFIC_SEARCH_WEBSITE_INVALID_INPUT_TEXT = "Invalid input, please try again"
FORM_NAME_TEXT = "Enter the name of the form\n Target first + last name"
FORM_EMAIL_TEXT = (
    "Enter the email of the form\n you can use corob21626@gmail.com as a sample"
)
FORM_PHONE_TEXT = "Enter the phone number of the form\n Target phone number"
FORM_COMMENT_TEXT = "Optional, enter comment. usually not mandatory by most websites, but entering something may increase the submitted forms amount"
##############################################
TXT_FILE_TEXT = "Specific_Websites.txt"
PLEASE_INSTALL_PIP_TEXT = "Please install the requests and bs4 modules or press: y+enter to automatically install them."
COULD_NOT_ADD_THE_WEBSITE_TEXT = "Error 3: Could Not Add the manually entered websites."
##############################################
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
}
WEBSITE_COLLECTED_TEXT = "[*] Websites collected"
##############################################
SUBMIT_FORMS_TEXT = "[*] Submitting forms"
ERROR_5_TEXT = "[!] Error 5: Issue requesting from the website"
ERROR_6_TEXT = "[!] Error 6: Some parameters might be missing."
ERROR_7_TEXT = "[!] Error 7: Form is empty, not submitting it and continuing to next website."
TRYING_TO_POST = "[*] Trying to post: "
ERROR_4_TEXT = "[!] Error 4: Issue Posting Request to server"
SUCCESS_200_TEXT = "[V] Form filled successfully! Website: "
ERROR_2_TEXT = "[!] Error 2: Form posting failed, Web Error: "
ERROR_1_TEXT = "[!] Error 1: Browser Blocked you from entering more requests,consider sending requests from a different IP (proxy for an example)."