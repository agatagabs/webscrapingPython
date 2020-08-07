from selenium import webdriver

browser = webdriver.Firefox(executable_path="/home/avatar/Projects/webscrapingPython/geckodriver")

Lane = {"top": [], "jungle": [], "middle": [], "bottom": [], "support": []}

browser.get("https://br.op.gg/champion/statistics")
name = browser.find_elements_by_css_selector("td:nth-child(4)")
winRate = browser.find_elements_by_css_selector("td:nth-child(5)")

while len(name) != 51:
    name.pop()

while len(winRate) != 51:
    winRate.pop()

for x, y in zip(name, winRate):
    for z in x.text.split("\n", 1)[1].split(", "):
        Lane[z.lower()].append([x.text.split("\n")[0], y.text])

print(Lane)

browser.close()