## Project: 0x11. Python - Network #1

This project focuses on using Python for network-related tasks, including fetching internet resources, making HTTP requests, and manipulating data from external services. The project aims to improve your understanding of how to use the urllib and requests packages for sending HTTP requests, handling responses, and working with JSON data.

### Resources
- [HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html)
- [Quickstart with Requests package](https://docs.python-requests.org/en/latest/user/quickstart/)
- [Requests package](https://docs.python-requests.org/en/latest/)

### Learning Objectives
Upon completion of this project, you should be able to explain the following concepts without needing external references:
- Fetching internet resources with the urllib package
- Decoding urllib response bodies
- Using the requests package for HTTP requests
- Making HTTP GET, POST, PUT, etc., requests
- Fetching JSON resources
- Manipulating data from external services

### Requirements
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- All files must be executable
- The length of your files will be tested using `wc`
- All modules should have documentation
- Your code should not be executed when imported (use `if __name__ == "__main__":`)

### Tasks
## Task 1. What's my status? #0
   - Write a Python script that fetches https://alx-intranet.hbtn.io/status
   - Use the package urllib
   - Display the body of the response
   - Use a with statement
   - Example output:
     ```
     Body response:
         - type: <class 'bytes'>
         - content: b'OK'
         - utf8 content: OK
     ```

## Task 2. Response header value #0
   - Write a Python script that takes in a URL, sends a request to the URL, and displays the value of the X-Request-Id variable found in the header of the response.
   - Use the packages urllib and sys
   - Example output:
     ```
     ade2627e-41dd-4c34-b9d9-a0fa0f47b237
     ```

## Task 3. POST an email #0
   - Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
   - The email must be sent in the email variable
   - Use the packages urllib and sys
   - Example output:
     ```
     Your email is: hr@holbertonschool.com
     ```

## Task 9. My GitHub!
   - Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
   - Use Basic Authentication with a personal access token as password to access your information
   - Use the packages requests and sys
   - Example output:
     ```
     2531536
     ```

