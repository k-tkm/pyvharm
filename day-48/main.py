from selenium import webdriver

chrome_driver_path = "/Users/kinjoutakeshiyume/Desktop/development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.amazon.co.jp/%E3%82%B3%E3%82%B9%E3%82%AE%E3%82%BC%E3%83%B3-Kosugizen-%E5%BE%B3%E7%94%A8%E3%82%AB%E3%83%A9%E3%83%BC%E3%82%BF%E3%82%AA%E3%83%AB10%E8%89%B2%E7%B5%84/dp/B01M08KCYI/ref=sr_1_7?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&dchild=1&keywords=%E3%82%BF%E3%82%AA%E3%83%AB&qid=1613723978&sr=8-7")
price = driver.find_element_by_id("priceblock_ourprice")
print(price.text)

# driver.close()
driver.quit()