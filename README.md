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

### User Sign Up
- The User sign up form allows users to create an account to interact with the community.
- When a user signs up for an account they are able to favorite and share their own recipes with the community.
- The User sign up form is fully responsive down to mobile size devices.
- User stories covered: 2,6,7,10,12,13
<details><summary>User Sign Up</summary>
<img src="documentation/features/user-sign-up.jpg">
</details>
<br>

### User Login
- The User login form allows users to login to an existing account to interact with the community.
- When a user logs in to their account they are able to favorite and share their own recipes with the community.
- The User login form is fully responsive down to mobile size devices.
- User stories covered: 6,7,10,12,13
<details><summary>User Login</summary>
<img src="documentation/features/user-login.jpg">
</details>
<br>

### Favorites
- The favorites are a feature of the user model, it acts as a list of ID's for the recipes the users likes the most and would like to come back to.
- The favorites feature also allows users make a list of items that they can find through their account page.
- The favorites feature also shows you the number of likes a recipe has received.
- User stories covered: 6,12
<details><summary>Favorites</summary>
<img src="documentation/features/favorites.jpg">
</details>
<br>

### Add and Edit Recipes
- The Add and Edit Recipe page allows the user to add their own recipe to the website.
- The Add and Edit Recipe page allows a users to edit their own recipes but should not allow them to edit others.
- The Add and Edit Recipe page is fully responsive down to mobile size devices.
- User stories covered: 7,10,12
<details><summary>Add and Edit Recipes</summary>
<img src="documentation/features/add-edit-recipes.jpg">
</details>
<br>

### Recipe List
- The recipes list is shown on the recipes page and displays a list of all the recipes.
- The recipes list is ordered by rating, this can be set by the admin.
- The recipes list is also paginated so that the user can only see 6 recipes at a time with navigation underneath.
- User stories covered: 1,3,4
<details><summary>Recipe List</summary>
<img src="documentation/features/recipe-list.jpg">
</details>
<br>

### Welcome Message/ Ethos
- The welcome message/ ethos is located on the home page and easily found as soon as you navigate to the site.
- The welcome message/ ethos lets users know they are getting a good service and unbiased opinion.
- User stories covered: 4
<details><summary>Welcome Message/ Ethos</summary>
<img src="documentation/features/welcome-message.jpg">
</details>
<br>

### Categories
- The categories page allows users to filter the recipes by what type of meal they are looking for.
- The categories page displays a list of only the current categories, if any are added or removed the list will update.
- The categories page is fully responsive down to mobile size devices.
- User stories covered: 1,3,9,10
<details><summary>Categories</summary>
<img src="documentation/features/categories.jpg">
</details>
<br>

### Featured Recipes
- The featured recipes are shown on the home page.
- The featured recipes are a list of recipes selected by the admin to be the best recipes.
- Only the featured recipes will show in this list, ordered by rating.
- The featured recipes list is fully responsive down to mobile size devices.
- User stories covered: 1,3,8,10
<details><summary>Featured Recipes</summary>
<img src="documentation/features/featured-recipes.jpg">
</details>
<br>

### Recipe Comments
- The Recipe  comments are shown on the Recipe details page.
- The Recipe comments are unique per Recipe.
- The Recipe comments are set to be manually approved by an admin for this project, in a real world deployment this can be changed to allow for different settings. 
- User stories covered: 7,12,14
<details><summary>Recipe Comments</summary>
<img src="documentation/features/recipe-comments.jpg">
</details>
<br>

### Error Pages
- The custom Error pages are used to replace the standard error pages from django.
- The custom Error pages cover 400, 404, 403, 500 errors.
- The featured recipes list is fully responsive down to mobile size devices.
- User stories covered: 1,10,11
<details><summary>Error Pages</summary>
<img src="documentation/features/error-pages.jpg">
</details>
<br>

### Social Media Links
- The social media links can be found in the footer.
- The social media links link to various social media handles, opening in a new tab.
- User stories covered: 5
<details><summary>Social Media Links</summary>
<img src="documentation/features/social-media-links.jpg">
</details>
<br>


[Back to Table Of Content](#table-of-content)

## Validation
### HTML Validation
I used the W3C Validation Service to validate the HTML of the website.
All pages passed with no errors and the contact form caused a warning that says there is an unnecessary script on page load, but this is required for the EmailJS form API to work, this was tested without the code and it will not function without it.
<details><summary>Base HTML</summary>
<img src="documentation/validation/validation-html-base.jpg">
</details>
<details><summary>Home Page</summary>
<img src="documentation/validation/validation-html-index.jpg">
</details>
<details><summary>Login Page</summary>
<img src="documentation/validation/validation-html-login.jpg">
</details>
<details><summary>Logout Page</summary>
<img src="documentation/validation/validation-html-logout.jpg">
</details>
<details><summary>Signup Page</summary>
<img src="documentation/validation/validation-html-signup.jpg">
</details>
<details><summary>Categories Page</summary>
<img src="documentation/validation/validation-html-categories.jpg">
</details>
<details><summary>Category Page</summary>
<img src="documentation/validation/validation-html-category.jpg">
</details>
<details><summary>Recipes Page </summary>
<img src="documentation/validation/validation-html-recipes.jpg">
</details>
<details><summary>Add / Edit Recipes Page </summary>
<img src="documentation/validation/validation-html-add-edit-recipes.jpg">
</details>
<details><summary>Account Page </summary>
<img src="documentation/validation/validation-html-Account.jpg">
</details>
<details><summary>Error Page </summary>
<img src="documentation/validation/validation-html-error.jpg">
</details>
<br>

### CSS Validation
I used the W3C Jigsaw CSS Validation Service to validate the CSS of the website.
My CSS passed with no errors and warnings to show.
<details><summary>CSS Validation</summary>
<img src="documentation/validation/validation-css-whole-page.jpg">
</details>
<br>

### JavaScript Validation
JSHint Static Code Analysis Tool for JavaScript was used to validate the Javascript files.
All Files passed with no errors and minimal warnings to show.
<details><summary>Theme Switch</summary>
<img src="documentation/validation/validation-js-theme.jpg">
</details>
<br>

### Python Validation
I used the PEP8 Validation Service to validate the python code for the website.
My code passed with no errors and warnings to show.

<details><summary>Recipe App</summary>

<details><summary>Python File</summary>
<img src="documentation/validation/validation-python.jpg">
</details>

</details>

<details><summary>Comments App</summary>

<details><summary>Python File</summary>
<img src="documentation/validation/validation-python.jpg">
</details>

</details>
<br>

### Accessibility
I used WAVE WebAIM web accessibility evaluation tool to ensure the website met high accessibility standards. All pages passed with no errors.
<details><summary>Home Page</summary>
<img src="documentation/validation/accessibility-index.jpg">
</details>
<details><summary>Login Page</summary>
<img src="documentation/validation/accessibility-login.jpg">
</details>
<details><summary>Logout Page</summary>
<img src="documentation/validation/accessibility-logout.jpg">
</details>
<details><summary>Signup Page</summary>
<img src="documentation/validation/accessibility-signup.jpg">
</details>
<details><summary>Categories Page</summary>
<img src="documentation/validation/accessibility-categories.jpg">
</details>
<details><summary>Category Page</summary>
<img src="documentation/validation/accessibility-category.jpg">
</details>
<details><summary>Recipes Page </summary>
<img src="documentation/validation/accessibility-recipes.jpg">
</details>
<details><summary>Add / Edit Recipes Page </summary>
<img src="documentation/validation/accessibility-add-edit-recipes.jpg">
</details>
<details><summary>Account Page </summary>
<img src="documentation/validation/accessibility-Account.jpg">
</details>
<details><summary>Error Page </summary>
<img src="documentation/validation/accessibility-error.jpg">
</details>
<br>

### Performance
Google Lighthouse in Google Chrome Developer Tools was used to test the performance of the website. 
<details><summary>Home Page</summary>
<img src="documentation/validation/lighthouse-index.jpg">
</details>
<details><summary>Login Page</summary>
<img src="documentation/validation/lighthouse-login.jpg">
</details>
<details><summary>Logout Page</summary>
<img src="documentation/validation/lighthouse-logout.jpg">
</details>
<details><summary>Signup Page</summary>
<img src="documentation/validation/lighthouse-signup.jpg">
</details>
<details><summary>Categories Page</summary>
<img src="documentation/validation/lighthouse-categories.jpg">
</details>
<details><summary>Category Page</summary>
<img src="documentation/validation/lighthouse-category.jpg">
</details>
<details><summary>Recipes Page </summary>
<img src="documentation/validation/lighthouse-recipes.jpg">
</details>
<details><summary>Add / Edit Recipes Page </summary>
<img src="documentation/validation/lighthouse-add-edit-recipes.jpg">
</details>
<details><summary>Account Page </summary>
<img src="documentation/validation/lighthouse-account.jpg">
</details>
<details><summary>Error Page </summary>
<img src="documentation/validation/lighthouse-error.jpg">
</details>
<br>

### Device Testing
The website was tested on the following devices:
- Huawei Matebook D15
- MacBook Pro 13” 2019
- Samsung Galaxy S21 FE 5G
- Samsung Galaxy S20 FE 5G
In addition, the website was tested using Google Chrome Developer Tools Device Toggling option for all available device options.

### Browser Compatibility
The website was tested on the following browsers in both regular and incognito modes:
- Google Chrome
- Mozilla Firefox
- Microsoft Edge

## Testing user stories
### Manual Testing
<br>
1. As a first time user I would like to be able to navigate through the website easily so that it is easy to find the information I am looking for.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Navbar / Dropdown Menu | On any page of the website, at the top of the page, find the Navbar and use it to navigate to a new page | Navbar link takes you to the selected page | Works as expected |
| Footer | On any page of the website, at the bottom of the page, locate the footer containing contact and social media information | Footer is located at the bottom of every page. | Works as expected |
| Error Pages | From any page on the website, go to the URL bar and add onto the end of the url a random string on characters to be redirected to an error page | The error page loads as expected. | Works as expected |
<details><summary>Screenshots</summary>
<img src="documentation/user-story-testing/user-story-x.jpg">
</details>
<br>

2. As a first time user I would like to be able to sign up for an account so that I can interact with the community.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| User Sign Up | From any page on the website, when not logged in, locate the Sign Up button on the Navbar to take you to the Sign Up form. | Fill out and submit the form to be signed into your account. | Works as expected |
<details><summary>Screenshots</summary>
<img src="documentation/user-story-testing/user-story-x.jpg">
</details>
<br>

3. As a first time user I want to see the available recipes that are on the website so that I can learn eat healthier.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Recipe List | From any page on the website use the Navbar to navigate to the Recipes page. | See a list of all the recipes orders by their ratings | Works as expected |
| Categories | From any page on the website use the Navbar to navigate to the Categories page. | See a list of all the Categories on the website. | Works as expected |
| Featured Recipes | From any page on the website use the Navbar to navigate to the Featured Recipes page. | See a list of all the Featured Recipes orders by their ratings | Works as expected |
<details><summary>Screenshots</summary>
<img src="documentation/user-story-testing/user-story-x.jpg">
</details>
<br>

3. As a first time user I want to see the available recipes that are on the website so that I can learn eat healthier.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Recipe List | From any page on the website use the Navbar to navigate to the Recipes page. | See a list of all the recipes orders by their ratings | Works as expected |
| Categories | From any page on the website use the Navbar to navigate to the Categories page. | See a list of all the Categories on the website. | Works as expected |
| Featured Recipes | From any page on the website use the Navbar to navigate to the Featured Recipes page. | See a list of all the Featured Recipes orders by their ratings | Works as expected |
<details><summary>Screenshots</summary>
<img src="documentation/user-story-testing/user-story-x.jpg">
</details>
<br>
