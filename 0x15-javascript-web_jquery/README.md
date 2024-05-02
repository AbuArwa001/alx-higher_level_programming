# 0x15. JavaScript - Web jQuery

## Description
This project is an introduction to the powerful jQuery library, which simplifies front-end web development. Through this project, we'll explore how jQuery makes tasks like DOM manipulation, event handling, and Ajax much simpler with an easy-to-use API that works across a multitude of browsers.

## Resources
- What is JavaScript?
- Selector
- Get and set content
- Manipulate CSS classes
- Manipulate DOM elements
- API Introduction
- GET & POST request
- JQuery Ajax Tutorial #1 - Using AJAX & API’s
- What went wrong? Troubleshooting JavaScript
- JQuery API
- JQuery Ajax

## Learning Objectives
After completing this project, you should be able to explain the following:
- Why jQuery makes front-end programming easier.
- How to select HTML elements in JavaScript and jQuery.
- The differences between ID, class, and tag name selectors.
- How to modify an HTML element's style.
- How to get and update an HTML element's content.
- How to modify the DOM.
- How to make GET and POST requests with jQuery Ajax.
- How to listen/bind to DOM and user events.

## Requirements
- All files must be interpreted on Chrome (version 57.0 or later).
- All files should end with a new line.
- Code should be semistandard compliant with the flag --global $: `semistandard *.js --global $`
- Use jQuery version 3.x.
- Do not use `var`.
- HTML should not reload for each action: DOM manipulation, update values, fetch data, etc.

## More Info
### Import jQuery
Include jQuery in your HTML file's `<head>` section:
```html
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```
## Manual QA Review
It is your responsibility to request a review for this project from a peer before the project’s deadline. If no peers have been reviewed, you should request a review from a TA or staff member.

# Tasks
### 0. No JQuery
Update the text color of the <header> element to red (#FF0000) using document.querySelector.

File: 0-script.js

### 1. With JQuery
Update the text color of the <header> element to red (#FF0000) using the jQuery API.

File: 1-script.js
### 2. Click and turn red
Update the text color of the <header> element to red (#FF0000) when the user clicks on the tag DIV#red_header.