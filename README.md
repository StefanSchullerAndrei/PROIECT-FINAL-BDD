# PROIECT-FINAL-BDD


### TESTED PARABANK WEBSITE FUNCTIONS

https://parabank.parasoft.com/parabank/register.htm;jsessionid=5A22F77B4926BC6E9A20EF6B90872650

I chose to check the functionality of the Parabank site using automation testing. In this testing module I used different Scenarios, such as: Register, forgot login info, bill pay, create new account and etc

### LANGUAGE, IDE, BOOKSTORES
I chose to perform the testing using the Python programming language and the PyCharm IDE. After installing Cucumber, Gherking & Ini plugins, I used the Selenium, webdriver-manager, behave and behave-html-formatter libraries to automate the interaction with the Parabank website. The "Python Packages" section of PyCharm can be accessed to install these libraries. After adding the name of the desired library in the field, I pressed the "Install" button.

### THE IMPORTANCE OF AUTOMATED TESTING
Efficiency in software development depends on automated testing. Speed, reproducibility, extended coverage, reusability, ease of integration with agile development practices and early detection of errors are the main benefits. This constantly helps to ensure the quality of the software.

### THE CHOSEN METHODOLOGY
The software development methodology called BDD (Behavior-Driven Development) focuses on the collaboration of team members and on describing the behavior of the application in a simple language, such as Gherkin.

### DESIGN PATTERN 
I chose to organize the code of the automated tests using the "Page Object Model" (POM). Reusability, encapsulation, ease of maintenance, readability and resistance to change are some of its benefits. POM improves the development and maintenance of automated tests and code structure.

### STRUCTURE OF THE PROJECT
The project has a structure consisting of a series of files and directories. We find settings for opening Chrome, maximizing the window and a default wait of three seconds in the "browser" file. We have the structure of the pages tested in the "environment". "features", "pages" and "steps" are the three directories that make up the general structure. The test scenarios are written in Gherkin syntax and can be found in the "features" category. We have general methods for actions such as clicking, finding the element, typing, etc. defined in "pages". The other files contain locators and specific methods for the suggested scenarios. The Gherkin syntax defines the functions of the "steps" directory. This structure organizes the code for automated tests.

### SCREENSHOTS WITH THE CODE

![image](https://github.com/StefanSchullerAndrei/PROIECT-FINAL-BDD/assets/170446681/f36013df-146b-4497-8b5a-966896e027e3)
![image](https://github.com/StefanSchullerAndrei/PROIECT-FINAL-BDD/assets/170446681/f50bb3b4-2a43-4eac-ad02-160edb92f05d)
![image](https://github.com/StefanSchullerAndrei/PROIECT-FINAL-BDD/assets/170446681/f9a72ce6-0028-4fd0-b67f-30472fcf3bc8)
![image](https://github.com/StefanSchullerAndrei/PROIECT-FINAL-BDD/assets/170446681/895b4b26-af41-4ac3-8205-02b3f7d89359)
![image](https://github.com/StefanSchullerAndrei/PROIECT-FINAL-BDD/assets/170446681/ded66c62-bbca-494a-b45f-1d9ab614c3db)
![image](https://github.com/StefanSchullerAndrei/PROIECT-FINAL-BDD/assets/170446681/94971ec4-af8d-4dc4-9959-16bd405e92ce)



### SCENARIOS

Test scenarios chosen for evaluation include:

* Register a new account
* Verify that username exists
* Verify login function
* Open new bank account
* Verify new account is indeed created on account overview tab
* Verify Bill Pay function is working
* Verify the new balance after the bill was paid
* Forgot login info function
* Update contact info
* Clear database to ensure that the account registered is indeed deleted
