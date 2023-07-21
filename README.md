# Movie Crazy Club
(Developer: Femi Ashiru)

![Movie Crazy Club Website Responsive Image](docs/am-i-responsive.png)

[Live Project](https://movie-crazy-club-73ece9687233.herokuapp.com/show_movies)

[Github Repo](https://github.com/ofemiashiru/CI_MS3_MCC)

## Table of Content

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
    4. [Scope](#scope)
3. [Design](#design)
    1. [Design Choices](#design-choices)
    2. [Colour](#colour)
    3. [Fonts](#fonts)
    4. [Structure](#structure)
    5. [Wireframes](#wireframes)
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks and Tools](#frameworks-and-tools)
5. [Features](#features)
6. [Testing](#validation)
    1. [HTML Validation](#HTML-validation)
    2. [CSS Validation](#CSS-validation)
    3. [JS Validation](#JS-Validation)
    4. [Accessibility](#accessibility)
    5. [Performance](#performance)
    6. [Responsiveness](#responsiveness)
    7. [Device testing](#performing-tests-on-various-devices)
    8. [Browser compatibility](#browser-compatibility)
    9. [Testing user stories](#testing-user-stories) 
7. [Bugs](#Bugs)
8. [Deployment](#deployment)
9. [Credits](#credits)
10. [Acknowledgements](#acknowledgements)


## Project Goals 

### User Goals
- Play QuickShot game.
- Save Score to the leader board.
- Contact Quickshot Site Owner.

### Site Owner Goals
- Allow users to play QuickShot game.
- Receive messages from QuickShot players.
- Show users the top ten QuickShot Players.

## User Experience

### Target Audience
- People who are fans of nostalgic 80s games. 
- People who are fans of shoot and aim games.
- People who are competitive and relish a challenge.

### User Requirements and Expectations

- Easy to use navigation that is responsive.
- Be able to easily browse between sections of the site and the game.
- All links to work as expected.
- Appealing design that works well on both desktop and mobile devices.
- Be able to play game on Mobile, tablet and desktop device.
- Be able to contact QuickShot game site.
- Accessibility.

### User Stories

#### First-time User 
1. I want to play the QuickShot game.
2. I want to save my score on the leader board.
3. I want to see the leader board.
4. I want to contact QuickShot game site.

#### Returning User
5. I want to see all the top ten scores.
6. I want to be able to see if I can top the leader board.
7. I want to be able to contact QuickShot game site.

#### Site Owner 
8. I want users to be able to play QuickShot game on mobile, tablet and desktop.
9. I want users to be able to save their score to the leader board.
10. I want users to be able to see the top ten scores.
11. I want users to be able to contact us.
12. I do not want users to use browser back button if they are looking for a page that does not exist.
13. Inform users that the game will be coming to App store and Google Play soon
14. I want users to take a quiz that tests their video game knowledge, to pass the time.

## Scope

The scope of the project in its first release is defined by the following features:

- Simple navigation that allows user to navigate between sections of the site and the game. 
- Game page that allows user to play game, see how to play game, save score to the leader board and navigate back to main site.
- Allow user to see their score on the leader board if they have reached the top ten.
- Allow users to see the top ten players on the leader board.
- Contact form to allow users to send queries. The form is fully functional using EmailJS and will not submit unless all fields are filled out.
- An error page (404.html) that appears when visiting a page that does not exist with navigation above.
- Clear and simple favicon icon to help users identify the site.

Features to be built in future releases:

- Addition of social media links when QuickShot develop their social media platforms.
- Active links to Apples App store and Google Plays store when the game becomes available on these platforms.

## Design

### Design Choices
QuickShot was designed to have an old school 80s game look that adopted some of the layout from 80s game displays creating a sense of nostalgia. The site is a simple scrolling page as it didn't need to be too complex and is simply made to advertise the game, display the leader board and give user the facility to send messages. The game design has a similar look to an old Nintendo game as I was looking to show how modern technology can still give users a sense of nostalgia while playing.

### Colour

For the colour scheme I opted for an army fatigue palette of greens and browns to match the theme of the game.

![Colour Scheme](docs/features/colour-scheme.png)

### Fonts

The main headings of the site and game use Press Start 2P with a fallback of sans-serif to mimic the look of 80s games. This font is also used on the navigation. For the body text of the site I opted for the Oswald font which also has a fallback of sans-serif. Both fonts were imported using Google Fonts API.

### Structure
The main site is structured with different sections for each page . Both main site and game are responsive in nature and have been tested on the industry standard width of 320px.

The website consists of 6 main pages:
- Home page which shows what the site is about, featured albums, and the various subscription options
- Artist page which allows users to browse the artist they want to listen to by letter and shows the top three featured artists
- Genre page which allows users to browse the artist they want to listen to by genre
- Events page which allows users to see the latest events and navigate to their corresponding sites
- News page which allows users to see and keep up with the latest news
- Contact page which allows users to contact the business and locate the office

### Wireframes

<details><summary>index.html</summary>
<img src="docs/wireframes/index.png" alt="index wireframe">
</details>
<details><summary>game.html</summary>
<p>Game Home</p>
<img src="docs/wireframes/game_home.png" alt="game home wireframe">
<p>How to play</p>
<img src="docs/wireframes/how_to_play.png" alt="game how to play wireframe">
<p>Game Display</p>
<img src="docs/wireframes/game_display.png" alt="game display wireframe">
<p>Game Over Screen</p>
<img src="docs/wireframes/game_over_screen.png" alt="game over screen wireframe">
</details>
<details><summary>404.html</summary>
<img src="docs/wireframes/404.png" alt="404 wireframe"> 
</details>

## Technologies Used

### Languages
- HTML
- CSS
- JavaScript

### Frameworks and Tools
- Bootstrap v4.5 - simply for base css
- Git
- GitHub
- Gitpod
- Balsamiq
- Ezgif.com
- Google Fonts
- Adobe Color
- Font Awesome
- Favicon<span>.</span>io
- Open Trivia DB 

## Features

### Logo Navigation and Search bar
- Navigation and Logo remains consistent on each page apart from game page (link to main site on game)
- Navigation is fully responsive and collapses when window is resized
- Navigation allows users to easily navigate from section to section and from main site to game
- Logo in Navigation takes user back to the home page

<p>Nav on Desktop</p>

![Logo Navigation on Desktop](docs/features/feature-navigation-bar-1.png)

<p>Nav on Tablet(Closed)</p>

![Logo Navigation on Tablet (Closed)](docs/features/feature-navigation-bar-2.png)

<p>Nav on Tablet(Open)</p>

![Logo Navigation and Tablet (Open)](docs/features/feature-navigation-bar-3.png)

<p>Nav on Mobile(Open)</p>

![Logo Navigation and Mobile (Open)](docs/features/feature-navigation-bar-4.png)

### Hero Section
- Greets user on entering the site and displays game on different screen sizes
- Shows user that QuickShot game will be coming soon on App store and Google Play (User story - 13)

![Hero Section](docs/features/feature-hero.png)

### About Section
- Informs user of what the QuickShot game is about 

![About Section](docs/features/feature-about.png)

### Leader board Section
- Informs users of the top ten players (User story - 3, 10)

![Leader board Section](docs/features/feature-leaderboard.png)

### Quiz Section
- Allows users to play a Video Game related quiz to pass the time (User story - 14)

![Quiz Section](docs/features/feature-quiz.png)

### Contact Section
- Allows users to send queries and messages to site owner (User story - 4, 7, 11)

![Contact Section](docs/features/feature-contact.png)

### Footer
- Features on all pages
![Footer](docs/features/feature-footer.png)

### Game
- Allows users to play the Quick Shot Game (User story 1, 6, 8)
- Allows users to save their score to the leader board, if it is a top ten score it will appear on the board (User story 2, 6, 9)

<p>Game Home screen</p>

![Game Play - Home](docs/features/feature-game-home.png)

<p>Game Play screen</p>

![Game Play - Display](docs/features/feature-game-display.png)

<p>Game Over screen</p>

![Game Play - Display](docs/features/feature-game-over.png)

### 404 Page
- Allow users to navigate back to site without the use of back button on browser when visiting a page that does not exist (User story - 12)

![404 page](docs/features/feature-404.png)

## Validation

### HTML Validation
The W3C Markup Validation Service was used to validate the HTML of the website. 

index.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fofemiashiru.github.io%2FCI_MS2_QSG%2Findex.html) - No Errors Found

game.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fofemiashiru.github.io%2FCI_MS2_QSG%2Fgame.html) - No Errors Found

404.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fofemiashiru.github.io%2FCI_MS2_QSG%2F404.html) - No Errors Found

### CSS Validation
The W3C Jigsaw CSS Validation Service was used to validate the CSS of the website.
After testing the whole sites CSS and my own custom CSS all pages passed with no errors, however, there were a number of warnings present that were related to the webkit css extensions used.

whole site [results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fofemiashiru.github.io%2FCI_MS2_QSG%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) - No Errors Found

custom css [results](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fofemiashiru.github.io%2FCI_MS2_QSG%2Fassets%2Fcss%2Fstyle.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) - No Errors Found

### JS Validation

[JS Hint](https://jshint.com/) was used to validate the JavaScript of the website.

<details><summary>index.js</summary>
<img src="docs/validation/js/index_js.png" alt="index script">
</details>

<details><summary>game.js</summary>
<img src="docs/validation/js/game_js.png" alt="game script">
</details>

<details><summary>highScore.js</summary>
<img src="docs/validation/js/highScore_js.png" alt="highScore script">
</details>

<details><summary>getHighScore.js</summary>
<img src="docs/validation/js/getHighScore_js.png" alt="gethighScore script">
</details>

<details><summary>quiz.js</summary>
<img src="docs/validation/js/quiz_js.png" alt="quiz script">
</details>

<details><summary>contact.js</summary>
<p>Initially the variable was called in the HTML file in accordance with the usage of EmailJS, however, I moved it into the JS file as I didn’t want to have any JS displayed in my HTML and wanted to adhere to separation of concerns.</p>
<p>This is the reason the warning appears about the undefined variable.</p>
<img src="docs/validation/js/contact_js.png" alt="contact script">
</details>


### Accessibility
The WAVE WebAIM web accessibility tool was used to ensure the website met accessibility standards. 

index.html [results](https://wave.webaim.org/report#/https://ofemiashiru.github.io/CI_MS2_QSG/index.html) - No Errors Found.

game.html [results](https://wave.webaim.org/report#/https://ofemiashiru.github.io/CI_MS2_QSG/game.html) - No Errors Found.

404.html [results](https://wave.webaim.org/report#/https://ofemiashiru.github.io/CI_MS2_QSG/404.html) - No Errors Found.

### Performance 
Google Lighthouse Tool was used to test the performance of the website. 
<details><summary>Home</summary>
<img src="docs/validation/performance/lighthouse-performance-index.png" alt="lighthouse for index">
</details>
<details><summary>Game</summary>
<img src="docs/validation/performance/lighthouse-performance-game.png" alt="lighthouse for game">
</details>
<details><summary>404</summary>
<img src="docs/validation/performance/lighthouse-performance-404.png" alt="lighthouse for 404">
</details>

### Performing tests on various devices 
The website was tested on the following devices:
- Apple MacBook Pro M1
- Apple iPhone 11
- Xiaomi Mi 11 Lite

### Browser compatibility
The website was tested on the following browsers:
- Google Chrome
- Safari
- Mozilla Firefox
- Microsoft Edge

### Responsiveness
The website is completely responsive and has been tested on mobile, tablet and desktop:

<details><summary>Mobile, Tablet and Desktop</summary>
<p>Part One</p>
<img src="docs/responsiveness/respsonsiveness-part-one.gif" alt="Responsiveness Part One">
<p>Part Two</p>
<img src="docs/responsiveness/respsonsiveness-part-two.gif" alt="Responsiveness Part Two">
</details>




### Testing user stories

- Please note that these screen recordings were taken before the play now buttons and quiz were added
- However the quiz itself has been added to fulfil user story 14

1. I want to play the QuickShot game.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Nav and Game Page | Click play game on Nav in index.html and start game on game.html | Game.html page opens and game should start when start game is clicked | Works as expected |

<details><summary>Screen recording</summary>
<img src="docs/user-story-testing/user-story-1-6-8.gif">
</details>

2. I want to save my score on the leader board.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Page | When game over screen appears, enter name and click save | Main page should open and smooth scroll to leader board section showing newly added score if it is in the top ten | Works as expected |

<details><summary>Screen recording</summary>
<img src="docs/user-story-testing/user-story-2-6-9.gif">
</details>

3. I want to see the leader board.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Nav | Click leader board on Nav in index.html | Main page should smooth scroll to leader board section | Works as expected |

<details><summary>Screen recording</summary>
<img src="docs/user-story-testing/user-story-3-5-10.gif">
</details>

4. I want to contact QuickShot game site

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Contact Section | Click contact on Nav in index.html, enter details in text boxes and click send button | Page should smooth scroll to contact section, allow user to enter fields and only send if all fields are entered. On clicking send a message should appear beneath informing user of whether or not the message was sent successfully | Works as expected |

<details><summary>Screen recording/ Screenshot</summary>
<img src="docs/user-story-testing/user-story-4-7-11.gif">
<img src="docs/user-story-testing/user-story-4-7-11.png">
</details>


5. I want to see all the top ten scores.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Nav | Click leader board on Nav in index.html | Main page should smooth scroll to leader board section | Works as expected |

<details><summary>Screen recording</summary>
<img src="docs/user-story-testing/user-story-3-5-10.gif">
</details>

6. I want to be able to see if I can top the leader board.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Nav and Game Page | Click play game on Nav in index.html and start game on game.html | Game.html page opens and game should start when start game is clicked | Works as expected |

<details><summary>Screen recording</summary>
<img src="docs/user-story-testing/user-story-1-6-8.gif">
</details>

7. I want to be able to contact QuickShot game site.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Contact Section | Click contact on Nav in index.html, enter details in text boxes and click send button | Page should smooth scroll to contact section, allow user to enter fields and only send if all fields are entered. On clicking send a message should appear beneath informing user of whether or not the message was sent successfully | Works as expected |

<details><summary>Screen recording/ Screenshot</summary>
<img src="docs/user-story-testing/user-story-4-7-11.gif">
<img src="docs/user-story-testing/user-story-4-7-11.png">
</details>


8. I want users to be able to play QuickShot game on mobile, tablet and desktop.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Nav and Game Page | Click play game on Nav in index.html and start game on game.html | Game.html page opens and game should start when start game is clicked | Works as expected |

<details><summary>Screen recording</summary>
<img src="docs/user-story-testing/user-story-1-6-8.gif">
</details>

9. I want users to be able to save their score to the leader board.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Page | When game over screen appears, enter name and click save | Main page should open and smooth scroll to leader board section showing newly added score if it is in the top ten | Works as expected |

<details><summary>Screen recording</summary>
<img src="docs/user-story-testing/user-story-2-6-9.gif">
</details>

10. I want users to be able to see the top ten scores.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Nav | Click leader board on Nav in index.html | Main page should smooth scroll to leader board section | Works as expected |

<details><summary>Screen recording</summary>
<img src="docs/user-story-testing/user-story-3-5-10.gif">
</details>

11. I want users to be able to contact us.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Contact Section | Click contact on Nav in index.html, enter details in text boxes and click send button | Page should smooth scroll to contact section, allow user to enter fields and only send if all fields are entered. On clicking send a message should appear beneath informing user of whether or not the message was sent successfully | Works as expected |

<details><summary>Screen recording/ Screenshot</summary>
<img src="docs/user-story-testing/user-story-4-7-11.gif">
<img src="docs/user-story-testing/user-story-4-7-11.png">
</details>


12. I do not want users to use browser back button if they are looking for a page that does not exist.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| 404 Page| Enter incorrect URI in address bar| 404 page should appear with Header and footer allowing user to navigate to a different page | Works as expected |

<details><summary>Screen recording</summary>
<img src="docs/user-story-testing/user-story-12.gif">
</details>


13. Inform users that the game will be coming to App store and Google Play soon

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Nav and Hero Section | Click Home on Nav in index.html | Page should smooth scroll to home section show users that QuickShot will be coming to App Store and Google Play store soon (Desktop only) | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/user-story-testing/user-story-13.gif">
</details>

14. I want users to take a quiz that tests their video game knowledge, to pass the time.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Quiz Section | Complete quiz in index.html | Quiz section should ask 10 questions one by one giving feedback for each response and give a total at the end of quiz allowing user to restart | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/user-story-testing/user-story-14.gif">
</details>

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Quiz Section | Choose no value for quiz question | Message should appear informing user to choose a value | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/user-story-testing/user-story-14b.gif">
</details>


## Bugs

| **Bug** | **Fix** | 
|-------------|------------|
|Receiving the error message ```An invalid form control with name='' is not focusable``` when submitting answer without picking true or false|As the element created was set to required the DOM was searching for the element but could not find it as I set it the display property to none - created custom validation within the quiz.js file starting on line 170 to handle non input.|

```
if(!userAnswer){
    document.querySelector('#answer-feedback').innerHTML = '> Please select True or False! <';
    return;
}
```

## Deployment

Deployed using GitHub Pages using the following steps:
1. Whilst in GitHub repository navigate to the Settings tab
2. On the left hand menu select Pages
3. Scroll to "Branch" tap none to show the different options and select "main"
4. Click save and the site will be published. You will see "Your site is live at https://ofemiashiru.github.io/CI_MS2_QSG/"

You can also fork the repository by:
1. Navigating to the GitHub repository
2. Click on "Fork" button in top right hand corner (Please note you must be signed in to Fork a repository)

You can clone the repository by:
1. Navigating to GitHub repository 
2. Locate the "Code" button above the file list and click it 
3. Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to where you wish to clone the directory
6. Type ```git clone``` and paste in the URL from the clipboard e.g ```$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)```
7. Press Enter to create your local clone in your chosen folder.

## Credits
Images not referenced below are owned by the Developer or created by Developer using CSS3.

### Media

[Cross hair used for cursor](assets/images/crosshair.png), taken from [Flaticon - created by xnimrodx](https://www.flaticon.com/free-icon/focus_865240?term=crosshair&page=1&position=20&origin=tag&related_id=865240)

[QuickShot logo](assets/favicon/android-chrome-512x512.png), taken from [Favicon.io](https://favicon.io/emoji-favicons/direct-hit)

[Questions used in Quiz](https://opentdb.com/api.php?amount=10&category=15&type=boolean). API generated using [Open Trivia Database](https://opentdb.com/)

### Code

- Used [Compart](https://www.compart.com/en/unicode/U+2022) to add appropriate Unicode for bullet points in game

- Used [w3schools.com](https://www.w3schools.com/jsref/met_win_setinterval.asp) to aid in using setInterval function

- Used [w3schools.com](https://www.w3schools.com/jsref/met_win_clearinterval.asp) to aid in using clearInterval function

- Used [w3schools.com](https://www.w3schools.com/jsref/met_document_removeeventlistener.asp) to aid in using the removeEventListener function

- Used [w3schools.com](https://www.w3schools.com/cssref/pr_scroll-behavior.php) to help with adding smooth scrolling to index.html

- Used [w3schools.com](https://www.w3schools.com/cssref/pr_class_cursor.php), [stackoverflow.com - show custom cursor](https://stackoverflow.com/questions/6623769/css-custom-cursor-doesnt-work-in-ff-chrome ) and [stackoverflow.com - centre cursor](https://stackoverflow.com/questions/19560878/css-change-custom-cursor-image-origin-hotspot-to-center) to create a custom cursor, to help show a custom cursor and to centre the custom cursor

- Used [w3schools.com](https://www.w3schools.com/cssref/css3_pr_box-shadow.php) to help add box shadows to images

- Used [stackoverflow.com](https://stackoverflow.com/questions/3186688/drop-shadow-for-png-image-in-css) to help add drop shadows to PNGs

- Used [w3schools.com](https://www.w3schools.com/css/css3_animations.asp) to add animation to the game labels when a target is hit

- Used [w3schools.com](https://www.w3schools.com/howto/howto_css_modals.asp) to assist with creating modals on game.html

- Used [w3schools.com](https://www.w3schools.com/css/css_grid.asp) to assist with using grid layout in CSS

- Used [w3schools.com](https://www.w3schools.com/css/css3_transitions.asp) to assist with using transitions in CSS

- Used [w3schools.com](https://www.w3schools.com/jsref/prop_win_localstorage.asp) to assist with saving and retrieving data from the local storage, and [stackoverflow.com](https://stackoverflow.com/questions/40843773/localstorage-keeps-overwriting-my-data) to stop the local storage data from being overwritten with new data

- Used [w3schools.com](https://www.w3schools.com/howto/howto_js_redirect_webpage.asp) to assist with redirecting to a new page

## Acknowledgements

I would like to take the opportunity to thank:
- Mo Shami for continued mentorship, guidance and support throughout this project. 
- Iris Smok for continued encouragement whilst working on this project.
- and all the Teaching and Non-teaching Personnel at Code Institute.