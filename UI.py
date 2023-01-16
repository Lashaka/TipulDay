# add a button  that adds example data to all fields
import PySimpleGUI as sg

import NewMain as main

import os

# If MoreWebsites is True, add websites to specificwebsites list
MoreWebsites = False

websites = ''

def submit_form():
    # Get values from form
    SearchString = values['searchstring']
    AmountOfWebsitesToSendFormsTo = int(float(values['websiteamount']))
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
            main.StartTipulDay(SearchString,AmountOfWebsitesToSendFormsTo,FormNameValue,FormPhoneNumberValue,FormEmailValue,FormCommentValue,MoreWebsites,SpecificWebsites,form)
            pass
        except:
            pass

    # Submit form using values
    main.StartTipulDay(SearchString,AmountOfWebsitesToSendFormsTo,FormNameValue,FormPhoneNumberValue,FormEmailValue,FormCommentValue,MoreWebsites,'')
    pass



# Create form layout
layout = [[sg.Text('Search String'), sg.Input(key='searchstring')],
          [sg.Text('Website Amount (multiplies by 12)'), sg.Input(key='websiteamount')],
          [sg.Text('Name'), sg.Input(key='name')],
          [sg.Text('Phone Number'), sg.Input(key='phone')],
          [sg.Text('Email'), sg.Input(key='email')],
          [sg.Text('Comment'), sg.Input(key='comment')],
          [sg.Button('Add Sample Info', key='sampleinfo')],
          [sg.Button('Add Specific Websites (Optional)', key='specificwebsites'),
           sg.Multiline(key='specificwebsiteslist', visible=False)],
          [sg.Button('Add Proxies (Optional)', key='proxies'),
           sg.Multiline(key='proxiesinput', visible=False)],   
          [sg.Button('Submit', key='submit', button_color=('white', 'green'), bind_return_key=True),
           sg.Button('Cancel', key='cancel', button_color=('white', 'red'))],
           [sg.Text('Console Output:')],
           [sg.Text()],
           [sg.Multiline(key='console', size=(45,5))]]

# Create form and show it
form = sg.Window('TipulDay', layout)

# Event loop to process form events
while True:
    event, values = form.Read()
    if event in (None, 'cancel'):
        os._exit(0) # stops all code execution and exits the program
        break
    elif event == 'submit':
        try:
            submit_form()
        except Exception as error:
            console = form.find_element('console')
            console.print(str(error))

    elif event == 'sampleinfo':    
        form.find_element('searchstring').Update('Dog Adopting leave your details')   
        form.find_element('websiteamount').Update('10')          
        form.find_element('name').Update('Nice Guy')   
        form.find_element('phone').Update('6666666666')   
        form.find_element('email').Update('Example@gmail.com')   
        form.find_element('comment').Update('I liked trains.')   

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

