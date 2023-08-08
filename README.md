# Project Name - YooMoov

* [Link to Deployed Project](https://yoomoov-2cbb8d75e399.herokuapp.com/)

## CONTENTS
​
* [USER EXPERIENCE (UX)](#user-experience)
  * [Purpose & target audience](#purpose-and-target-audience)
  * [Goals](#goals)


* [PROJECT DESIGN](#project-design)
  * [Agile Approach](#agile-approach)
  * [Wireframes](#wireframes)
  * [User Stories](#user-stories)
  * [Logic](#logic)
  * [Color Scheme](#color-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [MVP](#mvp)


* [FEATURES](#features)

* [VALIDATION](#validation)

* [TECH STACK](#tech-stack)

* [MODULES](#modules-libraries)

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
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgements](#acknowledgements)



## USER EXPERIENCE

   ### Purpose and target audience

YooMov is a website for people and businesses looking to hire a van and a driver to move belongings from one location to another.  An administrator can create different types of van listings in different locations, which will be displayed to a user on the front end.

A website visitor can search for van types in various locations using a filter, they can open up a detail page about each van, they can read some reviews from other customers and they can book a date for the van, or they can send an email via a contact form if they have any questions.

The user can register and login to thir User Dashboard to view, edit or delete their bookings and they can also leave feedback for any bookings that have completed.

The administrator will receive an email notification any time there is a new booking or a change to a booking, prompting them to change the status of the booking, from pending to approved or to completed. They can also review and approve feedback before it is published live on the front end.

<img src="/workspace/pp4-yoomoov/documentation/readme/am_I_responsive_screenshot.png">

  ### Goals
The main objectives of this website are:
1. Build an easy-to-use and navigate, fully responsive booking website, with a clean interface.
2. Create user account functionality for the administrator to add van listings and manage bookings.
3. Create a personal dashboard for a customer to login, create, view, edit and delete bookings.
4. Create a feedback module so customers and admin can leave and approve feedback.
5. Configure email to notify the customer and the administrator of any changes to bookings.


## PROJECT DESIGN

  ### Agile Approach
  From the start the project was managed using GitHub Projects, using an agile approach.
  - The project goals were broken into epics, which were broken into user stories with accceptance criteria and individual tasks.
  - Each user story was allocated a certain number of story points based on a rough estimation of time to comeplete the work.
  - This allowed me to create a roadmap with milestone and target dates.
  - Each User Story was assigned a label accordng to the MoSCoW system so I could proritise the work.
<img src="/workspace/pp4-yoomoov/documentation/readme/github_projects.png">

  ### Wireframes  (created in [Balsamiq](https://balsamiq.cloud/))
   The initial wireframes were created to understand how the site would work, and this layout would drive User Stories, logic required and overall design artwork decisions.

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
    - As an admin user I can login into the Admin area so that I can manage website content.
  9. USERSTORY(#9): Customise admin area branding
    - As an admin user, I recognise the admin area has the same look and feel as the front end, for continuity purposes.
  10. USERSTORY(#10 ): User Registration
    - As a website user, I can register, log in and log out to view my dashboard.
  11. USERSTORY(# 11 ): Create Booking Model
    - As an admin user, I can create Booking details in the admin area so that I can take a booking over the phone.
  12. USERSTORY(#12 ): View Bookings on User Dashboard
    - As a logged in user, I can view any bookings I have made in a list on my Dashboard.
  13. USERSTORY(# 13): Create Booking on User Dashboard
    - As a logged-in user I can create a booking from a listing page, which will appear on the user's dashboard.
  14. USERSTORY(#14 ): Edit Booking on User Dashboard
    - As a logged in User, I can edit the booking details from the Dashboard so I can make any changes.
  15. USERSTORY(#15 ): Delete booking on user dashboard
    - As a logged in User, I can delete the booking details from the Dashboard.
  16. USERSTORY(#16): Create Feedback Model
    - As an admin user I can add and view Feedback details in the admin area and approve feedback for display on the relevant detail page.
  17. USERSTORY(# 17): Feedback option after booking completion
    - As a logged-in user who has made a booking, I can leave feedback using the feedback button next to the booking on my Dashboard.
  18. USERSTORY(#18 ): User can see their feedback on their dashboard
    - As a logged-in user, I can see all the feedback I have left for other bookings on my Dashboard.
  19. USERSTORY(#19): Send email to admin via contact form
    - As an admin, I can receive an email with the details from the contact form, so I can follow up with the customer.
  20. USERSTORY(#20 ): Send booking email notifications
    - As a user I can receive an email notification when the booking has been created, approved, updated or deleted, so I can manage the booking in my account.
  21. USERSTORY(#21 ): Admin to receive email notifications when feedback has been created
    - As an admin, I can receive an email notification when a user creates feedback.
  22. USERSTORY(# 22): User to receive email when feedback has been approved by admin
    - As a user, I can receive an email notification when my feedback has been approved.
  23. USERSTORY(#23 ): Onscreen notification when logged in or out
    - As a user, I will see a on-screen notification to let me know I have logged in or logged out.
  24. USERSTORY(#24): Menu Bar notification when user is logged in
    - As a logged in user, I will see a welcome message on the navbar and a logout link.
  25. USERSTORY(#25 ): Create user story tests
    - As a developer, all user story tests will pass, so that I can be certain the site functons as intended.
  26. USERSTORY(# 26): Test Html, CSS, JS, Python, Lighthouse
    - As a developer all code will pass through validation tools to identify any issues, errors or non-conformance.
  27. USERSTORY(# 27): Create Automatic unit tests
    - As a developer, I will write some automatic unit tests for the purposes of demonstrating competence.
  28. USERSTORY(# 28): Final deployment
    - As a developer I will ensure the final project is fully deployed to Heroku so that it matches the development project.
  29. USERSTORY(#29): Final Checks
    - As a developer, I will complete the final checks to ensure all criteria for the project have been met before submission.


  ### Logic
  The database schema and website logic was conceived and created using [Lucid](https://lucid.app/) as follows:

  1. Website Flow:
  <img src="/workspace/pp4-yoomoov/documentation/readme/yoomoov_site_logic.jpeg">

  2. Database Structure:
  <img src="/workspace/pp4-yoomoov/documentation/readme/yoomoov_db_schema.png">

  ### Color Scheme (created in [Canva](https://www.canva.com/))
  An orange color scheme was chosen because it's associated with optimism and energy, many brands use orange to convey a message of positivity. Many marketers use orange to get an audience excited about something becuase it is an attention-grabbing, warm color that really pops.

  I created the logo in Canva using royalty free images to cerate the distinct cow icon so there could be a play on the word YooMoov (You Moove) and chose a complimentary color pallette

   <img src="/workspace/pp4-yoomoov/documentation/readme/cow_icon.png">
   <img src="/workspace/pp4-yoomoov/documentation/readme/logo_yoomoov_orange1.jpg">
   <img src="/workspace/pp4-yoomoov/documentation/readme/color_pallette.png">

   ### Imagery
   Stock Images were sourced from:
   1. Hero Photo by [Bernard Foss:](https://www.pexels.com/photo/white-vans-parked-on-gray-concrete-road-4620555/)
   2. Stock van images by [Canva Pro](https://www.canva.com/)

  - I used Canva to build the initial designs, which was the basis for finding a suitable bootstrap template that could help me achieve the look and feel as easily as possible.
  <img src="/workspace/pp4-yoomoov/documentation/readme/canva_mockup_home.jpeg">
  <img src="/workspace/pp4-yoomoov/documentation/readme/canva_mockup_services.jpeg">
  <img src="/workspace/pp4-yoomoov/documentation/readme/canva_mockup_van_detail.jpeg">

   ### Typography
   I found a bootstrap layout called [Lumia](https://bootstrapmade.com/demo/Lumia/) from bootsrapmade.com which aligned closely with the layout I needed.  I kept the default Google font of Raleway and sans serif

   ### MVP
   * Using the GitHub project board I was able to prioritise user stories to give me an MVP incremetally.
   1. I built the front end as a static website first.
   2. I developed the django admin area so an administrator could manage the site
   3. I built User CRUD functionality next via their dashboard
   4. I configured on sreen notifications to give feedback to the user
   5. I built a feedback mechanism - first for the adminstrator, and then for front end users
   6. I configured email notifications to alert the user and the administrator


## FEATURES
   * The original design…


## VALIDATION
   * Various validation messages were used...
   * <img src="assets/documents/XXXX">

## TECH STACK
   *

## MODULES & LIBRARIES
   *

## TESTING

  ### Tests performed
  *

  ### User Story Tests
  *

  ### Bugs resolved:
  *

  ### Unresolved bugs:
  *

  ### Improvements and future developments:
  *

## DEPLOYMENT
The following steps were taken to deploy this site:
  *

## FORKING & CLONING INSTRUCTIONS
  *

## CREDITS:

  ### Code
  *

  ### Content
  *

  ### Media
  *

  ### Acknowledgements
  *

