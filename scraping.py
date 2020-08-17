import pandas as pd 
from selenium import webdriver
from time import sleep
import csv

browser = webdriver.Chrome(executable_path="./chromedriver/chromedriver.exe")

Lane = {"Top": [] , "Jungle": [], "Middle": [], "Bottom": [], "Support": []}

#Entrando na seção WinRate
browser.get("https://br.op.gg/champion/statistics")
buttonWinRate = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[6]/div/div[1]/ul/li[2]/a")
browser.execute_script("return arguments[0].scrollIntoView(true);", buttonWinRate)
buttonWinRate.click()
sleep(2)

#Top
buttonTop = browser.find_element_by_css_selector("[data-tab-show-class='champion-trend-winratio-TOP'] > a")
buttonTop.click()
top = browser.find_elements_by_css_selector(".tabItem.champion-trend-winratio-TOP > tr")
for boneco in top:
    texto = boneco.text
    valores = texto.split("\n")
    nome = valores[1]
    porcentagens = valores[3].split(" ")
    winRate = porcentagens[0]
    Lane["Top"].append(nome + ": " + winRate)

#Jungle
buttonJungle = browser.find_element_by_css_selector("[data-tab-show-class='champion-trend-winratio-JUNGLE'] > a")
buttonJungle.click()
jungle = browser.find_elements_by_css_selector(".tabItem.champion-trend-winratio-JUNGLE > tr")
for boneco in jungle:
    texto = boneco.text
    valores = texto.split("\n")
    nome = valores[1]
    porcentagens = valores[3].split(" ")
    winRate = porcentagens[0]
    Lane["Jungle"].append(nome + ": " + winRate)

#Middle
buttonMiddle = browser.find_element_by_css_selector("[data-tab-show-class='champion-trend-winratio-MID'] > a")
buttonMiddle.click()
middle = browser.find_elements_by_css_selector(".tabItem.champion-trend-winratio-MID > tr")
for boneco in middle:
    texto = boneco.text
    valores = texto.split("\n")
    nome = valores[1]
    porcentagens = valores[3].split(" ")
    winRate = porcentagens[0]
    Lane["Middle"].append(nome + ": " + winRate)

#Bottom
buttonBottom = browser.find_element_by_css_selector("[data-tab-show-class='champion-trend-winratio-ADC'] > a")
buttonBottom.click()
bottom = browser.find_elements_by_css_selector(".tabItem.champion-trend-winratio-ADC > tr")
for boneco in bottom:
    texto = boneco.text
    valores = texto.split("\n")
    nome = valores[1]
    porcentagens = valores[3].split(" ")
    winRate = porcentagens[0]
    Lane["Bottom"].append(nome + ": " + winRate)

#Support
buttonSupport = browser.find_element_by_css_selector("[data-tab-show-class='champion-trend-winratio-SUPPORT'] > a")
buttonSupport.click()
support = browser.find_elements_by_css_selector(".tabItem.champion-trend-winratio-SUPPORT > tr")
for boneco in support:
    texto = boneco.text
    valores = texto.split("\n")
    nome = valores[1]
    porcentagens = valores[3].split(" ")
    winRate = porcentagens[0]
    Lane["Support"].append(nome + ": " + winRate)

#Fim :)
browser.close()


lanes = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in Lane.items() ]))
lanes.to_csv('testebot.csv', index = False)