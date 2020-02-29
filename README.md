# [coletteosullivan.com](https://coletteosullivan.com)

[![Build Status](https://travis-ci.com/coderbeez/interior-architect.svg?branch=master)](https://travis-ci.com/coderbeez/interior-architect)

![Site Header](https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/header.JPG)

*A portfolio website developed for an interior architect and designer using Django 2.2.*

## UX

This portfolio website was developed to provide a platform for the client, an interior architect and designer, to showcase her work. The site content, including Instagram posts, blogs, and detailed projects, is frequently updated so the client needed a site that was easy to maintain.

### User Stories

User stories for potential visitors to the website include:

#### Home Owner - Extension

After talking about it for years, I'll decided to build an extension to my house. A friend recommended Colette's site. I go straight to the Portfolio page and select a project similar to mine. Having read the story behind the design and build I purchase one of the drawings. I'm taken to a Stripe payment page, I prefer that as it feels more secure. Once complete I see a summary of my order and take note of my reference number. By email I receive both a receipt from Stripe and the drawing pdf from Colette. After mulling it over for a few days, I go back to the site and fill out the contact form leaving a description of my dream extension. Colette responds with useful advice on planning and designing to maximise light.

#### Home Owner - New Build

Having been gifted a site by my Uncle, I've decided to build a holiday home. I would like the house to be as sustainable as possible, but my funds are limited. Having seen an Instagram post by Colette on budget builds, I check out her site. I start with browsing blogs on sustainability and budgeting. I visit some of the portfolio projects. I fill out the contact form outlining my requirements. I'm so impressed by the reply from Colette that we agree to meet to discuss further. She's now drawing up my dream holiday home.

#### Interior Design Student

I'm currently enrolled in an interior design course but struggling with a colour rendering project. A fellow student recommended Colette's site. I visit the blog page and find two rendering blogs. I leave a like and a comment on both blogs. I'm sorted - they were just what I needed. I click on Instagram to start following Colette as she often posts when new blogs are uploaded. I know I'll be revisiting the site and recommending it to fellow students.

#### Architecture Firm

My firm is looking to hire an architectural technician. I've received an application from Colette and she's provided a link to her site. I review the about section outlining her skills, education and employment. She noted some portfolio projects in her application that have free drawing downloads. From these I can review her design and technical skills. Happy with her skills and breath of experience, I call her for interview.

#### Client

The client receives an email flag whenever a new comment, contact or purchase is made. She opens the site and clicks admin at the bottom of the home page. On login she can easily see and respond to outstanding comments and contacts. She simply clicks exclude on any comment or contact she would like to close. To update the site or fulfil an order, she enters admin at the end of the URL and logs into the Django admin interface. Styled and customised to look similar to the main site, the interface feels bespoke for the client.

### Design

Simplicity is key to COLETTE O'SULLIVAN with the look and flow of the site designed to provide a neutral background for the client's work.

#### Navigation

As a portfolio site, the client's name is centred and prominent above the navbar.

The main site is divided into four distinct sections, **about**, **blog**, **portfolio** and **contact** highlighted by a pared back navbar.

On small devices, the prominent name above the navbar is swapped for one in the navbar when it reaches the top the screen. From this point the navbar is sticky.

#### Colours & Fonts

A minimal colour scheme of black, white and stone, provides a neutral background for the client's content. The Google font *Montserrat*, is used in uppercase for all headings.  While another Google font *Ibarra Real Nova* is used, in both regular and italics styles, for all remaining text. Italics and hover colour changes are used to identify link text. Messages follow a traffic light green, orange and red colour scheme to inform, alert or warn users.

#### Preparation

Balsamiq was used to create wireframes for [large](https://github.com/coderbeez/interior-architect/blob/master/wireframes/wireframes_lg.pdf), [medium](https://github.com/coderbeez/interior-architect/blob/master/wireframes/wireframes_md.pdf) and [small](https://github.com/coderbeez/interior-architect/blob/master/wireframes/wireframes_sm.pdf) devices. During development, the original design was tweaked based on client feedback and requirements.

## Apps

Built with Django 2.2.10, the web site contains 7 apps: home, cv, blog, portfolio, contact, cart and users.
As there is no facility for users to register, a guest account has been created for assessment, username: guest, password: &B/82a"x

For ease of assessment:

- The BA education has a project example.
- The KOBW employment has a project example.
- The 1960s extension project has costed downloads.
- The Fordson project has a free download.

### Home App

The Home App provides a landing page for the site, introducing the client and her work. Portfolio images, blogs, and Instagram posts, entice the visitor to look further. Linked to other internal and external sources, content on this page updates automatically.

| **TYPE** | **NAME** | **DESCRIPTION** |
| --- | --- | --- |
| **View** | index | Includes 3 projects and 3 blogs. |
| **Template** | index | Owner introduction, portfolio carousel, most liked blog links, Instagram feed and admin login link. |
| | include-intro | Used to vary position of client photo and introductory text, depending on device size. |
| **Static** | Main CSS | Juicer Instagram feed formatting. |
| | Main JS | Set first carousel item as active. |

### CV App

The main challenge of the CV app was to present the clients CV in a novel way that could be easily viewed on all devices. Divided into 3 sections, expertise, education and employment, animated data circles and accordions help to break up the content. Updates are through Django's administration interface.

![CV Schema](https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/schema_cv.JPG)
**Diagram: CV Schema**

| **TYPE** | **NAME** | **DESCRIPTION** |
| --- | --- | --- |
| **Model** | Role | Individual role. Job field differentiates employment from education. |
| | Point | Bullet point for an individual role. |
| | Example | Link between a project and an individual role. |
| | Skill | Skill level to display in animated data circle. |
| **View** | About | Renders about page. Includes all roles as jobs or studies, depending on job field. Includes all skills. |
| **Template** | About | Owner introduction, animated expertise, education timeline and accordion, cv download and employment timeline and accordion. |
| **Static** | Main CSS | Timeline and data circle formatting. |
| | Main JS | Data circles and accordion animations. |

### Blog App

The Blog App affords the client the opportunity to create blogs with varying formats and site visitors the opportunity to like and comment on blogs. Although the client doesn't expect a lot of traffic, she is anxious to reply to all comments promptly so receives an email flag on new post. The comments page allows her to review and reply to all outstanding comments. Outside of comment replies, updates are through Django's administration interface.

![Blog Schema](https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/schema_blog.JPG)
**Diagram: Blog Schema**

| **TYPE** | **NAME** | **DESCRIPTION** |
| --- | --- | --- |
| **Model** | Category | Blog category list item. |
| | Blog | Individual blog. |
| | Section | Section data for an individual blog. Fields set to blank=True allow for maximum flexibility. |
| | Comment | Visitor comment and admin reply for an individual blog. |
| **Form** | CommentForm | Create a comment by adding data to the content field. |
| | ReplyForm | Update a comment by adding data to the reply and/or exclude fields. |
| **View** | Blogs | Renders an ordered list of blogs on the blogs page. Paginates after every 6 blogs. |
| | Blog | Renders an individual blog, its sections and comments, on the blog page. Renders a comment form. Creates an individual comment on valid from post. Sends email flag on valid form post.|
| | Like | Increments like field for an individual blog. |
| | Comments | View accessed by site admin only, login required. Renders outstanding comments (i.e. not excluded and no reply), oldest first, on the comments page. Renders reply form for each comment. Updates individual comment on valid form post. |
| **Template** | Blogs | Blog cards with links to individual blogs. Paginates after 6 blogs. |
| | Blog | Blog introduction and sections. Blog like count and upvote. Previous visitor blog comments and replies. New blog comment form. |
| | Comments | Login required. Outstanding blog comments. Exclude buttons and reply textboxes to update comments.  |

### Portfolio App

Through this app the client presents her project portfolio. Additional content, costed and free to download, is available for some projects. Updates are through Django's administration interface.

![Portfolio Schema](https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/schema_portfolio.JPG)
**Diagram: Portfolio Schema**

| **TYPE** | **NAME** | **DESCRIPTION** |
| --- | --- | --- |
| **Model** | Category | Project category list item. |
| | Project | Individual project. |
| | Section | Section data for an individual project. Fields set to blank=True allow for maximum flexibility. |
| | Download | PDF download available for an individual project. Price set to null=True and blank=True as some downloads are free. |
| **Form** | ContactForm | Create a contact. |
| | ReplyForm | Update a contact by adding data to the reply and/or exclude fields. |
| **View** | Projects | Renders an ordered list of projects on portfolio page. Paginates after every 6 projects. |
| | Project | Renders an individual project, its sections and downloads, on project page. |
| **Template** | Projects | Project cards with links to individual projects. Paginates after 6 projects. |
| | Project | Project introduction and sections. Downloads, if applicable, to purchase or download for free.  |

### Cart App

When it came to the Cart App, client requirements drove design decisions.

Although the app gives the client an opportunity to sell project content, it's not the main purpose of the site, and she wanted a subtle approach. On the project detail page, if downloads are available, costed downloads appear with a purchase button and free downloads with a download button. The cart navbar menu item only appears after clicking purchase on a costed download.

Although the client doesn't imagine a lot of sales, she was interested in knowing what visitors do and do not end up checking out. For these reasons, just the cart id is stored in session, with the remaining data is stored in the cart table and available to the client through the Django admin interface.

Stripe Checkout was chosen as the payment option for the site. According to the Stripe website it *creates a secure, Stripe-hosted payment page that lets you collect payments with just a few lines of code. It works across devices and is designed to increase your conversion.* The client really appreciated:

1. As a Stripe hosted option she doesn't have to worry about payment security.
2. Stripe Checkout meets the 2019 European Strong Customer Authentication (SCA) requirements.
3. A customisable interface still allowed her logo and colour scheme to be incorporated.
4. Stripe notifications settings allowed the clients to receive an email after every successful payment.
5. Stripe email settings allowed the client's customers to receive receipts directly from Stripe.

![Cart Schema](https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/schema_cart.JPG)
**Diagram: Cart Schema**

| **TYPE** | **NAME** | **DESCRIPTION** |
| --- | --- | --- |
| **Model** | Cart | Individual cart. Stripe field indicates checked out. Fulfilled field indicates order complete. |
| **View** | Cart | Renders cart page. If it exists, gets current cart id from session. |
| | Add | Adds a download to a cart. If it exists, gets current cart id from session. If it doesn't, creates a cart and adds its id to session. If passed download is not already in current cart, updates download and total in cart, and cart count in session. |
| | Remove | Removes a download from a cart. Gets current cart id from session. Removes passed download from cart. Updates cart total in cart, and cart count in session. |
| | Charge | Renders charge page and redirects payment to Stripe. Gets current cart id from session. Creates list of all downloads for current cart id. Creates Stripe checkout session as per Stripe documentation. Makes Stripe's session id available in context. |
| | Success | Renders success page. Gets Stripe's session id from URL and uses to retrieve Stripe's session data. Gets current cart id from session. Saves Stripe's session id to cart as reference. Removes cart data from session to prevent repurchase errors. Makes Stripe's session data available in context. |
| **Template** | Cart | Lists downloads in cart. Remove button to remove downloads from cart. Checkout button to proceed with purchase.  |
| | Charge | Redirects to Stripe from this page. Makes the Stripe session id available for Stripe JS.|
| | Success | Confirmation of success. Summary of order and reference from Stripe session data. |
| **Static** | Stripe JS | Stripe redirect. |

![Successful Purchase 1](https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/cart_flow1_dark.JPG)
![Successful Purchase 2](https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/cart_flow2_dark.JPG)
**Diagram: Cart Flow For Successful Purchase**

Stripe outline on their site *"not rely on the redirect to the success_url alone for fulfilling purchases as:
Malicious users could directly access the success_url without paying and gain access to your goods or services.
Customers may not always reach the success_url after a successful payment. It is possible they close their browser tab before the redirect occurs."* For these reasons the success page order summary shows Stripe's session data. For now order fulfilment is manual and my client relies on her Stripe account dashboard to verify payment success before sending pdfs.

### Contact App

Site visitors can contact the client by submitting a contact form. New contacts are flagged to the client and outstanding contacts pages gives her the facility to save and send email replies.

![Contact Schema](https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/schema_contact.JPG)
**Diagram: Contact Schema**

| **TYPE** | **NAME** | **DESCRIPTION** |
| --- | --- | --- |
| **Model** | Contact | Individual visitor contact and admin reply. |
| **View** | Contact | Renders contact form on contact page. Creates a contact on valid form post. Sends email flag on valid form post. |
| | Contacts | View accessed by site admin only, login required. Renders outstanding contacts (i.e. not excluded and no reply), oldest first, on contacts page. Renders reply form for each contact. Updates individual contact on valid form post. If update is reply, sends email, either text or html template. |
| **Template** | Contact | Contact form with highlighted required fields. |
| | Contacts | Login required. Outstanding contacts. Exclude buttons and reply textboxes to update contacts.  |
| | Reply Email | Contact reply formatted for email. |

![Contact Flow](https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/contact_flow_dark.JPG)
**Diagram: Contact Flow**

### User App

The user app is currently limited to login and logout templates using Django's User model. For this site, the client is the user, logging in using the admin link on the landing page to access the outstanding comments and contacts pages.

| **TYPE** | **NAME** | **DESCRIPTION** |
| --- | --- | --- |
| **Template** | Login | Login for site owner. |
| | Logout | Logout for site owner |

### Django Admin Interface

The client needed an interface to allow content updates. Having walked her through Django's admin interface, she felt comfortable with this option. To improve usability, app admin files were used to add inlines, order fields, filter, make editable etc. To tie in with the style of the main site, the admin interface was customised using HTML and CSS.

![Django Admin](https://github.com/coderbeez/interior-architect/blob/master/wireframes/images/django_admin_dark.JPG)
**Diagram: Customised Django Admin Interface**

### Future Features

**Search Engine Optimisation** The next thing to work on before my client launches her site is SEO.

**Automated Fulfilment** Currently fulfilment for paid downloads is manual but we would like to take advantage of automated fulfilment using webhooks as outlined in [Stripe's documentation](https://stripe.com/docs/payments/checkout/fulfillment#webhooks).

**Search Facility** As the client is currently building up her portfolio and blogs she did not want a search facility, feeling it would emphasis the lack of content. As content grows, I really feel this is something the site will need.

**Email** Currently emails are sent from a Gmail that was setup specifically for the site. In time the client would like emails to come from coletteosullivan.com

## Technologies & Programmes Used

### Languages

- [HTML](https://www.w3.org/)
- [CSS](https://www.w3.org/)
- [JavaScript](http://www.ecma-international.org/)
- [Python](https://www.python.org/)

### Development Tools

- [Visual Studio Code](https://code.visualstudio.com/) IDE used.
- [Git](https://git-scm.com/) Used to track changes during development.
- [GitHub](https://github.com/) Used to host the version control system and website content.

### Hosting Platforms & Databases

- [SQLite](https://www.sqlite.org/index.html) Default Django database used for development.
- [PostgreSQL](https://www.postgresql.org/) Database used for production on deployment to Heroku.
- [Heroku](https://www.heroku.com/) Cloud based hosting service.
- [AWS S3](https://aws.amazon.com/free/storage/?trk=ps_a131L000005OOOyQAO&trkCampaign=UK&sc_channel=PS&sc_campaign=acquisition_UK&sc_publisher=Google&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Storage|S3|UK|EN|Text&sc_content=s3_e&sc_detail=amazon%20s3&sc_category=S3&sc_segment=293639776553&sc_matchtype=e&sc_country=UK&s_kwcid=AL!4422!3!293639776553!e!!g!!amazon%20s3&ef_id=EAIaIQobChMI29XMofj25wIViaztCh2KzQZjEAAYASAAEgIR7PD_BwE:G:s) Cloud based storage for media files saved to database.
- [Go Daddy](https://ie.godaddy.com/) Domain hosting service.

### Frontend Resources

- [Stripe Checkout](https://stripe.com/ie/payments/checkout) Used to manage online payments.
- [Google Fonts](https://fonts.google.com/) Used for all fonts.
- [Font Awesome](https://fontawesome.com/) Used for all icons.
- [Bootstrap](https://getbootstrap.com/) Used for responsive layout and styling.
- [jQuery](https://jquery.com/) Used for navbar, carousel, accordion, data circles & stripe functionality.
- [jquery-circle-progress](https://github.com/kottenator/jquery-circle-progress) Used for animated data circles.
- [Juicer](https://www.juicer.io/) Used to link and display client's Instagram feed.

### Backend Resources

- [pip](https://pypi.org/project/pip/) Used to install Python modules.
- [Django](https://www.djangoproject.com/) Web framework used.
- [Django Heroku](https://pypi.org/project/django-heroku/) Used to improve deployment.
- [Gunicorn](http://docs.gunicorn.org/en/stable/) A Python WSGI HTTP server for UNIX.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) Used to render Django forms.
- [Django Math Filters](https://pypi.org/project/django-mathfilters/) Used to provide math filters for Django.
- [Pillow](https://pypi.org/project/Pillow/) A Python imaging library.
- [AWS Django Storages](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html) A custom storage backend for Django.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) Used to create, configure, and manage AWS services.
- [Psycopg2](https://pypi.org/project/psycopg2/) A PostgreSQL database adapter for Python.
- [Whitenoise](http://whitenoise.evans.io/en/stable/) Used to allow the web app to serve its own static files.
- [Stripe Checkout](https://stripe.com/ie/payments/checkout) Used to manage online payments.

### Design Tools

- [Balsamiq](https://balsamiq.com/) Used to develop wireframes for the website.
- [Microsoft Access & Publisher](https://www.office.com/) Used to create README diagrams.
- [Affinity Designer & Photo](https://affinity.serif.com/en-gb/) Used to edit images and identify hex colours for fonts and backgrounds.

## Testing

Testing detailed in [TESTING.md](https://github.com/coderbeez/interior-architect/blob/master/TESTING.md).

## Deployment

The website was developed in Visual Studio Code using a virtual environment and deployed to Heroku via Git.

The following instructions to clone and deploy assume the user has:

- IDE
- Python 3
- Pip
- Virtual Environment
- GitHub Account
- Heroku Account
- Heroku CLI
- AWS S3 Account & Bucket
- Stripe Account

### Clone in GitHub

The following instructions were taken from [GitHib Help]( https://help.github.com/en/articles/cloning-a-repository).

1. Open the [interior-architect](https://github.com/coderbeez/interior-architect) repository.
2. Click the **clone or download** button.
3. In the **clone with HTTPs** pop-up, click the **copy icon**.
4. Open **git bash**.
5. Change the current working directory to where you want the cloned directory to be made.
6. Type **git clone** and paste the URL copied earlier.
7. Press **enter**.

### IDE Development Setup

1. Create a virtual environment for your Python project.
2. Create a env.py file in the iaproject folder.
3. Add the following variables to the env.py file.

```import os
os.environ['DEBUG_VALUE']='False'
os.environ['EMAIL_HOST_USER']
os.environ['EMAIL_PASSWORD']
os.environ['SECRET_KEY']
os.environ['STRIPE_PUBLISHABLE']
os.environ['STRIPE_SECRET']
os.environ['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY']
os.environ['AWS_STORAGE_BUCKET_NAME']
os.environ['DATABASE_URL']
os.environ['ALLOWED_HOSTS']
```

4. Use `pip install -r requirements.txt` to install Python required modules.

### Deploy to Heroku

1. On the [Heroku](https://id.heroku.com/login) website log into your account.
2. Click **new** and **create new app**.
3. Give your app a **name** (it must be unique), select a **region** and click **create app**.
4. Under **resources** choose add on postgres hobby free.
5. Click **reveal id**.
6. Return to your IDE and fill the values for your environment variables in the env.py file.
7. Return to the Heroku dashboard and under **settings/ config vars** click **reveal vars**. Add the key values for all your environment variables.
8. In your console type ```heroku login```, and when prompted click any key to open the browser and log into your heroku account.
9. Type ```heroku git:remote -a appname```.
10. Type ```git subtree push --prefix iaproject heroku master``` to push the code to Heroku.
11. Cd into iaproject and type ```python manage.py makemigrations``` and ```python manage.py migrate``` to create and run migrations.
12. Type ```python manage.py createsuperuser``` to create a super user.
13. Open the Heroku app address adding ```/admin``` to the end of the URL and login with the super user credentials.
14. Use this Django admin interface to add data to populate the blog, cv and portfolio apps.

## Credits

### Content

- Site concept and design by website developer.
- Site content provided by client.

### Media

- Favicon/logo by Blasko purchased from [Vector Stock](https://www.vectorstock.com/royalty-free-vector/house-construction-architect-logo-icon-vector-23672011).
- Work desk photo by Jessica Arends from [Unsplash](https://unsplash.com/photos/UzPbvwqvKNE).

### Code

#### README

- Aligning images from [Stack Overflow](https://stackoverflow.com/questions/12090472/github-readme-md-center-image).

#### HTML Code

- Remove Bootstrap card header border radius [Stack Overflow](https://stackoverflow.com/questions/46316719/how-to-make-card-header-no-border-radius-in-bootstrap-4).

#### CSS Code

- Timeline [Bootsnipp](https://bootsnipp.com/snippets/xrKXW).

#### JavaScript Code

- jquery-circle-progress [Kottenator](https://github.com/kottenator/jquery-circle-progress).
- Determine if item is at top of screen [Stack Overflow](https://stackoverflow.com/questions/7543718/test-in-jquery-if-an-element-is-at-the-top-of-screen).
- Carousel set first loop image as active [Stack Overflow](https://stackoverflow.com/questions/52870493/carousel-set-first-loop-image-as-active-item).
- $.each [Stack Overflow](https://stackoverflow.com/questions/34949440/how-to-get-data-attribute-value-of-all-elements-using-jquery).
- Check if element is hidden in jQuery [Stack Overflow](https://stackoverflow.com/questions/178325/how-do-i-check-if-an-element-is-hidden-in-jquery).
- Show, hide elements by data attribute [Stack Overflow](https://stackoverflow.com/questions/31802861/show-hide-elements-by-data-attribute).
- Get data attributes in jQuery [Stack Overflow](https://www.codeproject.com/Questions/369517/how-to-get-data-attributes-in-jquery).

#### Python Code

##### Django

- [Brad Traversy - YouTube Django Crash Course](https://www.youtube.com/watch?v=e1IyzVyrLSU).
- [Brad Traversy - Udemy Django Dev To Development](https://www.udemy.com/course/python-django-dev-to-deployment/).
- [Pretty Printed - YouTube Django Playlist](https://www.youtube.com/watch?v=QVX-etwgvJ8&list=PLXmMXHVSvS-DQfOsQdXkzEZyD0Vei7PKf&index=1).
- [Corey Schafer - YouTube Django Playlist](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p).
- [Real Python - Build A Portfolio App](https://realpython.com/get-started-with-django-1/).
- [Coding Point - Django Ecommerce Web App](https://www.youtube.com/playlist?list=PLPp4GCMxKSjCM9AvhmF9OHyyaJsN8rsZK).
- [Django 2.2 Documentation](https://docs.djangoproject.com/en/2.2/).

##### Models & Views

- Related names [Simple Is Better Then Complex](https://simpleisbetterthancomplex.com/tips/2018/02/10/django-tip-22-designing-better-models.html#naming-your-models).
- Choice Fields [Stack Overflow](https://stackoverflow.com/questions/18676156/how-to-properly-use-the-choices-field-option-in-django).
- Related names [Simple Is Better Then Complex](https://simpleisbetterthancomplex.com/tips/2018/02/10/django-tip-22-designing-better-models.html#naming-your-models).
- Limiting query results [Stack Overflow](https://stackoverflow.com/questions/6574003/django-limiting-query-results).
- F strings [Real Python](https://realpython.com/python-f-strings/).
- Bare excepts [Stack Overflow](https://stackoverflow.com/questions/4990718/about-catching-any-exception)

##### Users

- Python Django Tutorial Part 6 - User Registration [Corey Schafer](https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6).

##### Forms

- Send POST data from inside for loop [Stack Overflow](https://stackoverflow.com/questions/38046905/sending-post-data-from-inside-a-django-template-for-loop).
- Save instance [Real Python](https://realpython.com/get-started-with-django-1).
- Customising model form fields [Django Docs](https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/).
- Form Widgets [Coding Entrepreneurs](https://www.youtube.com/watch?v=-oWIyFYyNQw).

##### Templates

- Multiply in template tag [Stack Overflow](https://stackoverflow.com/questions/6285327/how-to-do-math-in-a-django-template).
- Foreign key in template tag [Stack Overflow](https://stackoverflow.com/questions/12281965/django-foreign-key-relation-in-template).

##### Pagination

- [Django Documentation](https://docs.djangoproject.com/en/3.0/topics/pagination/).

##### Shop Cart

- Django Tutorial for Beginners Part 22, Cart App [Coding Point](https://www.youtube.com/watch?v=20HCDEwEdeo&list=PLPp4GCMxKSjCM9AvhmF9OHyyaJsN8rsZK&index=23&t=0s).
- Stripe Checkout documentation [Stripe](https://stripe.com/docs/payments/checkout/one-time).
- Capture URL parameters [Stack Overflow](https://stackoverflow.com/questions/150505/capturing-url-parameters-in-request-get).
- Clear session [Stack Overflow](https://stackoverflow.com/questions/16039399/how-to-clear-all-session-variables-without-getting-logged-out).

##### Email

- How to send emails in Django [Data Flair](https://data-flair.training/blogs/django-send-email/).
- Sending a confirmation email using Gmail [Coding Entrepreneurs](https://www.youtube.com/watch?v=51mmqf5a0Ss).
- Sending a confirmation email using Gmail [Coding Entrepreneurs](https://www.youtube.com/watch?v=51mmqf5a0Ss).
- Gmail less secure apps [Google](https://support.google.com/mail/thread/5621336?hl=en).

##### Admin

- Admin.py Inlines [Stack Overflow](https://stackoverflow.com/questions/14308050/django-admin-nested-inline).
- Admin.py Display, filters, edits [Brad Traversy](https://www.udemy.com/course/python-django-dev-to-deployment/).
- Admin.py Order [Stack Overflow](https://stackoverflow.com/questions/4571916/django-admin-sort-order).
- Admin CSS [Brad Traversy](https://www.udemy.com/course/python-django-dev-to-deployment/).
- Admin HTML [Brad Traversy](https://www.udemy.com/course/python-django-dev-to-deployment/).
- Admin HTML Setting favicon [Stack Overflow](https://stackoverflow.com/questions/34959897/set-favicon-in-django-admin).

### Acknowledgements

- Many thanks to my client for her wonderful content, endless faith and infectious enthusiasm! To my mentor Ali Ashik, and ***all*** on Code Institute's Slack channel for making this journey possible.
