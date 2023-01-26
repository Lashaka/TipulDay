import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import constants.constants as const
class Submit_forms(object):

    def __init__(
            self:object,
            websites,
            url,
            formname,
            formphone,
            formemail,
            formcomment,
            console

            ) -> None:
        self.console = console
        self.FORM_NAME = formname
        self.FORM_EMAIL = formemail
        self.FORM_COMMENT = formcomment
        self.FORM_PHONE = formphone
        self.SuccessfullForms=0
        self.FailedForms=0  
        self.websites = websites

        self.url = url

    def main(self) -> None:
        if self.console !=None:
            self.console.print(self.FORM_EMAIL,self.FORM_COMMENT,self.FORM_NAME,self.FORM_PHONE)
            self.console.print(const.SUBMIT_FORMS_TEXT)
        else:
            print(self.FORM_EMAIL,self.FORM_COMMENT,self.FORM_NAME,self.FORM_PHONE)
            print(const.SUBMIT_FORMS_TEXT)
        if len(self.websites) > 0:
            for website in self.websites:
                try:
                    response = requests.get(website)
                except:
                    if self.console !=None:
                        self.console.print(const.ERROR_5_TEXT)
                    else:
                        print(const.ERROR_5_TEXT)

                    self.FailedForms += 1
                    continue
                

                soup = BeautifulSoup(response.text, "html.parser")
                Domain = urlparse(website).netloc
                form_action = soup.find_all("form") 
                for data in form_action:
                   action = data.get("action") 
                   if action == f"{Domain}/" or action == f"https://{Domain}/" or action == f"http://{Domain}/":
                       continue
                   else:
                       try:     
                           if Domain in self.websites:
                               for website in self.websites:
                                   if Domain in self.websites:
                                       self.websites.remove(website)

                                       continue
                           break
                       except:
                           continue
                       
                       
                       
                       

                form_elements = soup.find_all("input") + soup.find_all("textarea")

                form_data = {}
    
                for element in form_elements:
                    name = element.get("name")
                    value = element.get("value")  
                    form_data[name] = value

                for data in form_data:
                    try:
                        if "name" in data or "1" in data or "form_field_1" in data or "contact_name" in data: 
                            form_data[data] = self.FORM_NAME
                        if "phone" in data or "num" in data or "tel" in data  or "2" in data or "form_field_2" in data or "contact_phone" in data:
                            form_data[data] = self.FORM_PHONE
                        if "mail" in data or "3" in data or "form_field_3" in data or "contact_email" in data:
                            form_data[data] = self.FORM_EMAIL
                        if "Comment" in data or "message" in data or "details" in data  or "text" in data or "4" in data or "form_field_4" in data:
                            form_data[data] = self.FORM_COMMENT             
                    except:
                        if self.console !=None:
                            self.console.print(const.ERROR_6_TEXT, website)
                        else:
                            print(const.ERROR_6_TEXT, website)

                   
                if len(form_data) is 0:
                    if self.console !=None:
                        self.console.print(const.ERROR_7_TEXT)
                    else:
                        print(const.ERROR_7_TEXT)
                    self.FailedForms += 1
                    continue
                else:
                    try:
                        if self.console !=None:
                            self.console.print(const.TRYING_TO_POST, form_data)
                        else:
                            print(const.TRYING_TO_POST, form_data)
                        response = requests.post(website, data=form_data)
                    except:
                        if self.console !=None:
                            self.console.print(const.ERROR_4_TEXT)
                        else:
                            print(const.ERROR_4_TEXT)
                        self.FailedForms += 1
                        continue

                    if response.status_code == 200:
                        if self.console !=None:
                            self.console.print(const.SUCCESS_200_TEXT + website)
                        else:
                            print(const.SUCCESS_200_TEXT + website)
                        self.SuccessfullForms += 1
                        continue
                    else:
                        if self.console !=None:
                            self.console.print(const.ERROR_2_TEXT,response.status_code)
                        else:
                            print(const.ERROR_2_TEXT,response.status_code)
                        self.FailedForms += 1
                        continue
            if self.console !=None:
                self.console.print("[*] Finished Submitting Forms")
                self.console.print('\n\tSuccessfully Filled Forms:', str(self.SuccessfullForms))
                self.console.print('\n\tFailed Forms:', str(self.FailedForms))
            else:
                print("[*] Finished Submitting Forms")
                print('\n\tSuccessfully Filled Forms:', str(self.SuccessfullForms))
                print('\n\tFailed Forms:', str(self.FailedForms))
        else:
            if self.console !=None:
                self.console.print(const.ERROR_1_TEXT)
            else:
                print(const.ERROR_1_TEXT)

