from selenium import webdriver

browser = webdriver.Firefox(executable_path="/home/avatar/Projects/webscrapingPython/geckodriver")

Lane = {}
browser.get("https://br.op.gg/champion/statistics")
content = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[6]/div/div[2]/div/div[1]/div/table/tbody[1]/tr[1]/td[5]")
print(content.text)