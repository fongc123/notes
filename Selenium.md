# Selenium: Browser Automation
*Selenium allows automatic control over your browser.*

## Setup: Start the Selenium driver!
The code block below shows how to start the Selenium Webdriver.
```Python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome(executable_path = "./chromedriver.exe") # for Windows
driver = webdriver.Chrome(executable_path = "./chromedriver")     # for MacOS

# more advanced - use the Remote Webdriver which can be run using Docker
driver = webdriver.Remote(command_executor = "http://localhost:4444/wd/hub")

```