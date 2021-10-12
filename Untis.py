from time import sleep
from selenium import webdriver
import typer

from secrets import username, password

app = typer.Typer()
url = 'https://thalia.webuntis.com/WebUntis/?school=les#/basic/login'

#Chrome wird nicht mit einer automatisierten Software kontrolliert
options = webdriver.ChromeOptions()
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
browser = webdriver.Chrome(chrome_options=options)

#Browser öffnen
browser.get(url)
browser.set_window_size(1920, 1080)
browser.maximize_window()

#Anmelden bei WebUntis
sleep(2)
Benutzer_input = browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/form/div[1]/div/input')
Benutzer_input.send_keys(username)

Passwort_input = browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/form/div[2]/div/input')
Passwort_input.send_keys(password)

Login_btn = browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div/form/button')
Login_btn.click()
sleep(3)


@app.command()
def stundenplan():
    Stundenplan_btn = browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div/a[4]/div/div')
    Stundenplan_btn.click()

@app.command()
def abwesenheit():
    Abwesenheit_btn = browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div/a[5]/div/div')
    Abwesenheit_btn.click()

@app.command()
def noten():
    Noten_btn = browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div/a[10]/div/div')
    Noten_btn.click()

@app.command()
def prüfungen():
    Prüfung_btn = browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div[1]/div/a[9]/div/div')
    Prüfung_btn.click()

if __name__ == '__main__':
    app()