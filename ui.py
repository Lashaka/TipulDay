import PySimpleGUI as sg
from threading import Thread
from modules.main import main
class UI:
    def __init__(self):
        self.MoreWebsites = False
        self.websites = []
        self.form = self.create_window()
        self.get_UI_events()


    def submit_form(self):
        SearchString = self.values["searchstring"]
        AmountOfWebsitesToSendFormsTo = int(float(self.values["websiteamount"]))
        FormNameValue = self.values["name"]
        FormPhoneNumberValue = self.values["phone"]
        FormEmailValue = self.values["email"]
        FormCommentValue = self.values["comment"]
        if self.MoreWebsites:
            self.SpecificWebsites = self.values["specificwebsiteslist"].split(",")
            for Website in self.SpecificWebsites:
                self.websites.append(Website)

        try:
            print(self.websites)
            Thread(target=main(
            SearchString,
            AmountOfWebsitesToSendFormsTo,
            FormNameValue,
            FormPhoneNumberValue,
            FormEmailValue,
            FormCommentValue,
            self.websites,
            self.form.find_element('console')
            ).main(), daemon=True).start()
        except Exception as e:
            print(e)
            pass

    def create_window(self):
        layout = [[sg.Text('Search String'), 
        sg.Input(key='searchstring')],
        [sg.Text('Website Amount (multiplies by 12)'), 
        sg.Input(key='websiteamount')],
        [sg.Text('Name'), 
        sg.Input(key='name')],
        [sg.Text('Phone Number'), 
        sg.Input(key='phone')],
        [sg.Text('Email'), 
        sg.Input(key='email')],
        [sg.Text('Comment'), 
        sg.Input(key='comment')],
        [sg.Button(
        'Add Sample Info', 
        key='sampleinfo')],
        [sg.Button(
        'Add Specific Websites (Optional)', 
        key='specificwebsites'),
         sg.Multiline(
        key='specificwebsiteslist', 
        visible=False)], 
        [sg.Button(
        'Submit', 
        key='submit', 
        button_color=('white', 'green'), 
        bind_return_key=True),
        sg.Button(
        'Cancel', 
        key='cancel', 
        button_color=('white', 'red'))],
        [sg.Text('Console Output:')],
        [sg.Text()],
        [sg.Multiline(
        key='console', 
        size=(45,5))]]
        form = sg.Window(
        'TipulDay', 
        layout
            )
        return form
    
    def get_UI_events(self):
        while True:
            event, self.values = self.form.Read(timeout=10)
            if event in (sg.WIN_CLOSED, '-CLOSE-'):
                break
            match event:

                case (None, 'cancel'):
                    exit()

                case 'submit':
                    try:
                        Thread(target=self.submit_form(),daemon=True).start()
                    except Exception as error:
                        self.console = self.form.find_element('console')
                        self.console.print(str(error))

                case 'sampleinfo':    
                    self.form.find_element('searchstring').Update('Dog Adopting leave your details')   
                    self.form.find_element('websiteamount').Update('10')          
                    self.form.find_element('name').Update('Nice Guy')   
                    self.form.find_element('phone').Update('6666666666')   
                    self.form.find_element('email').Update('Example@gmail.com')   
                    self.form.find_element('comment').Update('I liked trains.')   

                case 'specificwebsites':
                    if self.form.find_element('specificwebsiteslist').visible:
                        self.form.find_element('specificwebsiteslist').Update(visible=False)     
                        self.form.find_element('specificwebsites').Update('Add Specific Websites (Optional)')   
                        MoreWebsites= True
                            
                    elif(self.form.find_element('specificwebsiteslist').visible==False):
                        self.form.find_element('specificwebsiteslist').Update(visible=True)
                        self.form.find_element('specificwebsites').Update('Remove Specific Websites')   

                        MoreWebsites=False        

ui = Thread(target=UI()).start()