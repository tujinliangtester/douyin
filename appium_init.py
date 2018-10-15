from appium import webdriver
import xlrd
import time
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.keys import Keys

dyno='1542684036'
wb = xlrd.open_workbook('init.xlsx')
sh = wb.sheet_by_name('appium')
desired_caps = {}
i = 0
flag = 'begin'
while i < 100:
    i += 1
    print(sh.cell_value(i, 0))

    if sh.cell_value(i, 0) == 'begin':
        while sh.cell(rowx=i + 1, colx=0):
            i += 1
            if sh.cell_value(i, 0) == 'end':
                break
            if sh.cell(rowx=i, colx=1):
                print(i)
                key = sh.cell_value(rowx=i, colx=0)
                val = sh.cell_value(rowx=i, colx=1)
                desired_caps[key] = val

        break

desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}
desired_caps['noReset'] = 'true'
desired_caps['unicodeKeyboard'] = 'true'
desired_caps['resetKeyboard'] = 'true'
print(desired_caps)
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(30)

print('手动将抖音切换到搜索页面....')
time.sleep(10)

el = driver.find_element_by_id('com.ss.android.ugc.aweme:id/a5q')
# el.clear()
# 抖音号
el.click()
time.sleep(0.5)
el.send_keys(dyno)

print(el.text)
# el.send_keys(Keys.ENTER)

el = driver.find_element_by_id('com.ss.android.ugc.aweme:id/a5s')
el.click()

time.sleep(5)
el = driver.find_element_by_id('com.ss.android.ugc.aweme:id/bbo')
el.click()

time.sleep(5)
el = driver.find_element_by_id('com.ss.android.ugc.aweme:id/a1e')

assert el.text == '抖音号: ' + dyno

# el=driver.find_element_by_id('com.ss.android.ugc.aweme:id/a6m')
# el.click()

# el = driver.find_element_by_id('com.ss.android.ugc.aweme:id/amq')
els=driver.find_elements_by_id('com.ss.android.ugc.aweme:id/amm')
els[0].click()

#用图片查看工具找到元素的坐标位置
lx=657/720
ly=613/1280

x = driver.get_window_size()['width']
y = driver.get_window_size()['height']
#
# driver.swipe(x, y,x,y,1)
# driver.swipe(x, y,x,y,1)

actions = TouchAction(driver)
actions.tap(x=x*lx, y=y*ly)
actions.perform()


time.sleep(1)
s=time.strftime("%m%d", time.localtime())+'_'
img = s+dyno+'.png'
driver.save_screenshot(img)

if __name__ == '__main__':
    print('ok')
