from selenium import webdriver


### this software is only for learning proposes, so the method used maybe is not the batter for scrap.
# website used to scrap: https://www.scrapethissite.com/pages/
def PrototipeOne():
    op = webdriver.ChromeOptions()
    op.add_argument("--no-sandbox")


    browser_engine = webdriver.Edge()
    cobaia_url = "https://www.scrapethissite.com/pages/simple/"
    browser_engine.get(cobaia_url)
    input()




if __name__ == "__main__":
    PrototipeOne()