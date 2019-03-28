# Network Requests Counter [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

This is a utility written in python 3. Here this script can be used to Validate/View/count the  **Desired HTTP Requests and Responses** sent between the Web browser and the Web server. So this can be used to check whether a web-application is firing all the necessary requests or not.

#### Motivation:
Testing is hard, but it pays back if done properly. Selenium gives you many tools to automatically test your web application on real browsers. One thing it doesn’t provide is the access to the browser’s network activity log. That leaves us with the mere ability to look at the HTML elements and trust that the network activity in the background is working as we’d expected. 
Earlier the process of counting the necessary network requests was implemented by using **browsermobproxy** utility. The browsermobproxy provides a HAR file which then has to be converted to JSON format inorder to view the network requests.This is another dependency for the project.

#### Built With:
- [Python 3.x](https://www.python.org/download/releases/3.0/)
- [Javascript-Resource Timing API](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming) - To retrieve and analyze detailed network timing data.
- [Selenium](https://www.seleniumhq.org/) - For automating web applications for testing purposes
- [Email](https://docs.python.org/2/library/email.html#module-email) - Library for sending email messages.

#### Javascript-Resource Timing API
After some research, I found another way to implement this is by using **javascript-Resource Timing API**.So the main reason behind using this API is to eliminate the unnecessary code which was required to obtain a result from the browsermobproxy utility.This API provides a way to retrieve and analyze detailed network timing data regarding the loading of an application's resource(s). An application can use the timing metrics to determine, for example, the length of time it takes to fetch a specific resource such as an XMLHttpRequest, <SVG>, image, script, etc.

#### Usage:
```javascript
var resources = performance.getEntriesByType("resource");
```
```javascript
var resources = window.performance.getEntriesByType("resource");
```
The **resources** is an array of [PerformanceResourceTiming](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming) objects. The PerformanceResourceTiming object contains the URL of the requested resource, timing metrics and resource size data. The browser has a resource timing buffer to hold PerformanceResourceTiming objects. Whenever the browser starts to fetch a resource, it will create a new PerformanceResourceTiming object and store into the buffer until the buffer is full.

#### Steps performed by the script are as follows:
1. Open a web-application /Webpage mentioned in config file
2. Use Selenium to perform operations click on HTML elements, query the DOM structure,modify values,submitting a form,uploading a file etc.
3. Fetch the network requests/url from config file which you want to validate/count. 
3. Execute custom Javascript Resource Timing API using JavascriptExecutor, which will return all the network requests.
4. Compare the network requests from **step4** with the pre-defined network requests from **step3**.
5. Mark the pre-defined request as **PASS** if it matches with any of the actual page requests.
6. Mark the pre-defined Request as **FAIL** if it doesn't match with any of the actual page requests.
7. Send an email report.
      ![Email Report ](/Images/Email.png "Email Report")


## Getting Started:

#### Prerequisites:
1. Python 3
2. This project already has pipfile so go ahead and install all the dependencies from it . Use the below command:Install from Pipfile, if there is one: Please refer to [link](https://pipenv.readthedocs.io/en/latest/basics/#example-pipenv-workflow).

 ```bash
 pipenv install
 ```
#### Customizations:

###### Config File: **_Please  add the below configurations in Config.ini file_**
1. Mention the URL where you want to validate the network requests:

    * Edit: website 
2. Add single or multiple expected network requests in Expected_network_requests section
    * Edit: Expected_network_requests 
3. Add the sender for email:
     
    * Edit: sender 
4. Add single or multiple receivers for email:
     
    * Edit: receiver
5. Add email subject

    * Edit: receiver


##### Note: 
_we have two options for the sending the email_
1. Email module
2. Boto3 

#### How to run the script:
Here we have two options for setup.
1. Set up a _cron job_ daily (**_recommended_**).
2. Run the script manually when it's needed.












 



