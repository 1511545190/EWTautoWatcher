from selenium import webdriver
from time import sleep
wd = webdriver.Chrome()
wd.implicitly_wait(10)
wd.get("http://www.ewt360.com")
ele = wd.find_element_by_id("username")
ele.send_keys('sdqljzx1100316\tl29012578\n')
wd.find_element_by_id("myClassEntrance").click()

#切换窗口
'''
for handle in wd.window_handles:
    wd.switch_to.window(handle
    )
    if handle != windows:
        break
  '''
print("1:")
print(wd.current_window_handle)
print(wd.window_handles)
#wd.close()
''''''
wd.switch_to.window(wd.window_handles[-1]) 

#切换视频
wd.find_element_by_css_selector('main div .ewt-tab-filter:nth-child(2) li:nth-last-child(1)').click()
ele = wd.find_elements_by_css_selector('#app div  li div  button')
for i in ele:
    if str(i.text) == '做作业':
        i.click()
        #wd.refresh()
        break



wd.switch_to.window(wd.window_handles[-1]) 
print("2:")
print(wd.window_handles)
print(wd.current_window_handle)
''''''
wd.find_element_by_css_selector('main div span p').click()

print(wd.window_handles)

        







input(' ')
wd.quit()

