import sys
import os
browsers = sys.argv
if browsers.__len__() !=  0:
    for browser in browsers[1:]:
        f = open("context/testsettings.json", "w")
        f.write(
            '{"url": "https://www.google.com","browser": "'+browser+'","driver_timeout": "5"}')
        f.close()
        os.system('behave')

os.system('allure serve reports/')

