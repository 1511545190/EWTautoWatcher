#-i https://pypi.tuna.tsinghua.edu.cn/simple
from selenium import webdriver
web = webdriver.Chrome()
web.get("https://www.baidu.com/")
web.implicitly_wait(5)
print(web.window_handles)
web.find_element_by_css_selector('#kw').send_keys("Hello\n")
web.find_element_by_css_selector("#content_left a:nth-child(1)").click()
print(web.window_handles)
web.switch_to.window(web.window_handles[-1])
web.find_element_by_css_selector(".desktop-guide-close").click()
web.find_element_by_css_selector(".manual-trans-btn").click()
print(web.window_handles)
web.switch_to.window(web.window_handles[-1])
web.find_element_by_css_selector(".text-mark").click()




input(" ")















web.quit()