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

https://pypi.org/project/django-mathfilters/

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

*A portfolio website for an interior architect and designer, developed for Code Institute's full stack framework milestone project.*

# UX

 is a website developed to assist coding students studying HTML, CSS, JavaScript and Python languages for Code Institute’s Diploma in Full Stack Web Development. The site allows students to save notes and share links for each language.

1. **About** Students can register to host their own language notes using familiar topic headings with a full range of CRUD operations. Registration and log in are required for Notes. To facilitate assessment a test user has been setup with email tester@gmail.com, password testUser, and notes created for JavaScript and Python.

2. **Blog** Language links are again grouped under familiar topic headings and categorised by type, i.e. instruct, practice, resource and other. Students can create a new link, add a star rating or report a problem with an existing link. No registration or log in is required for Links.

3. **Portfolio** Inspiration and motivation is provided by coding quotes, suggested language links, daily award site links and a Spotify playlist for those times when Stack Overflow just isn’t delivering.

4. **Contact** Inspiration and motivation is provided by coding quotes, suggested language links, daily award site links and a Spotify playlist for those times when Stack Overflow just isn’t delivering.

5. **Admin** Inspiration and motivation is provided by coding quotes, suggested language links, daily award site links and a Spotify playlist for those times when Stack Overflow just isn’t delivering.

## User Stories

User stories for potential visitors to the website include:

### Home Owner

I’m struggling with the JavaScript automated testing topic and looking for some links for further study. I visit the COLETTE O'SULLIVAN site, select JavaScript from the links dropdown. I’m presented with a familiar list of JavaScript topics – I select Jasmine. A list of link types opens – I select instruct. A list of link names with star ratings and i buttons opens. After reading the description under additional information, I click a YouTube link. Having watched the video I go back and add my rating of 4 stars. I’m registered on the site already but I haven’t had to log in to use links.

### New Build - Architecture

I’ve come across a great YouTube video for PyMongo which I’d like to share with my fellow students. On Slack, links tend to get lost unless pinned, so I open COLETTE O'SULLIVAN and select Python from the links dropdown. I click add new. I enter the details, selecting MongoDB for topic, instruct for type and give it a 5 star rating. I could add a description but its optional, so I skip this time. It’s quick and easy – I don’t need to register or log in to add a link.  I could have done a search for the word PyMongo to check if the link already existed but COLETTE O'SULLIVAN will flag it and simply add my star rating if another student has already added this url.

### Interior Design Student

As study needs to fit around home and work life, notes must be accessible from multiple devices - my personal laptop, work desktop and mobile. Having come across an article on Flask Bcrypt during this morning's commute, I want to review and jot down some notes. I open up COLETTE O'SULLIVAN. It's already in dark mode as it's remembered my preference. I select Python from the notes dropdown. I'm asked to log in using email and password. My Python notes page opens. When I use the word search facility to see if I've saved Bcrypt notes already, it tells me there are no results. I click add new to create a new note selecting Flask for the topic, and entering a note name and some contents. With a few minutes to spare, I return to the home page and check out today's Awwwards site under distraction for inspiration for my next milestone.

### Architecture Company

When my brain is fried, motivation has dipped or its simply time for a coffee, I head to COLETTE O'SULLIVAN’s distraction sidebar. I always read the randomly selected coding quote. I check out today’s site of the day from the Awwwards link. As I’m on the JavaScript milestone, I visit the sample link for that language. I click the Spotify link to start the playlist when I return to coding.

## Design

Simplicity is key to COLETTE O'SULLIVAN with the look and flow of the site designed for ease of use.

### Navigation

The key driver of site design was navigation, allowing the user to find the desired location with as few clicks as possible.  The site was divided into four distinct sections, **about**, **blog**, **portfolio** and **contact** highlighted by the pared back navbar. 

As links are not associated with accounts, users selecting a links language are immediately routed to the read links page for their chosen language. From here users can access the add link page, or use the bespoke accordion or word search to find and edit existing links. With four levels, the links accordion allows for efficient filtering. Again focusing on efficiency, the word search searches all four levels simultaneously.

Users that select a notes language are routed to the login page, if not already logged in, before being routed to the read notes page for their chosen language.  Following a consistent design, users can again access the add note page, or use the accordion and word search to find and edit existing notes. Users remain logged in until they select logout or end their session. New users can choose register directly from the notes dropdown or link from the login page. After registering, users are automatically logged in. The notes dropdown register option changes to logout once a user registers or logs in, following the mantra of only showing the user what they need, when they need it.

### Colours & Fonts

Following on from simplified navigation, COLETTE O'SULLIVAN has been designed with minimal graphics, fonts and colours. A simple pencil image, to reflect note taking, is used on the home page and repeated on the playlist. The main font *Cabin Condensed*, a very readable condensed font, was chosen to better display lists on mobile devices. In either normal or dark mode, the core colour scheme consists of a background, text and link colour. The stone and charcoal colours, taken from the pencil image, switch between background and text, depending on mode. The link colours, identifying everything clickable, were chosen for contrast and accessibility. Flashed messages follow a green/red approach to notify or alert users. Given dark mode is often discussed on the Code Institute's Diploma Slack channel, it was included as an option for users. The mode selected is saved in local storage so user preference is remembered on return visits.

<div align="center">
<img  src="https://github.com/coderbeez/COLETTE O'SULLIVAN/blob/master/wireframes/images/colours.png" alt="COLETTE O'SULLIVAN colours">
</div>

### Preparation

Microsoft PowerPoint was used to compile initial [planning documents](https://github.com/coderbeez/COLETTE O'SULLIVAN/blob/master/wireframes/wireframes.pdf) including Balsamiq wireframes, database collections and an app diagram. During development, the original design was tweaked based on feedback from the client.

# Apps

Using Flask and Jinja, a base page is used to render COLETTE O'SULLIVAN's 8 site pages as follows:

## Blog

![Home Page Image](https://github.com/coderbeez/COLETTE O'SULLIVAN/blob/master/wireframes/images/home.png)

- A pared back navbar with a home button and two simple dropdowns, notes and links, highlights the two main site sections. Both dropdowns allow users to select a language passing it onto the relevant routes. The notes dropdown has an additional register option if the user is not logged in and logout if logged in. Apart from font size, the navbar remains the same on different devices.

- The text over a simple pencil image sets out the site's name, function (save notes, share links) and languages (HTML, CSS, JavaScript and Python).

## Portfolio

<img align="right" height="500" src="https://github.com/coderbeez/COLETTE O'SULLIVAN/blob/master/wireframes/images/register.png" alt="COLETTE O'SULLIVAN register page">

- New users access the Register Page either by selecting register from the notes dropdown, or by clicking the register link on the Login Page.

- In the forms.py file, WTForms is used to define the Register Form's name, email, password, confirm password and submit fields.

## Cart

<img align="right" height="500" src="https://github.com/coderbeez/COLETTE O'SULLIVAN/blob/master/wireframes/images/login.png" alt="COLETTE O'SULLIVAN login page">

- On selecting a language from the notes dropdown, users not already logged in, are routed to the Login Page using `login_manager.login_view = "login"`.

- A Flask-Login `@loginrequired` decorator on read, add, edit and delete note routes ensures only logged in users access notes.

## CV

<div align="center">
<img src="https://github.com/coderbeez/COLETTE O'SULLIVAN/blob/master/wireframes/images/notes.gif" alt="COLETTE O'SULLIVAN notes page">
</div>

- Users access the Notes Page by selecting a language from the notes dropdown. If a user is logged in they go directly to their language Notes Page. A Flask-Login `@loginrequired` decorator ensures users not currently logged in, are first routed to the Login Page before being redirected to their relevant language Notes Page.

- Within the language Notes Page, notes are grouped by topic, sorted by name, and presented in a bespoke accordion.

## Contact

<img align="right" height="500" src="https://github.com/coderbeez/COLETTE O'SULLIVAN/blob/master/wireframes/images/addnote.png" alt="COLETTE O'SULLIVAN add note page">

- A Flask-Login `@login_required` decorator ensures access to this route is limited to logged in users.

- Users access the Add Note Page from a link on the language Notes Page, passing the language argument from Notes to Add Notes.
  
## Cart

<img align="right" height="500" src="https://github.com/coderbeez/COLETTE O'SULLIVAN/blob/master/wireframes/images/editnote.png" alt="COLETTE O'SULLIVAN edit note page">

- A Flask-Login `@login_required` decorator ensures access to this route is limited to logged in users.

- Users access the Edit Note Page from a link on level three of the language Notes Page accordion.

## User

<div align="center">
<img src="https://github.com/coderbeez/COLETTE O'SULLIVAN/blob/master/wireframes/images/links.gif" alt="COLETTE O'SULLIVAN links page">
</div>

- Users access the Links Page by selecting a language from the links dropdown. Links are not associated with a user and no log in is required to access.

- Within the language Links Page, links are grouped by topic and type, sorted by name, and presented in a bespoke accordion.

## Add Link Page

<img align="right" height="600" src="https://github.com/coderbeez/COLETTE O'SULLIVAN/blob/master/wireframes/images/addlink.png" alt="COLETTE O'SULLIVAN add link page">

- Users access the Add Link Page from a link on the language Links Page, passing the language argument from Links to Add Links.

- WTForms Link Form is used to define and validate the topic, type, name, url, description, rating and submit fields.

- The select topic list displayed is language specific with a default `-select-` option.

``` document_language = mongo.db.languages.find_one({"language": language }, { "topics": 1})
topics = document_language["topics"]
form.topic.choices = [("", "-select-")]+[(topic, topic) for topic in topics]
```

- As well as the data from the form fields, a MongoDB insert_one method takes the language from the language argument.

- To avoid duplicates, new urls are checked against existing links for that language. If already present, the new rating is added to the existing document and a Flash Message informs the user of the link details.

```if existing_link:
      mongo.db.links.update_one({"_id": ObjectId(existing_link["_id"])},{"$push": {"ratings": int(form.rate.data)}})
      flash(f'Link exists: {existing_link["topic"]} - {existing_link["link_type"]} - {existing_link["link_name"]}. Your rating was added!')
```

- Once a link is successfully added, the user is redirected to the language Links Page.

- Flash Messages guide the user through the add link process.

## Future Features

**Email** Email's from coletteosullivan.com

**Can't think** Addition of Django and milestone 4 topics.

# Database Design

The default Django SQLite database was used for developement and PostgreSQL for production on deployment to Heroku.

## Blog Models

The Languages Collection was created to populate topic dropdowns for each language throughout the site. As topics are updated by Code Institute, rather than hard code lists per language this approach allows for efficient list management. The administrator completes all CRUD operations directly in MongoDB.

| **NAME** | **DB TYPE** | **FORM TYPE** | **VALIDATION** | **SOURCE** |
| --- | --- | --- | --- | --- |
| **_id** | ObjectId | N/A |  N/A | Auto |
| **language** | String | N/A | N/A | Admin |
| **topic** | Array Strings | N/A | N/A | Admin |

## Portfolio Models

The Links Collection is a core data collection. Users can read all existing documents and create new documents. Their update options are limited to adding a star rating or flagging an issue with an existing document. Only the administrator can delete links documents. The Links Collection is shared amongst all users, hence the limited CRUD operations for users.

| **NAME** | **DB TYPE** | **FORM TYPE** | **VALIDATION** | **SOURCE** |
| --- | --- | --- | --- | --- |
| **_id** | ObjectId | N/A |  N/A | Auto |
| **language** | String | N/A | N/A | User *(nav dropdown)* |
| **topic** | String | Radio |Required | User |
| **url** | String | String | Required, URL, Unique| User |
| **link_name** | String | String | Required | User |
| **description** | String | Text Area | Optional | User |
| **ratings** | Array Integers | Integer | Required | User |
| **check** | Boolean | N/A | N/A | Auto *(default False)* / Admin |
| **flag** | Boolean | Button | N/A | Auto *(default False)* / User/ Admin |

## Cart Models

The Notes Collection is the second core collection. Users have the full range of CRUD operations for their own notes with no access to the notes of other users. Users must register and log in for this section of the site.

| **NAME** | **DB TYPE** | **FORM TYPE** | **VALIDATION** | **SOURCE** |
| --- | --- | --- | --- | --- |
| **_id** | ObjectId | N/A |  N/A | Auto |
| **user_id** | ObjectId | N/A | N/A | User *(login)* |
| **language** | String | N/A | N/A | User *(nav dropdown)* |
| **topic** | String | Radio | Required | User |
| **note_name** | String | String | Required | User |
| **content** | String | Text Area | Required | User |

## Contact Model

The Quotes Collection is sampled in the site's distraction sidebar. Read is the only CRUD operation available to users. The collection is managed by the administrator directly through MongoDB.

| **NAME** | **DB TYPE** | **FORM TYPE** | **VALIDATION** | **SOURCE** |
| --- | --- | --- | --- | --- |
| **_id** | ObjectId | N/A |  N/A | Auto |
| **quote** | String | N/A | N/A | Admin |
| **author** | String | N/A | N/A | Admin |

## User Model

The Users Collection is used to facilitate notes on the site. Users create a new account on the Register Page and access existing accounts on the Login Page. The remaining CRUD operations are managed by the administrator directly through MongoDB.

| **NAME** | **DB TYPE** | **FORM TYPE** | **VALIDATION** | **SOURCE** |
| --- | --- | --- | --- | --- |
| **_id** | ObjectId | N/A |  N/A | Auto |
| **user_name** | String | String |Required, Length 2-20 | User |
| **email** | String | String |Required, Email, Unique | User |
| **password** | String (hashed) | Password | Required, Length 6-10, Match Confirm | User |

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

- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) Cloud based database service used.
- [Heroku](https://www.heroku.com/) Cloud based hosting service used.

## Frontend Resources

- [Google Fonts](https://fonts.google.com/) Used for all fonts.
- [Font Awesome](https://fontawesome.com/) Used for all icons.
- [Bootstrap](https://getbootstrap.com/) Used for responsive layout and styling.
- [jQuery](https://jquery.com/) Used for DOM manipulation, enabling accordion and dark-mode functionality.
- [Juicer](https://www.juicer.io/) Used to link and display client's instagram feed.

## Backend Resources

- [pip](https://pypi.org/project/pip/) Used to install Python modules.
- [Flask](https://palletsprojects.com/p/flask/) Web application framework used.
- [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/) Used to allow communication between Python and MongoDB.
- [Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/latest/) Used for hashing user passwords.
- [Flask-Login](https://flask-login.readthedocs.io/en/latest/) Used for user session management.
- [Flask-SSLify](https://github.com/kennethreitz/flask-sslify) Used to redirect all incoming requests to HTTPS.
- [WTForms](https://jquery.com/) Used to define and validate forms.
- [Jinja](https://palletsprojects.com/p/jinja/) Web template engine used.

## Design Tools

- [Balsamiq](https://balsamiq.com/) Used to develop wireframes for the website.
- [Microsoft PowerPoint](https://office.live.com/start/PowerPoint.aspx) Used to develop the initial website proposal.
- [Affinity Designer](https://affinity.serif.com/en-gb/) Used to edit images and identify hex colours for fonts and backgrounds.
- [Techsini](https://techsini.com/multi-mockup/index.php) Used to generate README header image.
- [Microsoft Screen Recorder](https://uk.pcmag.com/operating-systems/86044/how-to-capture-video-clips-in-windows-10) Used to record README videos.
- [EZgif](https://ezgif.com/) Used to create README gifs.
- [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) Used to create README device images.

# Testing

Testing detailed in [TESTING.md](https://github.com/coderbeez/COLETTE O'SULLIVAN/blob/master/TESTING.md).

# Deployment

The website was developed in Visual Studio Code using a virtual environment and deployed to Heroku via GitHub.

The following instructions to clone and deploy assume the user has:

- IDE
- Python 3
- Pip
- Virtual Environment
- GitHub Account
- MongoDB Atlas Account
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
