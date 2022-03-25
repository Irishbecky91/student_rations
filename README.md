# Student Rations

![Image name](file path)

[View the live project here](depolyed link)

## Table of contents
1. [Introduction](#Introduction)
2. [UX](#UX)
    1. [Ideal User Demographic](#Ideal-User-Demographic)
    2. [User Stories](#User-Stories)
    3. [Development Planes](#Development-Planes)
    4. [Design](#Design)
3. [Features](#Features)
    1. [Design Features](#Design-Features) 
    2. [Existing Features](#Existing-Features)
    3. [Features to Implement in the future](#Features-to-Implement-in-the-future)
4. [Issues and Bugs](#Issues-and-Bugs)
5. [Technologies Used](#Technologies-Used)
     1. [Main Languages Used](#Main-Languages-Used)
     2. [Additional Languages Used](#Additional-Languages-Used)
     3. [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)
6. [Testing](#Testing)
     1. [Testing.md](TESTING.md)
7. [Deployment](#Deployment)
     1. [Deploying on Heroku](#Deploying-on-Heroku)
     2. [Forking the Repository](#Forking-the-Repository)
     3. [Creating a Clone](#Creating-a-Clone)
8. [Credits](#Credits)
     1. [Content](#Content)
     2. [Media](#Media)
     3. [Code](#Code)
9. [Acknowledgements](#Acknowledgements)
***

## Introduction
This website was designed to display simple recipes for the student population. The focus of the site is to allow users to upload recipes and images for other users to search and use. 

Users will also be able to comment on recipes and upload images of their attempts at the recipe.

This is the fourth of five  Portfolio Projects that the developer must complete during their Full Stack Software Development (with eCommerce) Program at The Code Institute.

The main requirements were to build a Full-Stack site based on business logic used to control a centrally-owned dataset. This also requires the developer to set up an authentication mechanism and provide role-based access to the site's data or other activities based on the dataset.


[Back to top ⇧](#Student-Rations)

## UX 

### Ideal User Demographic
#### The ideal user of this website is:
- Students
- Parents
- Budgeting Individuals
- Cooking Enthusiasts

### User Stories
#### Users:
1. As a **user**, I can **view a paginated list of recipes** so that **I can more easily select a recipe to view**.

2. As a **user**, I can **view a list of recipes** so that **I can select one to make**.

3. As a **user**, I can **open a recipe** so that **I can see the required 
ingredients and steps to make the meal**.

4. As a **user**, I can **view the number of likes on a recipe** so that **I can decide if this recipe is worth trying**.

5. As a **user**, I can **read comments other users have left on a recipe** so that **I can see tips and reviews of the recipe**.

6. As a **user**, I can **register an account** so that **I can submit recipes or comment on and like others' recipes**.

7. As a **user**, I can **leave comments on recipes** so that **I can give tips for the recipe or review the recipe**.

8. As a **user**, I can **like or unlike a recipe or comment** so that **I can interact with the content**.

9. As a **user**, I can **upload images to the comments section** so that **I can show my attempts to replicate the recipe**.

10. As a **user**, I can **add recipes to a favourites page** so that **I can easily find the recipes again for future use**.

#### Site Admin:
1. As a **Site Admin**, I can **create, read, update and delete recipes** so that **I can manage my site content**.

2. As a **Site Admin**, I can **create drafts** so that **I can finish writing my site content later**.

### Development Planes
To create a comprehensive and appealing website, the developer researched other recipe based websites to discover what features and functionality would be required. This information created the above user stories and is developed further below.

#### Strategy
Broken into three categories, the website will attempt to focus on the following target audiences:
- **Roles:**
     - User
     - Admin

- **Demographic:**
     - Young adults
     - College/University students
     - Cooking Enthusiasts
     - People looking for budget meals

- **Psychographics:**
     - Personality & Attitudes:
        - Creative
	    - Outgoing
	    - Young
	    - Thrifty
     - Values:
        - Budget-minded
	    - Love of good food
     - Lifestyles:
        - Students
	    - Low-income families
	    - Interested in homemade food

The website needs to enable the **user** to:
- search for recipes.
- comment on and like recipes.
- upload images of their own experience using the recipe.
- register and log in to enable them to upload their recipes.
- add recipes to a favourites page.

The website needs to enable the **admin** to:
- approve recipe uploads.
- create drafts so they can be completed later.

With the user stories in mind, the developer created the below strategy table to determine the trade-off of importance and viability with the following results:

![Strategy Table](static/media/README/strategy-table.png 'Strategy Table')

#### Scope
A scope was define to identify what needed to be done to align features with the strategy previously defined. This was broken into two categories:
- **Content Requirements**
     - The user will be looking for:
        - a comprehensive list of recipes.
	    - a comprehensive list of ingredients and steps to follow.
	    - a list of comments and images of others' attempts to replicate the meal on each recipe page.
	    - a page to find all their favourite recipes.

- **Functionality Requirements**
     - The user will be able to:
        - Easily navigate the site to find the information they want.
	    - Be able to select recipes they wish to try.
	    - Comment on and like recipes.
	    - Upload images in the comments section to show their results of trying the recipe.

#### Structure
The information architecture was organized in a hierarchical tree structure to ensure that users could navigate through the site with ease and efficiency, with the following results
![Home Page Wireframe](static/media/README/site-map.png 'Site Map')

#### Skeleton 
Wireframe mockups were created using [Balsamiq](https://balsamiq.com/ 'Balsamiq Website'), providing a positive user experience with the following results:

Home Page:
![Home Page Wireframe](static/media/README/home-page-wireframe.png 'Home Page - Wireframe')

About Page:
![About Page Wireframe](static/media/README/about-page-wireframe.png 'About Page - Wireframe')

Search Page:
![Search Page Wireframe](static/media/README/search-page-wireframe.png 'Search Page - Wireframe')

Recipe Page:
![Recipe Page Wireframe](static/media/README/recipe-page-wireframe.png 'Recipe Page - Wireframe')

Favourites Page:
![Favourites Page Wireframe](static/media/README/favourites-page-wireframe.png 'Favourites Page - Wireframe')

### Design

#### Colour Scheme
The developer chose to use a clean black and white style page, with flashes of green throughout to hint towards healthy edible greens. This colour scheme was chosen as it is quite modern and it allows the colours from the recipes to be presented clearly and appear more attractive.

The black and white colouring give a very clean and clear view of the site content. The dark background is easier on the eyes, which for students can become quite strained due to their studies.

#### Typography
The font chosen for the logo was Courier New Bold as it is clear and concise, without any frills. This font was chosen as a representation of the site, showing clear concise recipes without all the added articles discussing each ingredient. This Logo was created by the developer using [GNU Image Manipulation Program (GIMP)](https://www.gimp.org/ 'GIMP Website')

The fonts chosen for this site are Roboto, for the headings, and Open Sans, for all other text, as these are popular and clear fonts which work well with the design of the site. Both of there fonts were chosen from [Google Fonts](https://fonts.google.com/ 'Google Fonts Website')

 Roboto from Google Fonts was chosen as it is a clean and concise font. For the paragraph text the font Open Sans from Google Fonts was chosen as it is a popular font that is also clean and concise.

#### Imagery
To match the colour scheme chosen, an image of some food and utensils on a dark background was chosen. This image has a few basic ingredients and gives a less threatening appearance to students who may be nervous about trying new recipes. On each recipe page, an image of the finished meal is shown with the recipe to allow the user to visualise the end product.

[Back to top ⇧](#Student-Rations)

## Features

### Design Features
Each page of the website features a consistent responsive navigational system:

- The **Header** contains a conventionally placed logo in the top left of the page (whereby by clicking this will redirect users back to the home page) and navigation bar in the center of the header. On smaller screens, the navigation bar condenses into a dropdown with navigation options.

- There is a **Header Image** on most pages, depicting a selection of ingredients and utensils on a dark background. This image is used to keep the theme consistant and is only missing in the recipe pages where the focus is instead brought to an image of the recipe itself, or a placeholder if none is provided.

- The **Footer** is divided into five sections, four columns and a bottom row. The first column contains a short blurb, telling the user about the site. The second contains useful links to utensil shopping, budgeting ideas and more. The third has navigation links to the Student Rations site. The fourth has a list of contact infomation. Finally the bottom row contains social links and copyright information. On smaller screens, this condenses into a single column, with each section moving underneath it's neighbour on the left.

<dl>
  <dt><a href="https://student-rations.herokuapp.com/" target="_blank" alt="Home Page">Home Page</a></dt>
  <dd>The Home Page is laid out with a nav section on top, an image below the width of the screen, the content area containing the recipe cards, followed by the footer. The features are as follows:
     <ul>
          <li><strong>A Welcome Note or Login Request</strong> - On the home screen you will see, below the header image, either a request to login or register to the site, or a heading welcoming the user to the site, citing the user's username.
          </li>
          <li><strong>Recipe Cards</strong> - The main content has recipe cards that are four cards across on large screens, two across on medium screens and one across small screens. This is paginated by eight so anything more than eight cards will be shown on the next page.
          </li>
          <li><strong>Next/Prev Page Link</strong> - If more than eight recipe's on the site, the remainder will be shown on the next page, with a max of eight cards on each of the following pages. To access these, there is a Next or Prev link that shows underneath the recipe cards.
          </li>
     </ul>
  </dd>

  <dt><a href="https://student-rations.herokuapp.com/about/" target="_blank" alt="About Page">Recipe Page</a></dt>
  <dd>This page shows the details of each recipe. This page does not contain a header image but is instead deivded into two sections on top, followed by a single column section and commenting section underneath. The features are as follows:
     <ul>
          <li><strong>Content</strong> - There is a short piece describing the origin of the site.
          </li>
     </ul>
  </dd>

  <dt><a href="https://student-rations.herokuapp.com/creamy-courgette-lasagne/" target="_blank" alt="Recipe Page - Chicken Caesar Salad">Recipe Page</a></dt>
  <dd>This page shows the details of each recipe. This page does not contain a header image but is instead deivded into two sections on top, followed by a single column section and commenting section underneath. The features are as follows:
     <ul>
          <li><strong>Featured Image</strong> - The featured image shows the image the user uploaded, or the placeholder image if no image was uploaded by the user.
          </li>
          <li><strong>Like/Unlike Button</strong> - If the user is logged in, the like/unlike button will appear green and will allow the user to like the recipe. If they have already liked the recipe, clicking the button will remove the like.
          </li>
          <li><strong>Edit/Delete Buttons</strong> - If the user is logged in and is the author of said recipe, clicking the edit button will bring the user to the edit page. The recipe details are populated into the form and the user is able to edit the information, upload a new image and save the information. Alternatively, clicking the delete button removes the recipe from the database and redirects the user back to the home page.
          </li>
          <li><strong>Comment Feature</strong> - If the user is logged in, the comment form is visible under the recipe on the right of the page. Entering a comment and submitting will then cause the form to disappear and a message will show advising the comment is awaiting approval. On approval, comments are displayed under the recipe on the left of the page, showing the users name and date and time of commenting.
          </li>
     </ul>
  </dd>

  <dt><a href="https://student-rations.herokuapp.com/edit-a-recipe/creamy-courgette-lasagne" target="_blank" alt="Edit Recipe Page - Chicken Caesar Salad">Recipe Page</a></dt>
  <dd>This page shows the details of each recipe. This page does not contain a header image but is instead deivded into two sections on top, followed by a single column section and commenting section underneath. The features are as follows:
     <ul>
          <li><strong>Featured Image</strong> - The featured image shows the image the user uploaded, or the placeholder image if no image was uploaded by the user.
          </li>
          <li><strong>Like/Unlike Button</strong> - If the user is logged in, the like/unlike button will appear green and will allow the user to like the recipe. If they have already liked the recipe, clicking the button will remove the like.
          </li>
          <li><strong>Edit/Delete Buttons</strong> - If the user is logged in and is the author of said recipe, clicking the edit button will bring the user to the edit page. The recipe details are populated into the form and the user is able to edit the information, upload a new image and save the information. Alternatively, clicking the delete button removes the recipe from the database and redirects the user back to the home page.
          </li>
          <li><strong>Comment Feature</strong> - If the user is logged in, the comment form is visible under the recipe on the right of the page. Entering a comment and submitting will then cause the form to disappear and a message will show advising the comment is awaiting approval. On approval, comments are displayed under the recipe on the left of the page, showing the users name and date and time of commenting.
          </li>
     </ul>
  </dd>
</dl>
 
### Existing Features
- **Feature** - feature description.
- **Feature** - feature description.
- **Feature** - feature description.

### Features to Implement in the future
- **Feature Name**
     - **Feature** - description.
     - **Reason for not featuring in this release** - reason.
 
[Back to top ⇧](#Student-Rations)

## Issues and Bugs 
Sample text about bugs

**Bug** - bug description.
	- ***Solution***: description

**Bug** - bug description.
	- ***Solution***: description

[Back to top ⇧](#Student-Rations)

## Technologies Used
### Main Languages Used
- [Technology](Wiki Link "description of link")
- [Technology](Wiki Link "description of link")

### Additional Languages Used
- [Technology](Wiki Link "description of link")
     - Used to .

### Frameworks, Libraries & Programs Used
- [Technology](Wiki Link "description of link")
     - Used to .

[Back to top ⇧](#Student-Rations)

## Testing

Testing information can be found in a separate testing [file](TESTING.md "Link to testing file")

## Deployment

This project was developed using .

### Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. 

### Forking the Repository
By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](https://github.com/rebeccatraceyt/KryanLive "Link to GitHub Repo").
3. At the top of the repository, on the right side of the page, select "Fork"
4. You should now have a copy of the original repository in your GitHub account.

### Creating a Clone
How to run this project locally:
1. Install the [GitPod Browser](https://www.gitpod.io/docs/browser-extension/ "Link to Gitpod Browser extension download") Extension for Chrome.
2. After installation, restart the browser.
3. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](https://github.com/rebeccatraceyt/KryanLive "Link to GitHub Repo").
5. Click the green "GitPod" button in the top right corner of the repository.
This will trigger a new gitPod workspace to be created from the code in github where you can work locally.

How to run this project within a local IDE, such as VSCode:

1. Log into [GitHub](https://github.com/login "Link to GitHub login page") or [create an account](https://github.com/join "Link to GitHub create account page").
2. Locate the [GitHub Repository](repo url "Link to GitHub Repo").
3. Under the repository name, click "Clone or download".
4. In the Clone with HTTPs section, copy the clone URL for the repository.
5. In your local IDE open the terminal.
6. Change the current working directory to the location where you want the cloned directory to be made.
7. Type 'git clone', and then paste the URL you copied in Step 3.
```
git clone https://github.com/USERNAME/REPOSITORY
```
8. Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub [here](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository "Link to GitHub troubleshooting")

[Back to top ⇧](#Student-Rations)

## Credits 

### Content
- sample text.

### Media
- images sourced from .
- Text sourced from .

### Code 
Did the developer use outside references when building code?
- [Stack Overflow](https://stackoverflow.com/ "Link to Stack Overflow page")
- [W3Schools](https://www.w3schools.com/ "Link to W3Schools page")
- [Bootstrap](https://getbootstrap.com/ "Link to BootStrap page")
- etc.


[Back to top ⇧](#Student-Rations)

## Acknowledgements

- I would like to thank my friends and family for their valued opinions and critic during the process of design and development.
- I would also like to thank my mentor, Name, for his/her invaluable help and guidance throughout the process.

[Back to top ⇧](#Student-Rations)

***
