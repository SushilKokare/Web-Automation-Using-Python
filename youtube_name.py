from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Problem occured : after click() function google chrome opens and automatically closes
# for this problem follow link to get solution https://www.reddit.com/r/selenium/comments/g3nhz6/browser_closes_right_after_finishing_test/

class Music():
    # def __init__(self):
    #     self.driver = webdriver.Chrome()
        
    
    def play(self):
        
        name=input("Enter a youtube channel name : ") 
        name="https://www.youtube.com/c/"+name+"/videos"
        #print(name)
        self.driver = webdriver.Chrome()
        
        chrome_options = Options() 
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

        self.driver.get(name)

       # new=self.driver.find_element_by_xpath('//*[@id="thumbnail"]')
        new=self.driver.find_element_by_xpath('//*[@id="items"]/ytd-grid-video-renderer[1]')
        new.click()
       
    
bot = Music()
bot.play()