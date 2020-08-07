from selenium import webdriver

browser = webdriver.Firefox(executable_path="/home/avatar/Projects/webscrapingPython/geckodriver")

Lane = {"Top": [], "Jungle": [], "Middle": [], "Bottom": [], "Support": []}

browser.get("https://br.op.gg/champion/statistics")
element = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[6]/div/div[1]/ul/li[2]/a")
element.click()
name = browser.find_elements_by_css_selector("td:nth-child(3)")
winRate = browser.find_elements_by_css_selector("td:nth-child(4)")

print(len(name))

print(name[0].text)
print(winRate[0].text)


while len(name) != 149:
    name.pop()

while len(winRate) != 149:
    winRate.pop()

print(name[0].text)
print(winRate[0].text)

for x, y in zip(name, winRate):
    for z in x.text.split("\n", 1)[1].split(", "):
        Lane[z].append([x.text.split("\n")[0], y.text])

for x in Lane:
    print(x)
    print(Lane[x])

browser.close()