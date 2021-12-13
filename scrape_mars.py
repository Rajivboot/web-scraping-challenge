from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# making scrapping function and copying all codes from panda
def scrape():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    browser.visit("https://redplanetscience.com/")

    news_title=browser.find_by_css("div.content_title")[0].text

    news_p=browser.find_by_css("div.article_teaser_body")[0].text

    browser.visit("https://spaceimages-mars.com/")

    browser.find_by_css("button.btn.btn-outline-light").click()

    featured_image_url=browser.find_by_css("img.fancybox-image")["src"]

    df=pd.read_html("https://galaxyfacts-mars.com/")[0]

    df.columns=["Desc","Mars","Earth"]
    df.drop(0,axis=0, inplace=True)

    mars=df.to_html()

    browser.visit("https://marshemispheres.com/")

    hemisphere_image_urls = []

    for i in range(len(browser.find_by_css("a.product-item img"))):
        browser.find_by_css("a.product-item img")[i].click()
        hemi_url = browser.find_by_text("Sample")["href"]
        hemi_title = browser.find_by_css("h2.title").text
        # print(hemi_url, hemi_title)
        hemisphere_image_urls.append({"title":hemi_title, "img_url": hemi_url})
        # browser.visit("https://marshemispheres.com/")
        browser.back()
    browser.quit()   


    return {'newstitle':news_title, 'newp' : news_p, 'featured_url':featured_image_url, 'mars':mars, 'hemisphere_image_urls': hemisphere_image_urls }     

if __name__=="__main__": 
    print (scrape())
