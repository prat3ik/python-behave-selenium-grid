import sys
import os

args = sys.argv
if args.__len__() !=  0:
    if args[1] == '--single':
        for browser in args[3:]:
            f = open("context/testsettings.json", "w")
            f.write(
                '{"url": "https://www.google.com","browser": "' + browser + '","driver_timeout": "5"}')
            f.close()
            os.system('behave -n ' + args[2])

    else:
        for browser in args[1:]:
            f = open("context/testsettings.json", "w")
            f.write(
                '{"url": "https://www.google.com","browser": "' + browser + '","driver_timeout": "5"}')
            f.close()
            os.system('behave')

os.system('allure serve reports/')
