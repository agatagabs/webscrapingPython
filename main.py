from selenium import webdriver
from time import sleep

browser = webdriver.Firefox(executable_path="/home/avatar/Projects/webscrapingPython/geckodriver")

Lane = {"Top": [], "Jungle": [], "Middle": [], "Bottom": [], "Support": []}

browser.get("https://br.op.gg/champion/statistics")
elementWinRate = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[6]/div/div[1]/ul/li[2]/a")
browser.execute_script("return arguments[0].scrollIntoView(true);", elementWinRate)
elementWinRate.click()
sleep(2)

#Top
elementTop = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[6]/div/div[2]/div/div[2]/div/ul/li[2]/a")
elementTop.click()
all = browser.find_elements_by_css_selector(".tabItem.champion-trend-winratio-TOP > tr")
for boneco in all:
    texto = boneco.text
    valores = texto.split("\n")
    nome = valores[1]
    porcentagens = valores[3].split(" ")
    winRate = porcentagens[0]
    Lane["Top"].append([nome, winRate])

#Jungle
elementJungle = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[6]/div/div[2]/div/div[1]/div/ul/li[2]/a")
elementJungle.click()
all = browser.find_elements_by_css_selector(".tabItem.champion-trend-winratio-JUNGLE > tr")
for boneco in all:
    texto = boneco.text
    valores = texto.split("\n")
    nome = valores[1]
    porcentagens = valores[3].split(" ")
    winRate = porcentagens[0]
    Lane["Jungle"].append([nome, winRate])

#Middle
elementMiddle = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[6]/div/div[2]/div/div[1]/div/ul/li[3]/a")
elementMiddle.click()
all = browser.find_elements_by_css_selector(".tabItem.champion-trend-winratio-MIDDLE > tr")
for boneco in all:
    texto = boneco.text
    valores = texto.split("\n")
    nome = valores[1]
    porcentagens = valores[3].split(" ")
    winRate = porcentagens[0]
    Lane["Middle"].append([nome, winRate])

#Bottom
elementBottom = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[6]/div/div[2]/div/div[1]/div/ul/li[4]/a")
elementBottom.click()
all = browser.find_elements_by_css_selector(".tabItem.champion-trend-winratio-BOTTOM > tr")
for boneco in all:
    texto = boneco.text
    valores = texto.split("\n")
    nome = valores[1]
    porcentagens = valores[3].split(" ")
    winRate = porcentagens[0]
    Lane["Bottom"].append([nome, winRate])

#Support
elementSupport = browser.find_element_by_xpath("//html/body/div[2]/div[2]/div[2]/div[1]/div[6]/div/div[2]/div/div[1]/div/ul/li[5]/a")
elementSupport.click()
all = browser.find_elements_by_css_selector(".tabItem.champion-trend-winratio-SUPPORT > tr")
for boneco in all:
    texto = boneco.text
    valores = texto.split("\n")
    nome = valores[1]
    porcentagens = valores[3].split(" ")
    winRate = porcentagens[0]
    Lane["Support"].append([nome, winRate])


for key in Lane:
    print(key)
    for item in Lane[key]:
        print(item)
    

browser.close()