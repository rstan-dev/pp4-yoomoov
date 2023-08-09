# Project Name - YooMoov

* [Link to Deployed Project](https://yoomoov-2cbb8d75e399.herokuapp.com/)

## CONTENTS
* [USER EXPERIENCE (UX)](#user-experience)
  * [Purpose & target audience](#purpose-and-target-audience)
  * [Goals](#goals)
* [PROJECT DESIGN](#project-design)
  * [Agile Approach](#agile-approach)
  * [Wireframes](#wireframes)
  * [User Stories](#user-stories)
  * [Logic](#logic)
  * [Color Scheme](#color-scheme)
  * [Imagery](#imagery)
  * [Typography](#typography)
  * [MVP](#mvp)
* [FEATURES](#features)
* [VALIDATION](#validation)
* [TECH STACK](#tech-stack)
* [MODULES & LIBRARIES](#modules-libraries)
* [TESTING](#testing)
  * [Tests performed](#tests-performed)
  * [User Story Tests](#user-story-tests)
  * [Bugs resolved](#bugs-resolved)
  * [Unresolved bugs](#unresolved-bugs)
  * [Improvements & future developments](#improvements-and-future-developments)
* [DEPLOYMENT](#deployment)
* [FORKING & CLONING INSTRUCTIONS](#forking-cloning-instructions)
* [CREDITS](#credits)
  * [Code](#code)
  * [Resources](#resources)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgements](#acknowledgements)



## USER EXPERIENCE

   ### Purpose and target audience

YooMov is a website for people and businesses looking to hire a van and a driver to move belongings from one location to another.  An administrator can create different types of van listings in different locations, which will be displayed to a user on the front end.

A website visitor can search for van types in various locations using a filter, they can open up a detail page about each van, they can read some reviews from other customers and they can book a date for the van, or they can send an email via a contact form if they have any questions.

The user can register and log in to their User Dashboard to view, edit or delete their bookings and they can also leave feedback for any bookings that have been completed.

The administrator will receive an email notification any time there is a new booking or a change to a booking, prompting them to change the status of the booking, from pending to approved or to completed. They can also review and approve feedback before it is published live on the front end.

<img src="/workspace/pp4-yoomoov/documentation/readme/am_I_responsive_screenshot.png">

  ### Goals
The main objectives of this website are:
1. Build an easy-to-use and navigate, fully responsive booking website, with a clean interface.
2. Create user account functionality for the administrator to add van listings and manage bookings.
3. Create a personal dashboard for a customer to log in, create, view, edit and delete bookings.
4. Create a feedback module so customers and admin can leave and approve feedback.
5. Configure email to notify the customer and the administrator of any changes to bookings.


## PROJECT DESIGN

  ### Agile Approach
  From the start the project was managed using [GitHub Projects (View Here)](https://github.com/users/rstan-dev/projects/6), using an agile approach.
  - The project goals were broken into epics, which were broken into user stories with acceptance criteria and individual tasks.
  - Each user story was allocated a certain number of story points based on a rough estimation of time to complete the work.
  - This allowed me to create a roadmap with milestones and target dates.
  - Each User Story was assigned a label according to the MoSCoW system so I could prioritise the work.
<img src="/workspace/pp4-yoomoov/documentation/readme/github_projects.png">

  ### Wireframes  (created in [Balsamiq](https://balsamiq.cloud/))
   The initial wireframes were created to understand how the site would work, and this layout would drive User Stories, the logic required and overall design artwork decisions.

<img src="/workspace/pp4-yoomoov/documentation/readme/home.png">
<img src="/workspace/pp4-yoomoov/documentation/readme/services.png">
<img src="/workspace/pp4-yoomoov/documentation/readme/van_detail.png">
<img src="/workspace/pp4-yoomoov/documentation/readme/dashboard.png">

  ### User Stories
  All epics, user stories with their acceptance criteria and tasks can be viewed on the YooMoov [GitHub Project board](https://github.com/users/rstan-dev/projects/6)

- There were 13 Epics created from Project Concept to Project Submission.

- There were 29 User Stories Created including:
  1. USERSTORY(# 1): Gather General Requirements and visual layout
    - As a developer, I can see how the site should be laid out so that the functionality can be developed incrementally.
  2. USERSTORY(#2): Initial Django project setup
    - As a developer, I can access the initial project files in my developer environment, and deploy to Heroku, so that I can resolve any deployment issues early on.
  3. USERSTORY(#3): Create bootstrap template
    - As a developer I can deploy a basic site design so that it meets the minimum viable requirements.
  4. USERSTORY(#4 ): Bootstrap Navigation Breadcrumbs
    - As a website user, I can easily navigate the website so that I can find what I need.
  5. USERSTORY(#5 ): Create Van Model
    - As an admin user I can create Van details in the admin area so that they populate fields on the front end template.
  6. USERSTORY(#6 ): Search for van types
    - As a website user, I can use the Van Finder to display a list of vans by size, location or county.
  7. USERSTORY(#7): Display Van detail
    - As a website user, I can read more detail about a van so I can book or enquire.
  8. USERSTORY(# 8): Create SuperUser Account
    - As an admin user I can login into the admin area so that I can manage website content.
  9. USERSTORY(#9): Customise admin area branding
    - As an admin user, I recognise the admin area has the same look and feel as the front end, for continuity purposes.
  10. USERSTORY(#10 ): User Registration
    - As a website user, I can register, log in and log out to view my dashboard.
  11. USERSTORY(# 11 ): Create Booking Model
    - As an admin user, I can create Booking details in the admin area so that I can take a booking over the phone.
  12. USERSTORY(#12 ): View Bookings on User Dashboard
    - As a logged-in user, I can view any bookings I have made in a list on my Dashboard.
  13. USERSTORY(# 13): Create Booking on User Dashboard
    - As a logged-in user I can create a booking from a listing page, which will appear on the user's dashboard.
  14. USERSTORY(#14 ): Edit Booking on User Dashboard
    - As a logged-in User, I can edit the booking details from the Dashboard so I can make any changes.
  15. USERSTORY(#15 ): Delete booking on user dashboard
    - As a logged-in User, I can delete the booking details from the Dashboard.
  16. USERSTORY(#16): Create Feedback Model
    - As an admin user I can add and view Feedback details in the admin area and approve feedback for display on the relevant detail page.
  17. USERSTORY(# 17): Feedback option after booking completion
    - As a logged-in user who has made a booking, I can leave feedback using the feedback button next to the booking on my Dashboard.
  18. USERSTORY(#18 ): User can see their feedback on their dashboard
    - As a logged-in user, I can see all the feedback I have left for other bookings on my Dashboard.
  19. USERSTORY(#19): Send email to the admin via the contact form
    - As an admin, I can receive an email with the details from the contact form, so I can follow up with the customer.
  20. USERSTORY(#20 ): Send booking email notifications
    - As a user I can receive an email notification when the booking has been created, approved, updated or deleted, so I can manage the booking in my account.
  21. USERSTORY(#21 ): Admin to receive email notifications when feedback has been created
    - As an admin, I can receive an email notification when a user creates feedback.
  22. USERSTORY(# 22): User to receive email when feedback has been approved by admin
    - As a user, I can receive an email notification when my feedback has been approved.
  23. USERSTORY(#23 ): Onscreen notification when logged in or out
    - As a user, I will see an on-screen notification to let me know I have logged in or logged out.
  24. USERSTORY(#24): Menu Bar notification when User is logged in
    - As a logged in user, I will see a welcome message on the navbar and a logout link.
  25. USERSTORY(#25 ): Create user story tests
    - As a developer, all user story tests will pass, so that I can be certain the site functions as intended.
  26. USERSTORY(# 26): Test Html, CSS, JS, Python, Lighthouse
    - As a developer all code will pass through validation tools to identify any issues, errors or non-conformance.
  27. USERSTORY(# 27): Create Automatic unit tests
    - As a developer, I will write some automatic unit tests for the purposes of demonstrating competence.
  28. USERSTORY(# 28): Final Deployment
    - As a developer, I will ensure the final project is fully deployed to Heroku so that it matches the development project.
  29. USERSTORY(#29): Final Checks
    - As a developer, I will complete the final checks to ensure all criteria for the project have been met before submission.


  ### Logic
  The database schema and website logic was conceived and created using [Lucid](https://lucid.app/) as follows:

  1. Website Flow:
  <img src="/workspace/pp4-yoomoov/documentation/readme/yoomoov_site_logic.jpeg">

  2. Database Structure:
  <img src="/workspace/pp4-yoomoov/documentation/readme/yoomoov_db_schema.png">

  ### Color Scheme (created in [Canva](https://www.canva.com/))
  An orange color scheme was chosen because it's associated with optimism and energy, many brands use orange to convey a message of positivity. Many marketers use orange to get an audience excited about something because it is an attention-grabbing, warm color that really pops.

  I created the logo in Canva using royalty-free images to create the distinct cow icon so there could be a play on the word YooMoov (You Moove) and chose a complimentary color palette.

   - <img src="/workspace/pp4-yoomoov/documentation/readme/cow_icon.png">
   - <img src="/workspace/pp4-yoomoov/documentation/readme/logo_yoomoov_orange1.jpg">
   - <img src="/workspace/pp4-yoomoov/documentation/readme/color_pallette.png">

   With a color palette in mind I could create a project style guide:
   - <img src="/workspace/pp4-yoomoov/documentation/readme/yoomoov_style_guide.png">

   ### Imagery
   Stock Images were sourced from:
   1. Hero Photo by [Bernard Foss:](https://www.pexels.com/photo/white-vans-parked-on-gray-concrete-road-4620555/).
   2. Stock van images by [Canva Pro](https://www.canva.com/).

  - I used Canva to build the initial designs, which was the basis for finding a suitable bootstrap template that could help me achieve the look and feel as easily as possible.
  - <img src="/workspace/pp4-yoomoov/documentation/readme/canva_mockup_home.jpeg">
  - <img src="/workspace/pp4-yoomoov/documentation/readme/canva_mockup_services.jpeg">
  - <img src="/workspace/pp4-yoomoov/documentation/readme/canva_mockup_van_detail.jpeg">

   ### Typography
   * I found a bootstrap layout called [Lumia](https://bootstrapmade.com/demo/Lumia/)from bootsrapmade.com which aligned closely with the layout I needed.
   * I kept the default Google font of Raleway and sans serif.

   ### MVP
   Using the GitHub project board I was able to prioritise user stories to give me an MVP incrementally.
   1. I built the front end as a static website first.
   2. I developed the Django admin area so an administrator could manage the site.
   3. I built User CRUD functionality next via their dashboard.
   4. I configured on-sreen notifications to give feedback to the user.
   5. I built a feedback mechanism - first for the administrator, and then for front end users.
   6. I configured email notifications to alert the user and the administrator.


## FEATURES
The following features have been implemented:
1. Fully responsive website consisting of:
  - Home.
  - Services.
  - All Vans Page.
  - Vans Finder Filter to search by Size, Location or County.
  - Van detail page.
  - Contact form that sends an email to the admin user.
  - User Dashboard with CRUD functionality to manage bookings and add feedback.
  - <img src="/workspace/pp4-yoomoov/documentation/readme/feature_home.png">
  - <img src="/workspace/pp4-yoomoov/documentation/readme/feature_services.png">
  - <img src="/workspace/pp4-yoomoov/documentation/readme/feature_van_search.png">
  - <img src="/workspace/pp4-yoomoov/documentation/readme/feature_van_detail.png">
  - <img src="/workspace/pp4-yoomoov/documentation/readme/feature_dashboard.png">
  - <img src="/workspace/pp4-yoomoov/documentation/readme/feature_booking.png">
  - <img src="/workspace/pp4-yoomoov/documentation/readme/feature_feedback.png">

2. UX features include:
  - Ability for users to leave feedback after a booking has been completed.
  - Status of Bookings including Pending, Approved and Completed that is controlled by the administrator.
  -  <img src="/workspace/pp4-yoomoov/documentation/readme/uxfeat_leave_feedback.png">
  - Status of feedback prevents publishing until approved.
  -  <img src="/workspace/pp4-yoomoov/documentation/readme/uxfeat_feedback_status.png">
  - Pagination to ensure listings are organised
  -  <img src="/workspace/pp4-yoomoov/documentation/readme/uxfeat_pagination.png">
  - Back to top button for easy site navigation.
  - Social media links.
  -  <img src="/workspace/pp4-yoomoov/documentation/readme/uxfeat_back_to_top.png">
  - Onscreen alert and success messages appear.
  - Register, Login and Logout forms for streamlined user authentication.
  -  <img src="/workspace/pp4-yoomoov/documentation/readme/uxfeat_login_page.png">
  - Email notifications sent to both user and administrator.
  - Favicon included for site identification.
  -  <img src="/workspace/pp4-yoomoov/documentation/readme/uxfeat_favicon.png">
  - Breadcrumb navigation.
  - <img src="/workspace/pp4-yoomoov/documentation/readme/uxfeat_breadcrumbs.png">
  - Dynamic user navigation.
  - <img src="/workspace/pp4-yoomoov/documentation/readme/uxfeat_dynamic_nav.png">
  - <img src="/workspace/pp4-yoomoov/documentation/readme/uxfeat_dynamic_nav_user.png">
  - Custom branding on the administration area.
  <img src="/workspace/pp4-yoomoov/documentation/readme/uxfeat_custom_admin.png">


## VALIDATION
Various validation methods have been incorporated:
 1. Onscreen Confirmation, when logging out, updating or deleting a booking.
 - <img src="/workspace/pp4-yoomoov/documentation/readme/confirmation_message.png">
 2. Onscreen Success / Error after creating, editing, deleting, logging in or out.
 - <img src="/workspace/pp4-yoomoov/documentation/readme/error_alert.png">
 3. Date validation to prevent booking a past date.
 - <img src="/workspace/pp4-yoomoov/documentation/readme/validate_past_dates.png">
 4. Form validation to ensure fields are completed where required or the correct format is needed such as for email addresses.

## TECH STACK
The site has been built with the following tech and tools:
1. HTML5.
2. CSS.
3. JavaScript.
4. Python.
5. Django - database framework.
6. Jinja - HTML logic rendering for dynamic content.
7. ElephantSQL - database hosting.
8. Cloudinary - media hosting.
9. Bootstrap 4.
10. JQuery.
11. GitHub Projects - agile management, kanban, roadmap and milestones.
12. GitHub Repo - code storage.
13. Git - version control.
14. GitPod & VS Code - IDE.
15. Heroku - live site hosting.

### Tools used
- [Image resizer](https://www.reduceimages.com/).
- [Canva Artwork](https://www.canva.com/).
- [Lucid Chart](https://lucid.app/) - schema and flow diagrams.
- [Favicon generator](https://favicon.io/favicon-converter/).
- [Responsive Image generator](https://ui.dev/amiresponsive).
- [Browserstack Browser Compatability](https://www.browserstack.com/).


## MODULES & LIBRARIES
   * font-awesome - icons.
   * bootstrap-made - HTML and CSS templates.
   * allauth - sign-up and login.
   * cripsy forms - imporved form styling and validation.
   * django.core.mail - sending email.
   * django.messages - success and alert bootstrap messages.
   * django.core.paginator - pagination.
   * datetime - handling date and time fields.


## TESTING
FOR DETAILED TEST REPORTS AND RESULTS PLEASE [VIEW THEM HERE:](/workspace/pp4-yoomoov/TESTING.md).

  ### Tests performed
  The site was thoroughly tested during development with each feature tested before committing to GitHub.  The testing regime included:
  1. Incremental testing.
  2. Early user observation test.
  3. Manual user story tests.
  4. HTML, CSS, JSHINT, PYLINT, Lighthouse.

  ### User Story Tests
  Each user story was tested manually according to a structured test sheet [VIEW IT HERE:](https://docs.google.com/spreadsheets/d/1qAa4tR_dnJwZkhPTGCNh35P1FVwFQc9NjnrO-5prhpI/edit#gid=0), with results being recorded and any failures rectified.

  ### Bugs resolved:
  The following bugs were recorded and rectified
  1. Colors were inconsistent on the website - CSS was updated according to the style guide.
  2. Breadrcumbs were missing on Contact and Delete page - code was added on these templates.
  3. The validation used to prevent creating a double booking on the same day, affected the Edit Booking function.  The clean method on the Booking form was modified to check and remove the current booking - allowing the same form to be used for creating and updating bookings.
  4. Emails were not sent in the development environment due to GitPod's security policy.  Email config was set to display in terminal for testing purposes.  Updated for production.
  5.  No dynamic username in nav bar when logged in - updated base.html with {{ user }}(dashboard).
  6. When testing for browser compatibility, there were numerous AnonymousUser errors on different browsers.  This was rectified by adding a login_required decorator on the dashboard view.


  ### Unresolved bugs:
  The following bugs have been noted and left:
  1. When creating a booking manually in the admin area, the administrator has to manually enter fields such as the van name, price, location and county, any of which could be incorrect due to human error.  While not a significant bug, this should be addressed in future iterations.
  2. Similar to the above when creating feedback the administrator could choose an incorrect booking number or van name by mistake.
  3. Similar to the above, an administrator could choose the incorrect county for a given city.
  4. The user can select a van in a city or county that has no vehicles, resulting in nothing displayed on the page.  While not a significant bug to prevent the site from being used, this would be an annoying UX which should be addressed on the next iteration.
  5. If a user tries to book the same van on the same day, the booking form modal closes with an error message.  The user would have to reenter their details and select a different date. While not a significant bug to prevent the site from being used, this would be an annoying UX which should be addressed on the next iteration.

  ### Improvements and future developments:
  The following items have been identified for future development:
  1. Create model for services so they can be updated through the admin panel - enhances administrator experience.
  2. Create model for locations so they can be updated through the admin panel - enhances administrator experience.
  3. Dynamic Dependant Filter for Van Name, Size, location and County in the booking form and Van Finder form - enhances user experience by not allowing selections that have no content.
  4. Dynamic Date selector on Booking Form where dates are shown as unavailable - enhances user experience.
  5. Enhance User model to allow a profile section on User dashboard to capture first name, last name and phone number - enhances User booking experience.
  6. Configure Social account sign-on - enhances user login experience.
  7. Configure Password reset - enhances user login experience.
  8. Create Filters and Folders for the Dashboard so bookings can be archived rather than deleted.
  9. Add a dynamic meta description for each page - enhances SEO.

## DEPLOYMENT
I deployed the site right from project inception using this helpful [Code Institute Django Deployment Guide](https://docs.google.com/document/d/1g6xnseQfzFNZdp_gx_YOXkxcMMgZaQh7R3oyTFcOM_w/edit?usp=sharing).
1. Once the project was deployed, development took place on GitPod using a local server found by typing "python3 manage.py runserver".
2. On completion of development, the following steps took place to deploy the final site to Heroku.
  -



## FORKING & CLONING INSTRUCTIONS
You can create a copy of a GitHub Repository without affecting the original by forking it. Here's a step-by-step guide:
1. Log into GitHub or sign up for an account.
2. Go to the [YooMoov Repository URL](https://github.com/rstan-dev/pp4-yoomoov).
3. Click "Fork" on the right side of the repository's page to create a copy in your own repository.

To clone a copy:
1. Go to the [YooMoov Repository URL](https://github.com/rstan-dev/pp4-yoomoov).
2. Click the green code button, then the arrow, and select the "clone by https" option to copy the URL.
3. Open your preferred code editor and navigate to the directory where you want to clone the repository.
4. Type 'git clone', paste the copied URL, and press enter. The repository will then be cloned to your machine.


## CREDITS:

  ### Code
  * All Python logic was written and developed specifically for this project.
  * Main Site HTML & CSS templates were adapted from a bootstrap template called [Lumia](https://bootstrapmade.com/demo/Lumia/) from bootsrapmade.com.
  * Login templates were adapted from allauth using bootstrap css.
  * Inspiration and solutions for the site came from:
    - Code Institue - [I Think Therefore I Blog](https://github.com/rstan-dev/rs-django-blog).
    -  Brad Traversy - [Traversy Media Python Django Dev to Deployment](https://www.traversymedia.com/Python-Django-Dev-To-Deployment).
    - Alan Bushell - [La Cocina del Diablo](https://github.com/Alan-Bushell/la-cocina-del-diablo).
    - Rashidat Adekoya - [Deask HQ](https://github.com/Shida18719/desk-hq).
    - Samar Ziadat - [Oishii Ramen](https://github.com/SamarZiadat/oishii-ramen).

  ### Resources
  I used the following resources to help develop features and functionality:
  1. [allauth](https://django-allauth.readthedocs.io/en/latest/).
  2. [messages](https://docs.djangoproject.com/en/4.2/ref/contrib/messages/).
  3. [alerts](https://getbootstrap.com/docs/4.0/components/alerts/).
  4. [save()](https://docs.djangoproject.com/en/4.2/ref/models/instances/#django.db.models.Model.save).
  5. [LoginRequiredMixin](https://stackoverflow.com/questions/47244036/using-django-login-required-mixin).
  6. [datepicker](https://colorlib.com/wp/template/calendar-14/).
  7. [Django CRUD Functions](https://www.youtube.com/watch?v=EX6Tt-ZW0so).
  8. [DateInput Widget](https://docs.djangoproject.com/en/3.2/ref/forms/widgets/).
  9. [clean_date_required()](https://docs.djangoproject.com/en/3.2/ref/forms/validation/#cleaning-a-specific-field-attribute).
  10. [queryset api](https://docs.djangoproject.com/en/3.2/ref/models/querysets/).
  11. [sending email](https://docs.djangoproject.com/en/4.2/topics/email/).

  ### Content
  * All van content was written specifically for this project.

  ### Media
  * Logo was custom designed for this project.
  * Cow icon - Royalty free from Canva Pro.
  * Van Services pics - Royalty free from Canva Pro.
  * Van on Location pics - Royalty free from Canva Pro.
  * Hero Image - [Bernard Foss:](https://www.pexels.com/photo/)
  * Icons - font awesome.

  ### Acknowledgements
  * Thanks to my original mentor Spencer Barriball for his initial assistance.

