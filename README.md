[![Build Status](https://travis-ci.com/coderbeez/interior-architect.svg?branch=master)](https://travis-ci.com/coderbeez/interior-architect)

<div align="center">
<img src="https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/header.JPG" alt="Site header">
</div>

# [coletteosullivan.com](https://coletteosullivan.com)

*A portfolio website for an interior architect and designer, developed for a client while completing the Code Institute's fullstack milestone module.*

# UX

This portfolio website was developed to provide a platform for the client, an interior architect and designer, to showcase her work. The site content, including instagram posts, blogs, and detailed projects, is frequently updated so the client needed a site that was both flexible and easy to update.

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

Simplicity is key to COLETTE O'SULLIVAN with the look and flow of the site designed to provide a neutral background for the client's work.

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

The Home App provides a landing page for the site, introducing the client and her work. Blogs, instagram posts and project images entice the visitor to look further. This content is linked to either external sources

![Home Schema](https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/schema_home.JPG)

| **TYPE** | **NAME** | **DESCRIPTION** |
| --- | --- | --- |
| **View** | index | Import portfolio and blog models to display the top 3 most liked blogs and 3 selected projects. |
| **Template** | index | - |
| | include-intro | Used to position client photo and introductory text depepening on device size. |

## CV App

The main challenge of the CV app was to find a way to allow the client to present and maintain her CV in a novel way. Divided into 3 sections, skills, eductaion and expertise content is linked to model tables verses hard coded to enable the client to easily update through Django's default interface.

![CV Schema](https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/schema_cv.JPG)
*Diagram: CV Schema*

| **TYPE** | **NAME** | **DESCRIPTION** |
| --- | --- | --- |
| **Model** | Role | N/A |
| | Point | N/A |
| | Example | N/A |
| | Skill | N/A |
| **View** | About | - |
| **Template** | About | - |

## Blog App

The Blog App provides the client with a facility to create blogs with different formats and site visitors the facility to add likes and comments to blogs. The 3 blogs with the highest number of likes are displayed on the home page. As the client wanted to reply to all posted comments, a flag is sent to the client when a new comment is added. After logging in, the comments page allows the client to quickly review, reply and/or exclude outstanding comments from the site.

![Blog Schema](https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/schema_blog.JPG)
*Diagram: Blog Schema*

| **TYPE** | **NAME** | **DESCRIPTION** |
| --- | --- | --- |
| **Model** | Category | - |
| | Blog | - |
| | Section | - |
| | Comment | - |
| **Form** | CommentForm | - |
| | ReplyForm | - |
| **View** | Blogs | - |
| | Blog | - |
| | Like | - |
| | Comments | Login required |
| **Template** | Blogs | - |
| | Blog | - |
| | Comments | - |

## Portfolio App

The portfolio app is allows the client present detailed projects. The client can additinal content. She had chosen to make some available free of charge and others are charged.

![Potfolio Schema](https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/schema_portfolio.JPG)
*Diagram: Portfolio Schema*

| **TYPE** | **NAME** | **DESCRIPTION** |
| --- | --- | --- |
| **Model** | Category | N/A |
| | Project | N/A |
| | Section | N/A |
| | Download | N/A |
| **Form** | ContactForm | - |
| | ReplyForm | - |
| **View** | Projects | - |
| | Project | - |
| **Template** | Projects | - |
| | Project | - |

## Cart App

When it came to the Cart App, client requirements drove design decisions.

Although the app gives the client an opprtunity to sell her project drawings, it's not the main purpose of the site, and she wanted a subtle approach. On the project detail page, if downloads are available, costed downloads appear with a purchase button and free downloads with a download button. The cart navbar menu item only appears after clicking purchase on a costed download.

Although the client doesn't imagine a lot of sales, she was interested in knowing what visitors do and do not end up checking out. For these reasones, just the cart id is stored in session, with the remaining data is stored in the cart table and available to the client through the Django admin interface.

Stripe Checkout was chosen as the payment option for the site. According to the Stripe website it *creates a secure, Stripe-hosted payment page that lets you collect payments with just a few lines of code. It works across devices and is designed to increase your conversion.* The client really appreciated:

1. As a Stripe hosted option she doesn't have to worry about payment security.
2. Stripe Checkout meets the 2019 European Strong Customer Authentication (SCA) requirements.
3. A customisable interface still allowed her logo and colour scheme to be incorporated.
4. Stripe notifications settings allowed the clients to receive an email after every successful payment.
5. Stripe email settings allowed the client's customers to receive receipts directly from Stripe.
Payment methods: Credit cards, debit cards, Apple Pay, Google Pay, FPX and iDEAL
Payment types: One-time and recurring payments
Payment authentication: Dynamic 3D Secure (ready for Strong Customer Authentication)
Localization: Localized for 14 languages
Email receipts: Automatic email receipts to your customers

![Cart Schema](https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/schema_cart.JPG)
*Diagram: Cart Schema*

| **TYPE** | **NAME** | **DESCRIPTION** |
| --- | --- | --- |
| **Model** | Cart | - |
| **View** | Cart | - |
| | Add | - |
| | Remove | - |
| | Charge | - |
| | Success | - |
| **Template** | Cart | - |
| | Charge | - |
| | Success | - |

![Contact Schema](https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/cart_flow1.JPG)
![Contact Schema](https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/cart_flow2.JPG)


*Diagram: Cart Flow - Successful Purchase*

## Contact App

Site visitors can contact the client by submitting a contact form. New contacts are flagged to the client and outstanding comments pages gives her the facility to save and send replies.

![Contact Schema](https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/schema_contact.JPG)
*Diagram: Contact Schema*

| **TYPE** | **NAME** | **DESCRIPTION** |
| --- | --- | --- |
| **Model** | Contact | - |
| **View** | Contact | - |
| | Contacts | - |
| **Template** | Contact | - |
| | Contacts | Login required |
| | Reply Email | - |

![Contact Flow](https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/contact_flow.JPG)
*Diagram: Contact Flow*

<div align="center">
<img src="https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/contact_flow_dark.JPG" alt="COLETTE O'SULLIVAN contact flow">
<strong>Contact Flow Diagram</strong>
</div>

## User App

The user app is currently limited to login and logout templates using Django's User models. For this site, the client is the user, logging in using the admin link on the landing page to access the outstanding comments and contacts pages.

![User Schema](https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/schema_user.JPG)

| **TYPE** | **NAME** | **DESCRIPTION** |
| --- | --- | --- |
| **Template** | Login | - |
| | Logout | - |

## Django Admin Interface

The client needed an interface to allow content updates. Having walked her through Django's default admin interface, she felt comfortable with this option. To improve usability, app admin files were used to add inlines, order fields, filter, make editable etc. To tie in more with the style of the main site, the admin inteface css was customised.

<div align="center">
<img src="https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/django_admin_dark.JPG" alt="COLETTE O'SULLIVAN django admin" style="border-style: solid double;">
<strong>Customised Django Admin Interface</strong>
</div>

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
- [jquery-circle-progress](https://github.com/kottenator/jquery-circle-progress) Used for animated skill circles.
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

- Logo by Blasko purchased from [Vector Stock](https://www.vectorstock.com/royalty-free-vector/house-construction-architect-logo-icon-vector-23672011).
- /Spotify image adapted from [Spotify](https://www.spotify.com/ie/).

## Code

### README

- Aligning images from [Stack Overflow](https://stackoverflow.com/questions/12090472/github-readme-md-center-image).

### HTML Code

- Remove Bootstrap card header border radius [Stack Overflow](https://stackoverflow.com/questions/46316719/how-to-make-card-header-no-border-radius-in-bootstrap-4).

### CSS Code

- Timeline [Bootsnipp](https://bootsnipp.com/snippets/xrKXW).

### JavaScript Code

- jquery-circle-progress [Kottenator](https://github.com/kottenator/jquery-circle-progress).
- Determine if item is at top of screen [Stack Overflow](https://stackoverflow.com/questions/7543718/test-in-jquery-if-an-element-is-at-the-top-of-screen).
- Carousel set first loop image as active [Stack Overflow](https://stackoverflow.com/questions/52870493/carousel-set-first-loop-image-as-active-item).
- $.each [Stack Overflow](https://stackoverflow.com/questions/34949440/how-to-get-data-attribute-value-of-all-elements-using-jquery).
- Check if element is hidden in jQuery [Stack Overflow](https://stackoverflow.com/questions/178325/how-do-i-check-if-an-element-is-hidden-in-jquery).
- Show, hide elements by data attribute [Stack Overflow](https://stackoverflow.com/questions/31802861/show-hide-elements-by-data-attribute).
- Get data attributes in jQuery [Stack Overflow](https://www.codeproject.com/Questions/369517/how-to-get-data-attributes-in-jquery).

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
- Stripe Checkout documentation [Stripe](https://stripe.com/docs/payments/checkout/one-time).

#### Django Admin Interface Settings

- Admin.py [Brad Traversy](https://www.udemy.com/course/python-django-dev-to-deployment/).
- CSS [Brad Traversy](https://www.udemy.com/course/python-django-dev-to-deployment/).


#### Other

- /Before request decorator [Pythonise](https://pythonise.com/series/learning-flask/python-before-after-request).



## Acknowledgements

- Many thanks to my client for her direction and infectious enthusiasum! To my mentor Ali Ashik, and ***all*** on Code Institute's Slack channel.

<div align="center">
<img src="https://github.com/coderbeez/COLETTE O'SULLIVAN/blob/master/wireframes/images/notes.gif" alt="COLETTE O'SULLIVAN notes page">
</div>

<img align="right" height="500" src="https://github.com/coderbeez/COLETTE O'SULLIVAN/blob/master/wireframes/images/addnote.png" alt="COLETTE O'SULLIVAN add note page">

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



