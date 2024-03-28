# 0x10. Python - Network #0

This project aims to introduce the basics of networking with Python, focusing on HTTP requests and how to handle them. Through a series of tasks, learners will gain practical knowledge on working with HTTP protocols, URLs, and HTTP headers using Python scripts and bash commands.

## Learning Objectives

By the end of this project, learners should be able to:

- Understand what a URL is and how to read it.
- Explain the components of an HTTP URL, including the scheme, domain name, sub-domain, port number, and query string.
- Define what HTTP is and describe the structure of HTTP requests and responses, including methods, status codes, headers, and message bodies.
- Recognize what an HTTP Cookie is and how to make requests using cURL.
- Describe the process that occurs when a URL is entered in the browser at the application level.

## Resources

- [HTTP (HyperText Transfer Protocol)](https://developer.mozilla.org/en-US/docs/Web/HTTP) - except: “TRACE” Request Method, “CONNECT” Request Method, Language Negotiation and “Options MultiView” and Character Set Negotiation.
- [HTTP Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)

## Requirements

- Scripts will be tested on Ubuntu 20.04 LTS using `python3` (version 3.8.5).
- All bash scripts should be 3 lines long (`wc -l file` should print 3) and must include the shebang `#!/bin/bash`.
- The second line of all Bash scripts should be a comment explaining the script's purpose.
- All curl commands must use the `-s` (silent mode) option.
- Python code should follow the `pycodestyle` (version 2.8.*) guidelines.
- Documentation for modules, classes, and functions is mandatory.

## Tasks

### 0. cURL body size
Write a Bash script that sends a request to a URL and displays the size of the body of the response in bytes using `curl`.

### 1. cURL to the end
Script that sends a GET request to a URL and displays the body of a 200 status code response.

### 2. cURL Method
A script that sends a DELETE request to a URL and displays the body of the response.

### 3. cURL only methods
Display all HTTP methods the server of a given URL will accept.

### 4. cURL headers
Send a GET request to a URL with a custom header variable and display the body of the response.

### 5. cURL POST parameters
Script that sends a POST request to a given URL with email and subject parameters and displays the response body.

### 6. Find a peak
Implement a function in Python to find a peak in a list of unsorted integers without importing any modules.

## Quiz Questions

Complete the quiz questions to ensure understanding of the project's objectives.


