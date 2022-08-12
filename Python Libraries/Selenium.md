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

## Waits: The page doesn't load all at once.
By default, Selenium waits until the page is loaded. But, if you try and find an element as soon as the page is loaded, the element might not be there. Use `WebDriverWait()` to wait for a given time until the element is present.
```Python
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

element = WebDriverWait(driver, 10).until(
	EC.presence_of_element_located((By.CSS_SELECTOR, "#main"))
)
```

Explanation:
- `WebDriverWait()` will wait for 10 seconds
	- if found, it will assign the `Element` to the variable `element`
	- if not found, it will raise a `TimeoutExceptionError` (*i.e., waited too long*)
- the above code attempts to find an element with the matching **CSS selector** (*an element with ID equal to `main`*)
