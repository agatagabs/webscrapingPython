from selenium import webdriver

service = webdriver.edge.service.Service("C:\\Users\\tanko\\Downloads\\edgedriver_win64\\msedgedriver")
browser = webdriver.Edge(service=service)

Lane = {}
browser.get("https://br.op.gg/champion/statistics")
content = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[6]/div/div[2]/div/div[1]/div/table/tbody[1]/tr[1]/td[5]")
print(content.text)

