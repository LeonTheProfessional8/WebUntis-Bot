from time import sleep
from selenium import webdriver

class Untis():
    def __init__(self):
        #Chrome wird nicht mit einer automatisierten Software kontrolliert
        options = webdriver.ChromeOptions()
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable-automation"])
        self.browser = webdriver.Chrome(chrome_options=options)

    def Login(self):
        url = 'https://thalia.webuntis.com/WebUntis/?school=les#/basic/login'
        username = "FilajdicLeon20011206"
        password = "les20011206"

        #Browser öffnen
        self.browser.get(url)
        self.browser.set_window_size(1920, 1080)
        self.browser.maximize_window()

        #Anmelden bei WebUntis
        sleep(2)
        Benutzer_input = self.browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/form/div[1]/div/input')
        Benutzer_input.send_keys(username)

        Passwort_input = self.browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/form/div[2]/div/input')
        Passwort_input.send_keys(password)

        Login_btn = self.browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/form/button')
        Login_btn.click()
        sleep(3)

        #Stundenplan öffnen
        Stundenplan_btn = self.browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div/a[4]/div/div')
        Stundenplan_btn.click()
    
bot = Untis()
bot.Login()