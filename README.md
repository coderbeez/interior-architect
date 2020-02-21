[![Build Status](https://travis-ci.com/coderbeez/interior-architect.svg?branch=master)](https://travis-ci.com/coderbeez/interior-architect)

MILESTONE 4
https://github.com/AndrewIngram/django-extra-views/

Forms
<!--WHERE: Corey Schafer https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6-->

Stripe
Do not rely on the redirect to the success_url alone for fulfilling purchases as:

Malicious users could directly access the success_url without paying and gain access to your goods or services.
Customers may not always reach the success_url after a successful payment. It is possible they close their browser tab before the redirect occurs.

Email receipt sent to customers by stripe with COS colors and icon
https://www.vectorstock.com/royalty-free-vector/house-construction-architect-logo-icon-vector-23672011


Bugs
Email https://support.google.com/mail/thread/5621336?hl=en
Set Less secure apps to on in google account
Price in success - decimal
Can't use build uri for stripe success url

Email cos web link including safe links - making url look ugly
Why Outlook Adding “Safelinks.Protection.Outlook.Com” to All URLs
https://www.askvg.com/why-outlook-adding-safelinks-protection-outlook-com-to-all-urls-in-your-emails-and-how-to-disable-it/

Trying to implement get or 404 throws error
'Manager' object has no attribute 'get_object_or_404'



AWS django storages
https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html

Brad Traversy Real Estate https://www.udemy.com/course/python-django-dev-to-deployment/

https://pypi.org/project/django-heroku/

Email videos
https://www.youtube.com/watch?v=51mmqf5a0Ss
https://startcodingnow.com/making-your-own-email-templates-in-django/

<div align="center">
<img src="https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/header.JPG" alt="Site header">
</div>

# [COLETTE O'SULLIVAN](https://coletteosullivan.com)

*A portfolio website for an interior architect and designer, developed for Code Institute's full stack milestone project.*

# UX

This portfolio website was developed to provide a platform for the client, an interior architect and designer, to showcase her work. The site content, including instagram posts, blogs, and detailed projects, is frequently updated so the client needs a site that is both flexible and easy to update.

## User Stories

User stories for potential visitors to the website include:

### Home Owner - Extension

After talking about it for years, I'll decided to build an extension to my house. A friend recommended Colette's site. I go straight to the Potfolio page and select a project similar to mine. Having read the story behind the design and build I purchase one of the drawings. I'm taken to a Stripe payment page, I prefer that as it feels more secure. Once complete I see a summary of my order and take note of my reference number. By email I receive both a receipt from Stripe and the drawing pdf from Colette. After mulling it over for a few days, I go back to the site amd fill out the contact form leaving a description of my dream extension. Colette responds with useful advice on planning and designing to maximise light.

### Home Owner - New Build

Having been gifted a site by my Uncle, I've decided to build a holiday home. I would like the house to be as sustainable as possible, but my funds are limited. Having seen an instagram post by Colette on budget builds, I check out her site. I start with browsing blogs on sustainability and budgeting. I visit some of the portfolio projects. I fill out the contact form outlining my requirements. I'm so impressed by the reply from Colette that we agree to meet to discuss further. She's now drawing up my dream holiday home.

### Interior Design Student

I'm currently enrolled in an interior design course but struggling with a colour rendering project. A fellow student recommended Colette's site. I visit the blog page and find two rendering blogs. I leave a like and a comment on both blogs. I'm sorted - they were just what I needed. I click on instagram to start following Colette as she often posts when new blogs are uploaded. I know I'll be revisiting the site and recommending it to fellow students.

### Architecture Firm

My firm is looking to hire an architectural technician. I've received an application from Colette and she's provided a link to her site. I review the about section outlining her skills, education and employment. She noted some portfolio projects in her application that have free drawing downloads. From these I can review her design and technical skills. Happy with her skills and breath of experience, I call her for interview.

### Client

The client receives an email flag whenever a new comment, contact or purchase is made. She opens the site and clicks admin at the bottom of the home page. On login she can easily see and respond to outstanding comments and contacts. She simply clicks exclue on any comment or contact she would like to close. To update the site or fulfill an order, she enters admin at the end of the url and logs into the Django admin interface. Styled and customised to look similar to the main site, the interface feels bespoke for the client.

## Design

Simplicity is key to COLETTE O'SULLIVAN with the look and flow of the site designed for ease of use.

### Navigation

As a portfolio site, the client's name is centred and prominent above the navbar.
The main site is divided into four distinct sections, **about**, **blog**, **portfolio** and **contact** highlighted by a pared back navbar.

Navbar sticky.

### Colours & Fonts

A minimal colour scheme of black, white and stone, provides a neutral background for the client's colourful content. The Google font *Montserrat*, is used in uppercase for all headings.  While another Google font *Ibarra Real Nova* is used, in both regular and italics styles, for all remaining text. Italics and hover colour changes are used to identify link text. Messages follow a traffic light green, orange and red colour scheme to inform, alert or warn users.

### Preparation

Microsoft PowerPoint was used to compile initial [planning documents](https://github.com/coderbeez/COLETTE O'SULLIVAN/blob/master/wireframes/wireframes.pdf) including Balsamiq wireframes and an app diagram. During development, the original design was tweaked based on client feedback and requirements.

# Apps

Using Django 2.2.10, the web site is built with 7 apps: home, cv, blog, portfoiio, contact, cart and users.

## Home App

![Home Page Image](https://github.com/coderbeez/COLETTE O'SULLIVAN/blob/master/wireframes/images/home.png)

| **TYPE** | **NAME** | **DESCRIPTION** |
| --- | --- | --- |
| **View** | index | Import portfolio and blog models to display the top 3 most liked blogs and 3 selected projects. |
| **Template** | index | Landing and teaser page showing client intro, instagram posts, portfolio & blog samples. Provides access to admin pages for client. |
| **Template** | include-intro | Used to position client photo and introductory text depepening on device size. |

## CV App

<img align="right" height="500" src="https://github.com/coderbeez/COLETTE O'SULLIVAN/blob/master/wireframes/images/register.png" alt="COLETTE O'SULLIVAN register page">

| **TYPE** | **NAME** | **DESCRIPTION** |
| --- | --- | --- |
| **Model** | Role | N/A |
| **Model** | Point | N/A |
| **Model** | Example | N/A |
| **Model** | Skill | N/A |
| **View** | About | - |
| **Template** | About | - |

## Blog App

<img align="right" height="500" src="https://github.com/coderbeez/COLETTE O'SULLIVAN/blob/master/wireframes/images/login.png" alt="COLETTE O'SULLIVAN login page">

| **TYPE** | **NAME** | **DESCRIPTION** |
| --- | --- | --- |
| **Model** | Role | N/A |
| **Model** | Point | N/A |
| **Model** | Example | N/A |
| **Model** | Skill | N/A |
| **View** | About | - |
| **Template** | About | - |

## Portfolio App

<div align="center">
<img src="https://github.com/coderbeez/COLETTE O'SULLIVAN/blob/master/wireframes/images/notes.gif" alt="COLETTE O'SULLIVAN notes page">
</div>

| **TYPE** | **NAME** | **DESCRIPTION** |
| --- | --- | --- |
| **Model** | Role | N/A |
| **Model** | Point | N/A |
| **Model** | Example | N/A |
| **Model** | Skill | N/A |
| **View** | About | - |
| **Template** | About | - |

## Contact App

<img align="right" height="500" src="https://github.com/coderbeez/COLETTE O'SULLIVAN/blob/master/wireframes/images/addnote.png" alt="COLETTE O'SULLIVAN add note page">

| **TYPE** | **NAME** | **DESCRIPTION** |
| --- | --- | --- |
| **Model** | Role | N/A |
| **Model** | Point | N/A |
| **Model** | Example | N/A |
| **Model** | Skill | N/A |
| **View** | About | - |
| **Template** | About | - |
  
## Cart App

<img align="right" height="500" src="https://github.com/coderbeez/COLETTE O'SULLIVAN/blob/master/wireframes/images/editnote.png" alt="COLETTE O'SULLIVAN edit note page">

| **TYPE** | **NAME** | **DESCRIPTION** |
| --- | --- | --- |
| **Model** | Role | N/A |
| **Model** | Point | N/A |
| **Model** | Example | N/A |
| **Model** | Skill | N/A |
| **View** | About | - |
| **Template** | About | - |

## User App

<div align="center">
<img src="https://github.com/coderbeez/COLETTE O'SULLIVAN/blob/master/wireframes/images/links.gif" alt="COLETTE O'SULLIVAN links page">
</div>

| **TYPE** | **NAME** | **DESCRIPTION** |
| --- | --- | --- |
| **Model** | Role | N/A |
| **Model** | Point | N/A |
| **Model** | Example | N/A |
| **Model** | Skill | N/A |
| **View** | About | - |
| **Template** | About | - |

## Future Features

**Automated Fulfillment** Look up Stripe site???

**Cart Analysis** Statistics

**Search Facility** Statistics

**Email??** Email's from coletteosullivan.com

# Technologies & Programmes Used

## Languages

- [HTML](https://www.w3.org/)
- [CSS](https://www.w3.org/)
- [JavaScript](http://www.ecma-international.org/)
- [Python](https://www.python.org/)

## Development Tools

- [Visual Studio Code](https://code.visualstudio.com/) IDE used.
- [Git](https://git-scm.com/) Used to track changes during development.
- [GitHub](https://github.com/) Used to host the version control system and website content before deployment to Heroku.

## Hosting Platforms & Database

- [Heroku](https://www.heroku.com/) Cloud based hosting service.
- [Go Daddy](???) Domain hosting service.
- [SQLite](???) Default Django database used for developement.
- [PostgreSQL](???) Database used for production on deployment to Heroku.

## Frontend Resources

- [Google Fonts](https://fonts.google.com/) Used for all fonts.
- [Font Awesome](https://fontawesome.com/) Used for all icons.
- [Bootstrap](https://getbootstrap.com/) Used for responsive layout and styling.
- [jQuery](https://jquery.com/) Used for navbar, carousel, accordion, data circles & stripe functionality.
- [Juicer](https://www.juicer.io/) Used to link and display client's instagram feed.

## Backend Resources

- [pip](https://pypi.org/project/pip/) Used to install Python modules.
- [Django](???) Used ???.
- [Crispy Forms](???) Used to format html forms.
- [Django Math Filters](https://pypi.org/project/django-mathfilters/) Used for hashing user passwords.
- [Stripe](???) Used for managing online payment.

## Design Tools

- [Balsamiq](https://balsamiq.com/) Used to develop wireframes for the website.
- [Microsoft PowerPoint](https://office.live.com/start/PowerPoint.aspx) Used to develop the initial website proposal.
- [Affinity Designer](https://affinity.serif.com/en-gb/) Used to edit images and identify hex colours for fonts and backgrounds.
- [Microsoft Screen Recorder](https://uk.pcmag.com/operating-systems/86044/how-to-capture-video-clips-in-windows-10) Used to record README videos.
- [EZgif](https://ezgif.com/) Used to create README gifs.
- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) Used to create README device images.

# Testing

Testing detailed in [TESTING.md](https://github.com/interiorarchitect/COLETTE O'SULLIVAN/blob/master/TESTING.md).

# Deployment

The website was developed in Visual Studio Code using a virtual environment and deployed to Heroku via GitHub.

The following instructions to clone and deploy assume the user has:

- IDE
- Python 3
- Pip
- Virtual Environment
- GitHub Account
- Heroku Account

## Clone in GitHub

The following instructions were taken from [GitHib Help]( https://help.github.com/en/articles/cloning-a-repository).

1. Open the [COLETTE O'SULLIVAN](https://github.com/coderbeez/COLETTE O'SULLIVAN) repository.
2. Click the **clone or download** button.
3. In the **clone with HTTPs** pop-up, click the **copy icon**.
4. Open **git bash**.
5. Change the current working directory to where you want the cloned directory to be made.
6. Type **git clone** and paste the URL copied earlier.
7. Press **enter**.

## Create MongoDB Atlas Database

1. On the [MongoDB](https://cloud.mongodb.com/user#/atlas/login) website log into your Atlas account.
2. Under **cluster/ collections** click **create database** and enter a **database name** and **collection name**.
3. Click **create collection** to add more collections as per the database design above.
4. Under **cluster/ overview** click **connect**.
5. Click **connect your application**.
6. Select **Python** as the **driver** and select the **version**.
7. Copy the connection string `mongodb+srv://root:<password>@mysecondcluster-xkuqo.azure.mongodb.net/test?retryWrites=true&w=majority`.

## IDE Development Setup

1. Add the `MONGO_URI` to your environment file for local deployment. Replace `<password>` with your **password** and `test` with your **database name**.
2. Add a `SECRET_KEY` to your environment file.
3. Use `pip install -r requirements.txt` to install requirements.

## Deploy to Heroku
Create Procfile '''web: gunicorn <name of directory hold setting.py file>.wsgi'''
Create Requirements.txt file
1. On the [Heroku](https://id.heroku.com/login) website log into your account.
2. Click **new** and **create new app**.
3. Give your app a **name** (it must be unique), select a **region** and click **create app**.
4. Under **resources** add on Postgres, hobby free
5. Reveal ID - paste that into env file
6. Under **settings/ config vars** click **reveal vars**.
7. add key values for your env variables
8. heroku login - when prompted click any key to open browser and log into heroku account
9. heroku git:remote -a interiorarchitect
10. git subtree push --prefix iaproject heroku master to push code to Heroku
11. run migrations
12. create super user
13. site/admin add blogs, projects, and roles
14. debug mode off - collectstatic??
15. add address to allowed hosts settings.py
16. add address to aws s3.

# Credits

## Content

- Site concept and design by website developer.
- Language topics reflect Code Institute’s Diploma in Full Stack Web Development.
- Links collected by site developer during studies and from Code Institute's Diploma Slack channel.
- Quotes from [CodeWisdom](https://twitter.com/CodeWisdom), [DZone - Programming Quores](https://dzone.com/articles/best-programming-jokes-amp-quotes), [DZone - Software Developer Quotes](https://dzone.com/articles/more-inspirational-quotes-for-software-developers), [GoodReads](https://www.goodreads.com/quotes/tag/programming?page=1), [JournalDev](https://www.journaldev.com/240/my-25-favorite-programming-quotes-that-are-funny-too).

## Media

- Pencil image by Yoann Siloine from [Unsplash](https://unsplash.com/photos/dyaxQ-aoGWY).
- Spotify image adapted from [Spotify](https://www.spotify.com/ie/).

## Code

### README

- Aligning images from [Stack Overflow](https://stackoverflow.com/questions/12090472/github-readme-md-center-image).

### HTML Code

- Remove Bootstrap card header border radius [Stack Overflow](https://stackoverflow.com/questions/46316719/how-to-make-card-header-no-border-radius-in-bootstrap-4).

### CSS Code

- Timeline [Bootsnipp](https://bootsnipp.com/snippets/xrKXW).

### JavaScript Code

- /On page load event from [Stack Overflow](https://stackoverflow.com/questions/42541274/jquery-on-page-load-event-not-working).

### Python Code

#### Database

- /[Maximilian Schwarzmüller - Udemy MongoDB The Complete Developer's Guide](https://www.udemy.com/course/mongodb-the-complete-developers-guide/learn/lecture/11850844?start=300#overview).

#### Forms

- Send POST data from inside for loop [Stack Overflow](https://stackoverflow.com/questions/38046905/sending-post-data-from-inside-a-django-template-for-loop).

#### Users

- Python Django Tutorial Part 6 - User Registration [Corey Schafer](https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6).

#### Pagination

- [Django Documentation](https://docs.djangoproject.com/en/3.0/topics/pagination/).

#### Messages

- /[Flask Message Flashing Documentation](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/).

#### Templates

- Multiply in template tag [Stack Overflow](https://stackoverflow.com/questions/6285327/how-to-do-math-in-a-django-template).
- Foreign key in template tag [Stack Overflow](https://stackoverflow.com/questions/12281965/django-foreign-key-relation-in-template).

#### Shop Cart

- Django Tutorial for Beginners Part 22, Cart App [Coding Point](https://www.youtube.com/watch?v=20HCDEwEdeo&list=PLPp4GCMxKSjCM9AvhmF9OHyyaJsN8rsZK&index=23&t=0s).

#### Other

- /Before request decorator [Pythonise](https://pythonise.com/series/learning-flask/python-before-after-request).

## Acknowledgements

- Many thanks to my client for her direction and infectious enthusiasum! To my mentor Ali Ashik, and ***all*** on Code Institute's Slack channel.
