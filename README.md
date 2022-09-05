# Theo's Kitchen
(Developer: Benjamin Draper)

![Mock-up image](documentation/wireframes/am-i-responsive.jpg)

 [Live webpage]()

## About

Theo's kitchen is a website that inspire's people to create and share their recipes with each other while teaching others. People can learn to cook, start a healthy diet or simply try something new. With the account system you can favorite the recipes you like the most and add your own to share with the community as well.

## Table of Content
1. [Project Goals](#project-goals)
    1. [Website User Goals](#website-user-goals)
    2. [Website Owner Goals](#website-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
3. [User Stories](#user-stories)
4. [Design](#design)
    1. [Design Choices](#design-choices)
    2. [Colour](#colour)
    3. [Fonts](#fonts)
    4. [Structure](#structure)
    5. [Wireframes](#wireframes)
5. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks and Tools](#frameworks-and-tools)
    3. [Libraries](#libraries)
6. [Features](#features)
7. [Validation](#validation)
    1. [HTML Validation](#html-validation)
    2. [CSS Validation](#css-validation)
    3. [JavaScript Validation](#javascript-validation)
    4. [Python Validation](#python-validation)
    5. [Accessibility](#accessibility)
    6. [Performance](#performance)
    6. [Device Testing](#device-testing)
    6. [Browser Compatibility](#browser-compatibility)
8. [Testing user stories](#testing-user-stories)
9. [Bugs](#bugs)
10. [Deployment](#deployment)
11. [Credits](#credits)
12. [Acknowledgements](#acknowledgements)
 
## Project Goals
### Website User Goals
- As a website user, I want to be able to register for an account and log in and out when I wish.
- As a website user, I want to be able to view the recipe's stored on the website.
- As a website user, I want to be able to submit my own recipes to share with others.
- As a website user, I want to have easy options to navigate around the website.

### Website Owner Goals
- As the website owner, I want to promote the website to new and existing users.
- As the website owner, I want the users to be able to create an account and add their own recipes.
- As the website owner, I want users to be able to search for recipes and favorite the ones that they like.
- As the website owner, I want to a user friendly and easily navigable user interface.

[Back to Table Of Content](#table-of-content)

## User Experience
### Target Audience
- This website is targets people who want to learn more about how to cook healthy meals.
- This website targets people looking to loose weight by eating a healthy diet.
- This website targets people who want to learn how to cook simple but tasty meals.

### User Requirements and Expectations
- The user can expect an intuitive and accessible navigation system.
- The user can expect to easily find healthy and easy to cook recipes.
- The user can expect all links work as expected and functions perform their tasks correctly.
- The user can expect presentation is in line with the website guidelines and the website is visually appealing on all screen sizes.
- The user can expect easy to read headings to tell the users at a glance what they are looking at.
- The user can expect accessibility features to be clearly defined.

[Back to Table Of Content](#table-of-content)

## User Stories
1. As a first time user I would like to be able to navigate through the website easily so that it is easy to find the information I am looking for.
2. As a first time user would like to be able to sign up for an account so that I can interact with the community.
3. As a first time user I want to see the available recipes that are on the website so that I can learn eat healthier.
4. As a first time user I want to know about the website and its ethos so that I know I am getting a good service and unbiased opinion.
5. As a first time user I want to know how to find social media links so that I can have in depth conversation with my peers. 
6. As a returning user I would like to be able to favourite the recipes I like the most so that I can easily find them again later.
7. As a returning user I would like to be able to upload my own recipes to share with the community so that I can get their thoughts and feedback on my recipes.
8. As the website owner I there to be a section for featured recipes so that the admin approved 'best' recipes are shown first.
9. As the website owner I want the recipes divided into categories so that users looking for something specific can navigate easier.
10. As the website owner I want the website to act responsively to all device sizes so that the website can be viewed across all devices.
11. As the website owner I want users to get redirected to custom error pages so that they understand when when something has gone wrong and can be redirected back to the main website.
12. As the website owner I want users to create and manage their own accounts so that they can engage in conversation, favourite recipes and add their own.
13. As the website owner I want users to be able to comment on the recipe's on the website and share their opinions so that they can engage with the community more. 
14. As the website owner I want to be able to manually approve comments so that all comments meet the website's ethos.

### Agile Methodology

All functionality and development of this project were managed using GitHub which Projects can be found
[here](https://github.com/users/benjamindraper1996/projects/4)

[Back to Table Of Content](#table-of-content)

## Design
### Design Choices
The website was designed to be responsive and and easy to navigate with a attractive colour pallette that compliments the goals of the website.

### Colour
For the colour scheme I have opted to implement a dark and light theme while using colours that compliment the goals and ambitions of the website. To narrow down the choice of colours I used [coolors](https://coolors.co/) an example of both the dark and light theme are shown below.
<br>

#### Dark Mode
![Dark Mode Theme](documentation/features/colour-palette-dark.png)
<br>

#### Light Mode
![Light Mode Theme](documentation/features/colour-palette-light.png)

### Fonts
 I am using Inter font with a backup of sans-serif across the website for the title and headers. This is used to maintain a Consistent and professional look with an easily readable format. 
<br>
For the Secondary font for the body text the owners decided to use Quicksand with a backup of sans-serif, this will help to maintain the consistent theme across the website.

### Structure
The website has been built using a template engine so that all pages follow the same design to maintain the feel across the website.

The Pages are structured in a Regularly used, user friendly and well-known format. This makes each page easy to navigate, coupled with a responsive navbar and footer this gives the user many options for navigating around the website.

The website consists of 8 main pages, some views spread from these pages and an Error Page.
- Home page
- Login page
- Signup page
- Logout page
- Account page
- Recipes page (with a detailed view for each recipe)
- Catagories page (with a separate list for each category)
- Add/ Edit Recipes page
- Error pages (to guide the user back to the main website)

### Wireframes

<details><summary>Mobile Design</summary>
<img src="documentation/wireframes/mobile.jpg">
</details>
<details><summary>Desktop Design</summary>
<img src="documentation/wireframes/desktop.jpg">
</details>
<br>

[Back to Table Of Content](#table-of-content)

## Technologies Used
### Languages
- [HTML](https://www.w3schools.com/html/default.asp)
- [CSS](https://www.w3schools.com/css/default.asp)
- [JavaScript](https://www.w3schools.com/js/default.asp)
- [Python](https://www.w3schools.com/python/default.asp)

### Frameworks and Tools
- [GitHub](https://github.com/) was used to maintain the version control and store the project remotely
- [Gitpod](https://gitpod.io/) was used to write all the code and to link up with Github to maintain the version control.
- [Balsamiq](https://balsamiq.com/) was use to create the wireframes for the website.
- [Google Fonts](https://fonts.google.com/) was used to pick out the fonts in use across the website.
- [Favicon](https://favicon.io/) was used to create the favicon.
- [coolors](https://coolors.co/) was used to generate a colour pallette.
- [Am I Responsive?](https://ui.dev/amiresponsive) was used to test the responsive nature of the website design.
- [Bootstrap](https://getbootstrap.com/) was used for the pre-defined components and responsive nature of the layout.
- [Heroku](https://dashboard.heroku.com/) was used to host the website for the additional back-end functionality.
- [Cloudinary](https://cloudinary.com/) was used for its free persistent file storage capability over heroku.
- [W3C HTML Validator](https://validator.w3.org/) was used to validate the HTML
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS.
- [WAVE](https://wave.webaim.org/) was used to validate the accessibility of the website.
- [JShint](https://jshint.com/) was used to validate the Javascript.
- [PEP8 Online](http://pep8online.com/) was used to validate the Python.
- [Google Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) was used to validate the website performance, best practice and SEO.

### Libraries
#### Python Libraries


#### Third Party Libraries
- [Django](https://www.djangoproject.com/) – JUSTIFICATION: Django is used as both a framework and templating engine to speed up the development of the project.
- [Gunicorn](https://gunicorn.org/) – JUSTIFICATION: Gunicorn is used as the WSGI HTTP Server.
- [PostgreSQL](https://www.postgresql.org/) – JUSTIFICATION: PostgresSQL is used as the database to make sure we have persistent storage for the recipes.
- [Psycopg2](https://pypi.org/project/psycopg2/) – JUSTIFICATION: Psycopg2 is a database adapter helping me to access the data and is required for Postgres.
- [Dj-database-url](https://pypi.org/project/dj-database-url/) – JUSTIFICATION: is used to link the database to our deployed version using a URL environment variable.
- [Dj3-cloudinary-storage](https://pypi.org/project/dj3-cloudinary-storage/) – JUSTIFICATION: is used to link cloudinary to our deployed version using a URL environment variable for persistent image storage.
- [Summernote](https://summernote.org/) – JUSTIFICATION: Summernote is used to allow users to type their own recipes into the website using a simple text editor.
- [Django-Allauth](https://pypi.org/project/django-allauth/0.13.0/) – JUSTIFICATION: Django-Allauth is being used to provide email authentication and password management.

[Back to Table Of Content](#table-of-content)

## Features
### Navbar / Dropdown Menu
- Featured on all pages across the website.
- The Navbar / Dropdown menu is fully responsive and changes to a hamburger style button for smaller screen sizes.
- The Navbar / Dropdown menu has a link to login or sign up for an account.
- The Navbar / Dropdown menu includes links to allow users to navigate around the website easily.
- The Navbar / Dropdown menu includes the dark theme switch toggler option for users that prefer to use a lighter of darker theme.
- user stories covered: 1,2,10,12,13
<details><summary>Navbar / Dropdown Menu</summary>
<img src="documentation/features/hamburger.jpg">
</details>
<details><summary>Navbar / Dropdown Menu Light</summary>
<img src="documentation/features/menu-light.jpg">
</details>
<details><summary>Navbar / Dropdown Menu Dark</summary>
<img src="documentation/features/menu-dark.jpg">
</details>
<br>

### Footer
- Featured across the whole website.
- The Footer contains links to the various social media handles.
- The Footer contains Information on how to get in touch with support when needed.
- The footer is fully responsive down to mobile size devices.
- User stories covered: 1,5,10
<details><summary>Footer</summary>
<img src="documentation/features/footer.jpg">
</details>
<br>