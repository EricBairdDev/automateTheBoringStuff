from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://inventwithpython.com')
try:
    elem = browser.find_element(By.CLASS_NAME, 'label')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')

# Selenium has a module for keyboard keys that are impossible to type
# into a string value, which function much like escape characters. These
# values are stored in attributes in the selenium.webdriver.common.keys
# module. Since that is such a long module name, it’s much easier to
# run from selenium.webdriver.common.keys import Keys at the top of
# your program; if you do, then you can simply write Keys anywhere
# you’d normally have to write selenium.webdriver.common.keys.
# Table 11-5 lists the commonly used Keys variables.

# browser.back(). Clicks the Back button.
# browser.forward(). Clicks the Forward button.
# browser.refresh(). Clicks the Refresh/Reload button.
# browser.quit(). Clicks the Close Window button.

# The <html> tag is the base tag in HTML files: The full content of the
# HTML file is enclosed within the <html> and </html> tags. Calling
# browser.find_element_by_tag_name('html') is a good place to send
# keys to the general web page. This would be useful if, for example,
# new content is loaded once you’ve scrolled to the bottom of the page