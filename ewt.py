from selenium import webdriver
from time import sleep
web = webdriver.Chrome()
web.get("https://www.ewt360.com/")
web.implicitly_wait(10)
print(web.window_handles)
web.find_element_by_css_selector("#username").send_keys("sdqljzx1100316\tl29012578\n")
web.find_element_by_css_selector("#myClassEntrance").click()
print(web.window_handles)
sleep(5)
web.switch_to.window(web.window_handles[-1])
web.find_element_by_css_selector(" .ewt-tab-filter:nth-child(2) li:nth-last-child(1) button").click()
ele = web.find_elements_by_css_selector('#app div  li div  button')
for i in ele:
    if str(i.text) == '做作业':
        i.click()
        break
print(web.window_handles)
sleep(5)
web.switch_to_window(web.window_handles[-1])
web.find_element_by_css_selector('div .resource-info-YpSfa').click()
input