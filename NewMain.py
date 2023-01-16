# This Code gets phone number, name and mail and prints it as a form in given websites/given google searchx amount of estimated websites.

# Notes:
# be sure to change all the details in the next section to answer your needs
# VERY RECOMMENDED TO USE VPN
# google might block you after some attempts so try to using vpn if you get "Error 1 message" in the console.
# Some websites might block you from entering the info, but its ok to get errors as long as the script runs and gets more websites that succesfully retrieve forms.

###############################################################################################################################################################################

# List Of Potential Errors

# Error 1: Browser Blocked you from entering more requests,consider sending requests from a different IP (vpn for an example).
# Error 2: Error 2: Form posting failed.
# Error 3: Could Not Add the manually entered websites.
# Error 4: Issue Posting Request to server.
# Error 5: Issue requesting from the website.
# Error 6: Some parameters might be missing.
# Error 7: Form is empty, not submitting it and continuing to next website.

###############################################################################################################################################################################

# Libraries that are needed

# importing the necessary libraries
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re

###############################################################################################################################################################################

# Default variables
def StartTipulDay(searchstring,amountofwebsitestosendformsto,formnamevalue,formphonenumbervalue,formemailvalue,formcommentvalue,booladdspecificwebsites,specificwebsites):

    SearchStartNum = 0
    websites = []
    SuccessfullForms=0
    FailedForms=0
###############################################################################################################################################################################
    # Before we start, set the next parameters:

    # the google search value to submit values into
    # recommended 'leave details'/'leave a phone number/Contact restraunts(for restraunt forms submitting)' etc
    SearchString = searchstring  #'Dog Adopting leave your details'

    # Enter amount of websites to try to submit forums to:
    # number of websites is this value x12, note that google has a limit of this search value so from a specific number there will be no change.
    AmountOfWebsitesToSendFormsTo = amountofwebsitestosendformsto

    # enter form name value
    FormNameValue = formnamevalue  # Target first + last name

    # enter form number
    FormPhoneNumberValue = formphonenumbervalue  # Target phone number

    # enter form email # you can use corob21626@gmail.com as a sample
    FormEmailValue = formemailvalue  # Target Email

    # Optional, enter comment. usually not mandatory by most websites, but entering something may increase the submitted forms amount
    FormCommentValue = formcommentvalue  # example : Hello, please call me and send me emails!

    # Optional, change BoolAddSpecificWebsites value to true and add websites if you wish to ass websites manually

    BoolAddSpecificWebsites = booladdspecificwebsites 

    if(BoolAddSpecificWebsites is True):
        try:
            SpecificWebsites = specificwebsites #[f'https://www.example1.com',f'https://www.example2.com/']
            for Website in range(len(SpecificWebsites)):
                websites.append(SpecificWebsites[Website])
        except:
            print('Error 3: Could Not Add the manually entered websites.')


    ###############################################################################################################################################################################

    # This code gets all the websites that will potentially have data submitted into them

    print("[*] Started collecting website data")

    # formatting for the google search
    SearchString = SearchString.replace(" ", "+")


    for lp in range(AmountOfWebsitesToSendFormsTo):
        url = f'https://www.google.com/search?q={SearchString}&start={SearchStartNum}'

        #fake header to get real request
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

        response = requests.get(url,headers = headers)

        # parse the HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # get the top websites from the search results
        for link in soup.find_all('a'):
            if link.get('href'): 
                websites.append(link.get('href'))
                if "http" not in websites[-1]:
                    websites.remove(link.get('href'))
                elif "google" in websites[-1]:
                    websites.remove(link.get('href'))
                    

        # increases after every loop to start in +10 search value
        SearchStartNum = SearchStartNum+10

    print("[*] Websites collected")

    ###############################################################################################################################################################################

    # Code that inputs the form into all the websites

    print("[*] Submitting forms")

    if(len(websites) > 0):
        for website in websites:
            # specifying the website url
            url = website

            # making a request to the website and getting the response
            try:
                response = requests.get(url)
            except:
                print("[!] Error 5: Issue requesting from the website")
                FailedForms += 1
                continue

            # parsing the response using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')


            # Finding if action post link exists in order to add it to the post        
            #gets base domain to add the action post link
            Domain = urlparse(website).netloc
            ActionUrl =''
            form_action = soup.find_all('form') 
            for data in form_action:
                action = data.get('action') 
                if(action == Domain +'/' or action == 'https://'+Domain + '/' or action == 'http://'+Domain + '/'):
                    continue
                else:
                    try:
                        ActionUrl=action
                        BoolUsingMainUrl=False      
                        if Domain in websites:
                            for website in websites:
                                if Domain in websites:
                                    websites.remove(website)

                                    continue
                        break
                    except:
                        continue
                    

        

            # finding the form elements in the page
            form_elements = soup.find_all('input') + soup.find_all('textarea')
            #form_elements.append(soup.find_all('input', {'type': 'tel'}))
            # creating a dictionary to store the form data
            form_data = {}

                # looping through the form elements and getting the data
            for element in form_elements:
                name = element.get('name')
                value = element.get('value')  
                form_data[name] = value

            for data in form_data:
                DataName = data
                try:
                    if "name" in DataName or "1" in DataName or "form_field_1" in DataName or "contact_name" in DataName: 
                        form_data[DataName] = FormNameValue
                    if "phone" in DataName or "num" in DataName or "tel" in DataName  or "2" in DataName or "form_field_2" in DataName or "contact_phone" in DataName:
                        form_data[DataName] = FormPhoneNumberValue
                    if "mail" in DataName or "3" in DataName or "form_field_3" in DataName or "contact_email" in DataName:
                        form_data[DataName] = FormEmailValue
                    if "Comment" in DataName or "message" in DataName or "details" in DataName  or "text" in DataName or "4" in DataName or "form_field_4" in DataName:
                        form_data[DataName] = FormCommentValue             
                except:
                    print('[!] Error 6: Some parameters might be missing.', website)

                # making a post request to the website with the form data
                # Here the issue can be that some sites will use a different location to post the form. Here you should read the 'target' attribute of the post form and append it to the base URL. I think because of this issue many form posts will fail
            if(len(form_data) is 0):
                print('[!] Error 7: Form is empty, not submitting it and continuing to next website.')
                FailedForms += 1
                continue
            else:
                try:
                    print('[*] Trying to post: ', form_data)
                    response = requests.post(url, data=form_data)
                except:
                    print('[!] Error 4: Issue Posting Request to server')
                    FailedForms += 1
                    continue
                        # checking the response status code
                if response.status_code == 200:  # code 200 is success
                    print('[V] Form filled successfully! Website: ' + website)
                    SuccessfullForms += 1
                    continue
                else:
                    print('[!] Error 2: Form posting failed, Web Error: ',response.status_code)
                    FailedForms += 1
                    continue  
    else:
        print('[!] Error 1: Browser Blocked you from entering more requests,consider sending requests from a different IP (vpn for an example).')


    ###############################################################################################################################################################################

    # Final Information Print
    print("[*] Finished Submitting Forms")
    print('\n\tForm Filling Template: \n Name:'+FormNameValue+' \n Phone Number:' + FormPhoneNumberValue+' \n Email:'+FormEmailValue+' \n Meaasge(Optional):'+FormCommentValue)
    print('\n\tSuccessfully Filled Forms:', str(SuccessfullForms))
    print('\n\tFailed Filled Forms:', str(FailedForms))
