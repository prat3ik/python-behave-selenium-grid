# Python-Behave-Selenium(GRID)

## Selenium

Is a framework for automating browser interactions. More information can be found [here](https://www.seleniumhq.org/)

## Behave

Is a framework for BDD (Behaviour-Driven Development). It is a common language syntax which can be used to define steps for end to end tests. It's documentation can be found [here](https://behave.readthedocs.io/en/latest/)


## SELENIUM GRID

 **Download the Selenium standalone jar file: [https://bit.ly/2TlkRyu](https://bit.ly/2TlkRyu)**

1) Open terminal-1 and enter: `java -jar /Users/pratik/Downloads/selenium-server-standalone-3.141.59.jar -role hub`

It gives o/p saying: `Nodes should register to [http://192.168.29.218:4444/grid/register/](http://192.168.29.218:4444/grid/register/)` so you need to start the node(step-2)

2) Open terminal-2 and enter: `java -jar selenium-server-standalone-3.141.59.jar -role node -hub [http://192.168.29.218:4444/wd/hub](http://192.168.29.218:4444/wd/hub)`

Once you execute this command it will register the node to above hub and now hub will say: `Clients should connect to [http://192.168.29.218:4444/wd/hub](http://192.168.29.218:4444/wd/hub)`

So you have to use this URL([`http://192.168.29.218:4444/wd/hub`](http://192.168.29.218:4444/wd/hub)) for RemoteWebDriver 

example: `self.driver = webdriver.Remote(command_executor='[http://192.168.29.218:4444/wd/hub](http://192.168.29.218:4444/wd/hub)', desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True})`

## EXECUTE TEST

1) First of move root project directory execute `pip3 install -r requirements.txt`which will install the all needed python dependencies to your computer

2) Install the chromedriver using: `brew cask install chromedriver`
 
3) Install the geckodriver(firefox) using: `brew install geckodriver`
 
4) Install allure using `brew install allure` & `pip install allure_behave`(OR `npm install -g allure-commandline --save-dev`)

5) In the root project directory execute: `behave`and it will start executing tests

6) To execute tests with multiple browsers, do execute: `python3 exec.py chrome firefox` 

#### features
Contains `.feature` files. These are text files conforming to [gherkin syntax](https://behave.readthedocs.io/en/latest/philosophy.html#the-gherkin-language).

#### steps
Contains files with test methods which are bound to steps in the `.feature` files.

#### pages
Contains all page objects, as well as locators for finding elements on the webpages.
