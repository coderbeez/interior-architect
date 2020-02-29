# Testing

## Validation

### HTML

[W3C Validation Service](https://validator.w3.org/) Used to test the validity of HTML.

- A number of issues associated with templates caused errors in rendered html:

Linebreaks in textareas adds extra p tags.

```<p><p>Text</p></p>```

Empty th tags are added to single field forms.

```<tr><th></th><td>
<textarea name="content" cols="40" rows="5" class="textarea-style" required id="id_content">
</textarea>
</td></tr>
```

- A Juicer h1 causes errors and warnings. Leaving text within the h1 renders the Juicer logo, which the client did not want. Removing the h1 completely resulted in the Juicer logo showing. We compromised by leaving the h1 tag empty.

### CSS

[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) Used to test the validity of CSS – no errors found.

[Autoprefixer CSS](https://autoprefixer.github.io/) Used to ensure all relevant vendor prefixes included.

### JavaScript

[JSHint](https://jshint.com/) Used to test the validity of JavaScript functions – no errors found.

### Python

[Python-autopep8](https://pypi.org/project/autopep8/) Used to ensure Python conforms to Pep 8 styling. All code conforms apart from:

- *Settings.py Line too long* Didn't want to split string in password validator.
- *Settings.py Module level import not at top of file* Django Heroku docs say to place at bottom of file.
- *Credit urls too long* Some urls for credits are showing errors for length.

### Continuous Integration

[Travis](https://travis-ci.com/) was used throughout the build for continuous integration. Full details on how to apply are available [here](https://docs.travis-ci.com/user/tutorial/#to-get-started-with-travis-ci).

## Manual Testing

Throughout the development process Chrome was used to test for functionality and Chrome developer tools for layout and responsiveness on various screen sizes. Once deployed, the site was also tested on Edge, Firefox and Safari browsers and on both android and iOS mobiles.

After sign-off, structured manual testing of the site was carried out on various browsers and screens sizes. A detailed plan was followed to ensure code was thoroughly tested.

| **BROWSER** | **iOS** | **Android** | **iOS** | **Edge** | **Chrome** | **Firefox** | **Safari** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **SCREEN SIZE** | **Small** | **Small** | **Medium** | **Large** | **Large** | **Large** | **Large** |
| coletteosullivan https | P | P | P | P | P | P | P |
| www.coletteosullivan https | P | P | P | P | P | P | P |
| **HOME PAGE** | --- | --- | --- | --- | --- | --- | --- |
| Carousel | P | P | P | P | P | P | P |
| Liked Blogs | P | P | P | P | P | P | P |
| Instgarm Feed | P | P | P | P | P | P | P |
| Navbar Home Link | P | P | P | P | P | P | P |
| Navbar Sticky | P | P | N/A | N/A | N/A | N/A | N/A |
| **ABOUT PAGE** | --- | --- | --- | --- | --- | --- | --- |
| Navbar Link Bold | P | P | P | P | P | P | P |
| Expertise JS | N/A | N/A | P | P | P | P | P |
| Education List & Accordion | P | P | P | P | P | P | P |
| Education Example | P | P | P | P | P | P | P |
| Employment CV | P | P | P | P | P | P | P |
| Employment List & Accordion| P | P | P | P | P | P | P |
| Employment Example | P | P | P | P | P | P | P |
| **BLOG LIST PAGE** | --- | --- | --- | --- | --- | --- | --- |
| Navbar Link Bold | P | P | P | P | P | P | P |
| List | P | P | P | P | P | P | P |
| Pagination | P | P | P | P | P | P | P |
| Link | P | P | P | P | P | P | P |
| **BLOG DETAIL PAGE** | --- | --- | --- | --- | --- | --- | --- |
| Navbar Link Bold | P | P | P | P | P | P | P |
| Detail | P | P | P | P | P | P | P |
| Like Count | P | P | P | P | P | P | P |
| Like Click Count & Message | P | P | P | P | P | P | P |
| Comment List | P | P | P | P | P | P | P |
| Comment Post & Message | P | P | P | P | P | P | P |
| Comment Post List | P | P | P | P | P | P | P |
| Email Flag | P | P | P | P | P | P | P |
| **PORTFOLIO LIST PAGE** | --- | --- | --- | --- | --- | --- | --- |
| Navbar Link Bold | P | P | P | P | P | P | P |
| List | P | P | P | P | P | P | P |
| Pagination | P | P | P | P | P | P | P |
| Link | P | P | P | P | P | P | P |
| **PORTFOLIO DETAIL PAGE** | --- | --- | --- | --- | --- | --- | --- |
| Navbar Link Bold | P | P | P | P | P | P | P |
| Detail | P | P | P | P | P | P | P |
| **Project 1** | --- | --- | --- | --- | --- | --- | --- |
| Download Costed Click & Message | P | P | P | P | P | P | P |
| Navbar Cart & Count | P | P | P | P | P | P | P |
| Download Duplicate Message | P | P | P | P | P | P | P |
| **Project 2** | --- | --- | --- | --- | --- | --- | --- |
| Download Fee Click | P | P | P | P | P | P | P |
| Download PDF | P | P | P | P | P | P | P |
| **CART PAGE** | --- | --- | --- | --- | --- | --- | --- |
| Navbar Link Bold | P | P | P | P | P | P | P |
| Items & Total | P | P | P | P | P | P | P |
| Remove Click Message & Total | P | P | P | P | P | P | P |
| Checkout Click & Redirect | P | P | P | P | P | P | P |
| **CHARGE/STRIPE PAGE** | --- | --- | --- | --- | --- | --- | --- |
| Client Name & Logo | P | P | P | P | P | P | P |
| Total | P | P | P | P | P | P | P |
| Download Name, Price & Desciption | P | P | P | P | P | P | P |
| Card | P | P | P | P | P | P | P |
| **SUCCESS PAGE** | --- | --- | --- | --- | --- | --- | --- |
| Navbar Cart | P | P | P | P | P | P | P |
| Order Summary | P | P | P | P | P | P | P |
| Reference | P | P | P | P | P | P | P |
| Cart DB Table Updated | P | P | P | P | P | P | P |
| Stripe Site Dashboard Success | P | P | P | P | P | P | P |
| **CONTACT PAGE** | --- | --- | --- | --- | --- | --- | --- |
| Contact Link Bold | P | P | P | P | P | P | P |
| Fields | P | P | P | P | P | P | P |
| Click Post Message & Redirect | P | P | P | P | P | P | P |
| Email Flag| P | P | P | P | P | P | P |
| **ADMIN LOGIN PAGE** | --- | --- | --- | --- | --- | --- | --- |
| Login  | P | P | P | P | P | P | P |
| Navbar Comments, Contacts, Logout  | P | P | P | P | P | P | P |
| **ADMIN COMMENTS PAGE** | --- | --- | --- | --- | --- | --- | --- |
| Outstanding List | P | P | P | P | P | P | P |
| Exclude Click Message & List | P | P | P | P | P | P | P |
| Blog Comments | P | P | P | P | P | P | P |
| Reply Click Message & List | P | P | P | P | P | P | P |
| Blog Comments | P | P | P | P | P | P | P |
| **ADMIN CONTACT PAGE** | --- | --- | --- | --- | --- | --- | --- |
| Outstanding List | P | P | P | P | P | P | P |
| Exclude Click Message & List | P | P | P | P | P | P | P |
| Reply Click Message & List | P | P | P | P | P | P | P |
| Email | P | P | P | P | P | P | P |
| **ADMIN LOGOUT PAGE** | --- | --- | --- | --- | --- | --- | --- |
| Logout Click | P | P | P | P | P | P | P |
| Navbar Remove Comments, Contacts, Logout | P | P | P | P | P | P | P |
| Login Click | P | P | P | P | P | P | P |

P - Passed

N/A - Not Applicable

## Bug Log

1. **Heroku CSS Updates** During development it became apparent that CSS updates were not being reflected in Heroku deployments. The solution from Stack Overflow was to restart Heroku in the terminal `Heroku restart -a coderbeez-qwerty` .
Email https://support.google.com/mail/thread/5621336?hl=en
Set Less secure apps to on in google account

Price in success - decimal

Email cos web link including safe links - making url look ugly
Why Outlook Adding “Safelinks.Protection.Outlook.Com” to All URLs

coletteosullivan.com not working

1. Open AWS account https://devcenter.heroku.com/articles/pointdns
