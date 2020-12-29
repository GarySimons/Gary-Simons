

![IMG](/static/images/birdreadme.png)


# Gary Simons - personal resume website



## Overview

### Please note that the interface for creating, updating and deleting data is on the 'hidden' admin page. To access this page please enter *'/admin'* at the end of the url.


This is a website to **promote me as a full stack web developer**. In the future, I shall be able to use it to send to potential employers as a way of **advertising my skills.** It has been built using **template inheritance** which will make it easier to add content as my projects and skills grow. 


The aim of the project is to produce a website using **Flask** and **Python** that allows the use of data stored in a database on **MongoDB**. The website has to demonstrate the data storage principles that you should be able to **create, read, update and delete (CRUD)** that data through a user interface. For my project, the **user** of that interface will be **me** as the website's owner. 


**I have 'hidden' an admin section**, which can be accessed by **entering **'/admin'** at the end of the url.** This takes you to the **admin page**, from which you can read, add, update or delete the data. The data is **displayed to the user** in a panel on the **about page**, using easy to digest **text and progress bars to show skills and skill levels attained**. This text and the progress bars are **linked to the MongoDB database** and change when it is edited.


The site is hosted on **Heroku** as part of the project requirements.

### The goals of this website are:
* To build brand awareness.
* To showcase my coding skills to potential employers and recruiters.
* To exhibit my creative style to potential employers and recruiters.
* Intuitive navigation to keep the user engaged.

---

## UX

### This website is:
* Easy to navigate.
* Displays easy to read, simple, useful information.
* Has pleasing colours, illustration and typography.
* Fully responsive to work and look visually appealing on all viewing devices.
* Enabling recruiters and employers to see my skills, experience and education.
* Enabling recruiters and employers to see my work.
* Enabling recruiters and employers to contact me.
* Enabling recruiters and employers to access my social media.

---

## Users

### User stories:
* As a user of the website, I want to **navigate easily** and find the **information I need quickly**.
* As a user of the website, I want an **engaging design** that is visually appealing and stimulating.
* As a user of the website, I want **good user experience** to keep the me engaged.
* As a user of the website, I want to **view it on all devices** and it still to look good and work perfectly.
* As a user of the website, I want to be able to **contact the site owner**.
* As a user of the website, I want to **learn more about the developer as a person**.
* As a potential client or employer, I want to **view the technical skills** of the developer.
* As a potential client or employer, I want to **view the training and relevant education** of the developer.
* As a potential client or employer, I want to **view the work portfolio of the developer** to decide if I like their style.
* As a user of the website, I want to be able to **view the developer's social media** to feel more engaged with them.
* As a potential client or employer, I want to be able to **view the developer's LinkedIn** account.
* As a potential client or employer, I want to be able to **view the developer's GitHub** account.
* As a potential client or employer, I want to be able to **download the developer's CV**.

### Website owner stories:
* As the website owner, I want the website to be a **shop front** for me as a developer.
* As the website owner, I want the website to **display skills** and work to potential employers.
* As the website owner, I want to receive messages from users which could **lead to employment**. 
* As the website owner, I want to receive messages from users which could **lead to collaboration with other developers**. 
* As the website owner, I want to **update and add skills via the admin page** linked to my MongoDB database.
* As the website owner, I want to **update and add projects and work** to enhance the opportunities for employment.

---

## Design choices

**The website is designed to reflect me as a creative full stack web developer** and show my style. The website is clean and stylish, using muted blocks of colour to define areas. 

### Colours
I created a **simple, complimentary, sophisticated colour scheme** that carries through the site. This enables the different pages to have their own feel and identity, while maintaining a holding colour theme that ties them all together, giving an upmarket feel.
* ```dark-grey: #4d4d4d```
* ```light-grey: #a6a6a6```
* ```dark-pink: #a34966```
* ```light-pink: #d996a9```
* ```dark-green: #5c9990```
* ```light-green: #bacfb2```
* ```dark-blue: #3c5682```
* ```light-blue: #688499```

### Fonts
I've used the sans serif font [Montserrat](https://fonts.google.com/specimen/Montserrat) in two weights, (300 and 500) with some **sophisticated letter spacing** to add to the airy feel. I like the no-nonsense clean lines of the font, and feel it suits the website perfectly.

### Grid
I carried the **same basic grid through** the pages to add consistency and easy of navigation. A large **section header** quickly establishes the page you've landed on, and under that, is a panel holding the content for that page. A footer on each page hold **social media links and a downloadable CV.**

### Illustration
I created an image of a **woodcut style bird** carrying a card with the coding symbol **</>** on it. It is not only a beautiful image, but symbolizes me delivering coding solutions. I have used this image throughout the website and a visual logo of the website and of me.

---

## Wireframes

I built my wireframes using **Balsamiq Wireframes**. This was a quick and easy way to work out the basic pages and element and how the would interact with each other. I then mocked up more detailed versions using **Adobe InDesign** to allow me to play with fonts, colours and images. The basic structure from my wireframes remained much the same, but colours, styling and some elements were adapted as I built the website and saw how it worked as a whole.   

View my **Balsamiq** wireframes <a href="https://github.com/GarySimons/Gary_Simons/tree/master/wireframes/png">here.</a>

View my **Adobe InDesign** wireframes <a href="https://github.com/GarySimons/Gary_Simons/tree/master/wireframes/jpg">here.</a>

---

## Features

### Navigation bar
**This holds all the links to the sections of the site:** Logo (home button), home, about, projects and contact. This allows the user to navigate quickly to the relevant section. The **navigation bar** is always visible when you are on the site, allowing for easy navigation to any part, no matter where you first land. The **home button and logo** will take you right back to the **home page** where you can get your bearings and start your journey.

### Home
This is the first page a user comes to and it has to make a big impact. It has the job of informing the user as to what sort of site this is and to entice them to move further and engage with it. It opens with **strong simple white typography** on a plain grey background. Having a big name announces very quickly who the website is about. The tag line underneath then gives more context and explains what they do. **A beautiful illustration of a bird holding a card with </> on it symbolizes delivering code.** A tasteful **about me** link invites them to enter the website and takes the user straight to the **about page** where they can learn more.

### About
The about page shows some of the **key information about me.** There is a brief introduction to me and the things I stand for. Below that are two panels. One showing **my skills** with an easy to understand progress bar showing my proficiency level in a graphic way. The other shows my **relevant education and qualifications.** All pages apart from the home page have a **footer**, which holds links to my **LinkedIn, GitHub, Twitter, Facebook, Instagram** and a **downloadable pdf of my CV.** It has a **copyright** sign off displaying the current year.  

### Projects
The projects page highlights some of the **work I have been doing.** Each project is in a coloured panel with the website showing in a graphic line drawing of a laptop. A **view button** under each title opens a **large modal** with larger images of a laptop, tablet and phone. There is a short description of the website, a list of programs and languages used and a link to the **live website.** This gives the user an insight into the thinking behind the website and the way it was built. They can see how it displays on different devices, and then link to the website to see for themselves. I used the two websites that I have built as **Milestone Projects** and made two **fake website homepages** to show how it would work with more.

### Contact
The contact page simply holds a **form for users to fill in and contact me.** I kept the wording on the page very **inviting and conversational** to help the user feel more at ease and give a **friendly vibe.** 

### Admin (Accessed by adding *'/admin'* to the url)
The admin page is the **interface with the MongoDB database.** It shows a panel showing the **stored data.** Beside each of the listings are two buttons, **edit** and **delete.** Below is a **add new skill** button. 

#### Edit
The **edit button** opens a new page where it shows the data that you've clicked on in a form that allows for them to be edited. Below are a **save changes button** with sends the updated data to **MongoDB**, and a **back to skills button** which takes you back to the list of skills on the **admin page.**

#### Add
The **add skills button** opens a page with a form that needs to be filled in with a new skill and new proficiency level. The form has place-holder text to prompt the correct way to input the data. There is a **add skill button** which adds that skill and level to the **MongoDB database**. Again there is a **back to skills button** which takes you back to the list of skills on the **admin** page. 

#### Delete
The **delete button** on the page is actually a button that opens a **modal** that acts as a safety net to stop skills being deleted by accident. The message on the modal asks the question **'are you sure you want to delete this skill? once you press this button it's gone for good!'** There are then two buttons **'yes. i'm sure'** which is actually the **'real'** delete button that is wired up to remove the data. The other button **'no. keep it'** takes the user safely back to the **admin** page with no harm done. All the buttons on the website share common styles with two different widths. All the changes made in these panels are reflected in the information on the **about page.**

### Favicon
The website has a **Favicon** to visually show the user where the site is in their open tabs. It uses the **GS** logo from the navigation bar on the same grey background to tie it together.

---

## Features left to implement

* If time allowed I would have liked to add to the admin page, to enable me to **build more projects.** I would build a template that would allow me to quickly and simply add as many as needed.
* It would be good to add a **blog page.** This would give another insight into my interests, skills and personality, and allow the users to be more engaged with me as a person.
* I would like to **wire up the contact form** to send messages to my email.

---

## Technologies used

#### Languages
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [Python](https://www.python.org/)
* [JavaScript](https://www.javascript.com/)
* [jQuery](https://jquery.com/)

#### Frameworks and libraries
* [Flask](https://flask.palletsprojects.com/en/1.1.x/#)
* [Bootstrap](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
* [Font Awesome](https://fontawesome.com/)
* [Google Fonts](https://fonts.google.com/)
* [PopperJS](https://popper.js.org/)


#### Tools
* [MongoDB](https://account.mongodb.com/account/login)
* [Heroku](https://www.heroku.com/)
* [Balsamiq Wireframes](https://wireframestogo.com/)
* [TinyPNG](https://tinypng.com/)
* [Genfavicon](http://www.genfavicon.com/)

---

## Testing
* This was first time using **Python, Flask and MongoDB.** My testing was very thorough as each piece of code and app route had to work and link to the relevant part of the website. 
* Being very conscious of how easy it was for these elements to fail. I **tested constantly** to make sure they performed how I wanted them to, each time I added or made a change to my code.
* The testing involved myself and that of my friends and family.

### Manual testing of all elements on pages

#### Navigation bar
* Click on **logo** to check it links to home page.
* Click on **all links** to check they link to relevant page.
* Hover over **all links** to check they change colour.
* Change screen size to verify that it is **fully responsive** and switches from **in-line menu to hamburger menu** on mobile size.
* Change screen size to small verify that the **hamburger menu drops down and links work.**
* Repeat checks on mobile and tablet to verify they are correct.

#### Home page
* Change screen size to verify that it is **fully responsive** and the text and image work on all device sizes.
* Click on **about me** button to check it links to about page.
* Hover over **about me** link to check it changes colour.
* Repeat checks on mobile and tablet to verify they are correct.

#### About page
* Change screen size to verify that it is **fully responsive** and the panels work on all device sizes.
* Check that the skills panel is **showing correct data** (skill name and progress bar percentage) from MongoDB database.
* In the footer click on each **social media button** to check it takes you to the relevant website in a new window.
* In the footer click on **CV** to check it opens the downloadable pdf.
* Repeat checks on mobile and tablet to verify they are correct.

#### Projects page
* Change screen size to verify that it is **fully responsive** and the panels work on all device sizes.
* Click on each view button to check it opens **relevant modal.**
* Change screen size to verify that each modal is **fully responsive** and works on all device sizes.
* Click on each modal's **x and close buttons** to check they close the modal.
* Click on **view website buttons on Wildbunch Florist** and check it opens relevant website in new window.
* Click on **view website buttons on Handpicked Brighton** and check it opens relevant website in new window.
* Click on **view website buttons on Little Monsters** and check it is a link. This is a fake website so has no live website.
* Click on **view website buttons on Hummingbird Family Services** and check it is a link. This is a fake website so has no live website.
* Hover over **links** on main page and modals to check they change colour.
* In the footer click on each **social media button** to check it takes you to the relevant website in a new window.
* In the footer click on **CV** to check it opens the downloadable pdf.
* Repeat checks on mobile and tablet to verify they are correct.

#### Contact page
* Change screen size to verify that it is **fully responsive** and the panels work on all device sizes.
* **Write** into each form field to make sure it works.
* The send button isn't wire up, so will not send anything.
* Hover over **send button** to check it changes colour.
* In the footer click on each **social media button** to check it takes you to the relevant website in a new window.
* In the footer click on **CV** to check it opens the downloadable pdf.
* Repeat checks on mobile and tablet to verify they are correct.

#### Admin page
* Change screen size to verify that it is **fully responsive** and the panels work on all device sizes.
* Check **data from MongoDB database** is correct and displays correctly.
* Click on **edit buttons** to check they open the edit page with correct data.
* Click on **delete buttons** to check they open the warning modal.
* Click on **x and close** on modal to check they close the modal and go back to admin page.
* Click on **yes, I'm sure button** on modal to check it removes correct data from MongoDB database.
* Click on **no, keep it button** on modal to check it closes the modal and goes back to admin page leaving data in place.
* Click on **add new skill button** to check it opens add skill page.
* Hover over **buttons** to check they change colour.
* In the footer click on each **social media button** to check it takes you to the relevant website in a new window.
* In the footer click on **CV** to check it opens the downloadable pdf.
* Repeat checks on mobile and tablet to verify they are correct.

#### Edit skills page
* Change screen size to verify that it is **fully responsive** and the panels work on all device sizes.
* Check form is **displaying correct data** to be edited.
* **Edit data** in form and click the save changes button to check it closes the page and returns to admin page, and that the admin page displays edited data.
* Click on **back to skills button** to check it returns you to the admin page without changing data.
* Hover over **buttons** to check they change colour.
* In the footer click on each **social media button** to check it takes you to the relevant website in a new window.
* In the footer click on **CV** to check it opens the downloadable pdf.
* Repeat checks on mobile and tablet to verify they are correct.

#### Add skills page
* Change screen size to verify that it is **fully responsive** and the panels work on all device sizes.
* **Enter data** in form and click the add skill button to check it closes the page and returns to admin page, and that the admin page displays added data.
* Hover over **buttons** to check they change colour.
* Click on **back to skills button** to check it returns you to the admin page without changing data.
* In the footer click on each **social media button** to check it takes you to the relevant website in a new window.
* In the footer click on **CV** to check it opens the downloadable pdf.
* Repeat checks on mobile and tablet to verify they are correct.

#### Heroku
* Check Heroku is being **updated** and the changes are being deployed each time it is **pushed to GitHub.**
* Open app on Heroku and test all pages, links and forms work correctly.
* Repeat checks on mobile and tablet to verify they are correct.

### Planning
The planning for this project involved using my **wireframes** to sketch a plan of which pages, buttons and forms needed to link to the database and to other parts. 

### Stories

* After deciding on a palette of colours for the website. It was felt I had **too many** and need to edit them down. I played around using a **Hex Colour Picker** website to find the colours that worked together as a family. Enough difference that they had their own identity, but similar enough to connect. I chose **four basic colours** and used a dark version and a light version.

* On my mock ups and during most of the build, I had my **social links** as just letters **'Li'** (LinkedIn), **'Tw'** (Twitter) etc. I felt they added a very stylish 'designer' look to the pages. But after several testers found them confusing and didn't immediately get what they were, I changed them to **FontAwesome** icons to make it clearer. I liked my letters, but the world wasn't ready for them.

* From my wireframes right up until near the end I had a **button to take you to the admin page.** First it was in the **navigation bar**, but I felt I didn't want users to click on it, so I put it small on the contact page at the bottom in the **footer**. I was still a bit worried about it being still quite public, so my mentor suggested **not having the button at all.** Instead the admin page is accessed by adding **'/admin' to the url.** This makes it more **secure.** It also allowed me to add the footer to each page.

### Overall

#### Responsiveness
* I wanted my website to be fully responsive and work and look perfect on all devices. 
* I used **Bootstrap** to build the basic grid of my website. This involved selection the best breakpoints to find the perfect balance on all devices. Testing the changes using the **Chrome Developer Tools** tools to get it right.
* The result was a very balanced and dynamic website that looked slick and stylish when adapting to different devices.

#### Design
* The design of the website needed to be clean, stylish and sophisticated. I had most of the elements and feel of the pages all worked out at the **wireframe** stage. Using the simple clean sans serif font [Montserrat](https://fonts.google.com/specimen/Montserrat) in two weights, (300 and 500), and **opening up the letter spacing**, allowed me to create that feel. The **muted colours** all work together as a family to hold it together. 
* Using **CSS** styling allowed to create styles for images, words and panels that could be **replicated** across the website. This also meant that it was easy to **change multiple elements quickly and simply.**
* The result is a website that has an elegant, upmarket design to allow users to see my creative side.

#### Projects page
* The projects page needed a way to showcase my work to the user. Originally I simply had each project in a panel with an image of the homepage on a laptop with some text underneath describing the website and a link to the live version. However. it was felt that this wasn't very dynamic. 
* To solve this, I created a **large modal** that pops up when the view button is clicked.
* This was a better solution as it allowed me to create a graphic showing the home page on laptop, tablet and mobile. It gave me more room to write the description and add the link to the live website.
* It is also better for **user experience** as it adds more interest and drama when it pops up. It also leaves the projects page cleaner and neater.

#### Delete button
* When I added the **delete** button to the admin page, it originally simply deleted any skill when clicked.
* I felt that this was a very dangerous thing to do, as there was no going back once it was clicked.
* My solution was to wire up a modal that pops up when the **delete button** is clicked saying **'are you sure you want to delete this skill? once you press this button it's gone for good!'** There are then two buttons. **'yes. i'm sure'** which is actually the **'real'** delete button that is wired up to remove the data. The other button **'no. keep it'** takes the user safely back to the **admin** page.
* This solution means that the data is better protected from being deleted by accident, so makes it **more secure.**

### Bugs

#### Hamburger menu on mobile
* I am using the **Bootstrap hamburger menu** on the mobile version of my website. This has been working will and I was happy with how it looked.
* Towards the end of the build, I updated my jQuery script from **3.4.1** to **3.5.0** as it was discovered to be out of date. Just after while carrying out some testing on my phone, I discovered that my hamburger menu was no longer firing. 
* After looking for a solution and coming up blank, it was looked into by a **tutor** who did some investigating and found that the update was clashing with the navigation bar.
* I therefore reverted back to **3.4.1** and the hamburger menu worked again.

#### Template Inheritance
* When first trying to work with Template Inheritance I built a **base.html** page with a code block to hold the html from the other pages. But when I ran my app.py file, I was getting an error telling that it couldn't find my template. 
* On investigation I discovered that my folder structure was wrong, so none of the files could be found.
* I restructured by folders and put the files in their right pages, and was able to get the html pages to load inside the block code.

#### Heroku app
* Having linked my Heroku app to update every time I pushed to my repository. I was happy that all would be fine. It was deploying to Heroku and looked good. 
* However, my app just kept giving me an error when I tried to launch it.
* It was discovered that the problem was that I had set up an **env.py** file, that was being hidden in a **.gitignore file** to keep my password safe. This information wasn't being uploaded to Heroku, so it couldn't work.
* I therefore had to set the value for the this in the **Config Vars** of Heroku. Once there, Heroku could read it and the app worked.

#### Footer
* Viewed on a large screen and manually changing the screen size the footer appeared to work well and stay at the bottom of the page.
* However, when checking the page via inspect, I found it didn't go to the bottom of the screen on a tablet when there wasn't enough content on the page to push it down.
* I fixed this problem using flexbox in my css to make it always go to the bottom of the page.  

---

## Deployment

**My site is deployed on Heroku and GitHub.**

I've been using **GitPod**. These are the steps that I used in a **Unique Linux environment**. Please make sure you read your documentation to comply with your operating system.

1. First log onto **Heroku**.
2. In the **App Name form**, create a unique app name.
3. In the **Choose a Region** drop-down, choose **Europe** as that's our region and delivery will be quicker.
4. Click on **Create App**.
5. Next, log in to Heroku in the terminal with ```heroku login```. You will need to enter you email and password. This allows the connection from your project to Heroku and allows us to push changes to Heroku using git.
6. Create a new Git repository with the command, ```git init```.
7. Do a ```git add .``` to add the files and ```git commit -m "Intial commit"``` to commit those files.
8. We need now to associate Heroku as our remote master branch. Back on Heroku you will find the command ```heroku git:remote -a (name of your app)```, in the Deploy using Heroku Git section. Paste this into the terminal to set it up.
9. Create a **requirements.txt** file which will contain a list of all the applications required for Heroku to run the application.To do this type ```pip3 freeze --local > requirements.txt``` in the terminal. This will create a txt file with the list in.
10. Add this file, commit it and push it to Heroku with ```git push heroku master```.
11. You now have to create a **Procfile** which will tell Heroku which file to call to get the application running. To do this, in the terminal write ```echo web: python app.py > Procfile```. Add this to GitHub, and commit. Then ```git push heroku master``` to save it to Heroku.
12. Next, we want to get our application running on Heroku. In the terminal, type ```heroku ps:scale web=1```. 
13. On Heroku, go to **'settings'**, and click on the **'Reveal Config Vars'** button. 
14. In here we need to supply a our IP address and our port. The first key is **'IP'** and it's value is **'0.0.0.0'**. The second key is **'PORT'** and it's value is **'5000'**. If you have hidden sensitive data such as your **MONGO_URI** in your **env.py** file, you must also put in the key of **MONGO_URI**, and the value of the **password code** from the env.py file. This is so Heroku can see it.
15. Click on the button **'Open app'** and it will start the app and show your page.
16. To make sure you push to Heroku automatically each time you push to GitHub, you can set it up in Heroku.
17. First click on **Deploy**, and click on **Deployment Method**. Then click on the **GitHub** selection.
18. Below that in click on **Connect to GitHub**, and enter your repository's name, and search for it. **Connect**.
19. Click on **Enable Automatic Deploys**, underneath that.
20. Finally, deploy it by clicking the **Deploy Branch** button.
21. Now every time you push to GitHub, it will automatically push it through to Heroku too.

### Deploy locally

**In order to deploy this project locally you must do a number of things.**

1. First in the GitHub repository, click on the **Clone or download** button on the repository.
2. Click on the **Open in Desktop** button.
3. Click the **Choose** button and navigate to a local path where you want to clone the repository.
4. Click the **Clone** button.
5. You will need to make sure you have **Python 3.7** installed.
6. You will need to type ```pip3 install requirements.txt``` in your terminal.
7. Create an ```env.py``` file.
8. Inside this file you will need to provide some information for this app to run. ```import os```
```os.environ["MONGO_URI"] = 'mongodb+srv://Name:<password>@collection-2pvma.mongodb.net/test?retryWrites=true&w=majority'```

---

## Closing notes

* I've really enjoyed building this website has taught me lots of interesting new ways to do it. I really like using the **template inheritance** where you build a skeleton document, then **block codes** to allow you to place elements on pages. This seems to me to be a brilliant way to simplify and reduce the amount to code that has to be written. It also would prevent errors where you might change one page, but forget another.
* I've also found the **database** element of the challenge to be very interesting and fun. I like how you can control the data on one page the website and it updates it on another.  

---

## Credits

### Thanks

My mentor [Simen Daehlin](https://dehlin.dev/) for all the advice and pointers. And for always pushing me to go further.

All the **tutors** that helped me along the way on the **Tutor Support**. 

### Images

Bird image was sourced from the [iStock](https://www.istockphoto.com/gb) image library, but adapted by me to hold the </> card in it's mouth. 

### Text

All text written by me.

### Disclaimer

This website is a Milestone Project for the **Full Stack Web Development** course at [Code Institute](https://codeinstitute.net/)

---

## Acknowledgements

### Anna Gilhespy website
I used Anna Gilhespy's **Bootstrap** website [Bootstrap Essentials](https://ajgreaves.github.io/bootstrap-grid-demo/) to help me work out the structure of the grid.


### Corey Schafer
I watched Corey Schafer's YouTube tutorial [Python Flask Tutorial: Full-Featured Web App Part 2 - Templates](https://www.youtube.com/watch?v=QnDWIZuWYW0) to help me understand **Template Inheritance** better.

### Kevin Powell
I watched Kevin Powell's YouTube tutorial [Easy sticky footer - stop a footer from floating up a short page!](https://www.youtube.com/watch?v=yc2olxLgKLk) to help me understand **Flexbox** better to fix my footer to the bottom of the pages.


