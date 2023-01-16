# add a button  that adds example data to all fields
import PySimpleGUI as sg

import NewMain as main

# If MoreWebsites is True, add websites to specificwebsites list
MoreWebsites = False

websites = ''

def submit_form():
    # Get values from form
    SearchString = values['searchstring']
    AmountOfWebsitesToSendFormsTo = int(values['websiteamount'])
    FormNameValue = values['name']
    FormPhoneNumberValue = values['phone']
    FormEmailValue = values['email']
    FormCommentValue = values['comment']

    # If MoreWebsites is True, add websites to specificwebsites list
    if MoreWebsites is True:
        SpecificWebsites = values['specificwebsiteslist'].split(',')
        for Website in SpecificWebsites:
            websites.append(Website)

        # Submit form using values
        try:
            main.StartTipulDay(SearchString,AmountOfWebsitesToSendFormsTo,FormNameValue,FormPhoneNumberValue,FormEmailValue,FormCommentValue,MoreWebsites,SpecificWebsites)
            pass
        except:
            pass

    # Submit form using values
    try:
        main.StartTipulDay(SearchString,AmountOfWebsitesToSendFormsTo,FormNameValue,FormPhoneNumberValue,FormEmailValue,FormCommentValue,MoreWebsites,'')
        pass
    except:
        pass


# Create form layout
layout = [[sg.Text('Search String'), sg.Input(key='searchstring')],
          [sg.Text('Website Amount'), sg.Input(key='websiteamount')],
          [sg.Text('Name'), sg.Input(key='name')],
          [sg.Text('Phone Number'), sg.Input(key='phone')],
          [sg.Text('Email'), sg.Input(key='email')],
          [sg.Text('Comment'), sg.Input(key='comment')],
          [sg.Button('Add Specific Websites (Optional)', key='specificwebsites'),
           sg.Multiline(key='specificwebsiteslist', visible=False)],
          [sg.Button('Add Proxies (Optional)', key='proxies'),
           sg.Multiline(key='proxiesinput', visible=False)],   
          [sg.Button('Submit', key='submit', button_color=('white', 'green'), bind_return_key=True),
           sg.Button('Cancel', key='cancel', button_color=('white', 'red'))]]

# Create form and show it
form = sg.Window('TipulDay', layout)

# Event loop to process form events
while True:
    event, values = form.Read()
    if event in (None, 'cancel'):
        break
    elif event == 'submit':
        submit_form()
    elif event == 'specificwebsites': 
        if(form.find_element('specificwebsiteslist').visible==True):
            form.find_element('specificwebsiteslist').Update(visible=False)     
            form.find_element('specificwebsites').Update('Add Specific Websites (Optional)')   
            MoreWebsites= True      
        elif(form.find_element('specificwebsiteslist').visible==False):
            form.find_element('specificwebsiteslist').Update(visible=True)
            form.find_element('specificwebsites').Update('Remove Specific Websites')    
            MoreWebsites=False        
    elif event == 'proxies': 
        if(form.find_element('proxiesinput').visible==True):
            form.find_element('proxiesinput').Update(visible=False)     
            form.find_element('proxies').Update('Add Proxies (Optional)')   
            MoreWebsites= True      
        elif(form.find_element('proxiesinput').visible==False):
            form.find_element('proxiesinput').Update(visible=True)
            form.find_element('proxies').Update('Remove Proxies')    
            MoreWebsites=False      
form.Close()
