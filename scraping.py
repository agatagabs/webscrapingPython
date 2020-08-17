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

def BuscarWinrate(nomeLane,seletorBotao, seletorLine ):

    button = browser.find_element_by_css_selector(seletorBotao)
    button.click()
    line = browser.find_elements_by_css_selector(seletorLine)
    for boneco in line:
        texto = boneco.text
        valores = texto.split("\n")
        nome = valores[1]
        porcentagens = valores[3].split(" ")
        winRate = porcentagens[0]
        Lane[nomeLane].append(nome + ": " + winRate)


BuscarWinrate("Top", "[data-tab-show-class='champion-trend-winratio-TOP'] > a", ".tabItem.champion-trend-winratio-TOP > tr" )
BuscarWinrate("Jungle", "[data-tab-show-class='champion-trend-winratio-JUNGLE'] > a", ".tabItem.champion-trend-winratio-JUNGLE > tr")
BuscarWinrate("Middle", "[data-tab-show-class='champion-trend-winratio-MID'] > a", ".tabItem.champion-trend-winratio-MID > tr" )
BuscarWinrate("Bottom", "[data-tab-show-class='champion-trend-winratio-ADC'] > a", ".tabItem.champion-trend-winratio-ADC > tr")
BuscarWinrate("Support","[data-tab-show-class='champion-trend-winratio-SUPPORT'] > a", ".tabItem.champion-trend-winratio-SUPPORT > tr")

#Fim :)
browser.close()


lanes = pd.DataFrame(dict([ (k,pd.Series(v)) for k,v in Lane.items() ]))
lanes.to_csv('testebot.csv', index = False)