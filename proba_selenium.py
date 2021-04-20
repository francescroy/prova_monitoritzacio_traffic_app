

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

opt = Options()

opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2,
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2,
    "profile.default_content_setting_values.notifications": 2
  })


opt.add_argument('headless')

driver = webdriver.Chrome(options=opt,executable_path="./chromedriver")
driver.get("https://meet.guifi.net/prova_selenium")
#print(driver.title)


driver.implicitly_wait(10)

driver.get_screenshot_as_file('main-page.png')

#for i in range(5):

#    driver.execute_script("window.open('');")
    # Switch to the new window and open new URL
#    driver.switch_to.window(driver.window_handles[i+1])
#    driver.get("https://meet.guifi.net/dsg-upc")




#driver.find_element(By.ID, "search_form_input_homepage").send_keys("Youtube")

#driver.find_element(By.ID, "search_button_homepage").click()

#driver.quit()



