# PROJECT TEST DOC - YooMoov

## CONTENTS
* [TESTS PERFORMED](#tests-performed)
  * [Manual User Story Tests](#manual-user-story-tests)
  * [HTML](#html)
  * [CSS](#css)
  * [Lighthouse](#lighthouse)
  * [JSHINT](#jshint)
  * [PYLINT](#pylint)
  * [Browser Compatability](#browser-compatability)
  * [Automated Tests](#automated-tests)

  [Return to README.md](https://github.com/rstan-dev/pp4-yoomoov/blob/main/README.md)


## TESTS PERFORMED
  The site was thoroughly tested during development with each feature tested before committing to GitHub.  The testing regime included:
  1. Incremental testing
  2. Early user observation test
  3. Manual user story tests
  4. HTML, CSS, JSHINT, PYLINT, Lighthouse, PEP8
  5. Browser Compatability Tests
  6. Django Automated Tests

  ### Manual User Story Tests
  User story tests were conducted systematically, with any failing tests rectified.  A link to the Google Test Sheet [can be found here](https://docs.google.com/spreadsheets/d/1qAa4tR_dnJwZkhPTGCNh35P1FVwFQc9NjnrO-5prhpI/edit#gid=0)
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/user_test_manual_1.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/user_test_manual_2.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/user_test_manual_3.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/user_test_manual_4.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/user_test_manual_5.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main//documentation/testing/email_notifications_sent_recevied.png">

  * [Back to Contents](#contents)

  ### HTML
  All HTML pages were checked with [NU HTML Checker](https://validator.w3.org/nu/)
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/html_results_index.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/html_results_services.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/html_results_all_vans.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/html_results_van_filter.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/html_results_van_detail.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/html_results_dashboard.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/html_results_edit_booking.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/html_results_contact.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/html_results_delete_booking.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/html_results_leave_feedback.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/html_results_sign_up.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/html_results_login.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/html_results_on_screen_messages.png">

  * [Back to Contents](#contents)

  ### CSS
  All CSS pages were checked with [JIGSAW W3 VALIDATION](https://jigsaw.w3.org/css-validator/)
   - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/w3c_admin_css_results.png">
   - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/w3c_style_css_results.png">

   * [Back to Contents](#contents)

   ### JSHINT
  All JS pages were checked with [JSHINT](https://jshint.com/)
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/jshint_results.png">

  * [Back to Contents](#contents)

  ### PYLINT
  All Python pages were checked with [CODE INSTITUTES PYTHON LINTER](https://pep8ci.herokuapp.com/)
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/pylint_results_admin.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/pylint_results_apps.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/pylint_results_choices.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/pylint_results_context_processors.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/pylint_results_forms.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/pylint_results_models.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/pylint_results_project_urls.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/pylint_results_urls.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/pylint_results_views.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/pylint_test_contact.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/pylint_test_dashboard.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/pylint_test_errors.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/pylint_test_pages.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/pylint_contact_urls.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/pylint_contact_views.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/pylint_pages_urls.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/pylint_pages_views.png">

  * [Back to Contents](#contents)

  ### LIGHTHOUSE
  A lighthouse report was run on the site following deployment on the Home Page and Dashboard Page
  * The performance issues are related to image sizes and have been noted in the Future Enhancements
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/lighthouse_home.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/lighthouse_dashboard.png">

  * [Back to Contents](#contents)

  ### PEP8
  During development, any PEP8 problems in the IDE tab were addressed.  The following were left as they are in the settings and env.py files and relate to specific links or security keys.
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/pep8_results.png">

  * [Back to Contents](#contents)

  ### Browser Compatability
  - The production site was tested using [Browserstack](https://www.browserstack.com/) to ensure compatibility across various devices, and browsers including Mac, iPhone, Windows and Android, Chrome, Safari and Firefox on different pages chosen at random
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/browser_test_android_chrome.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/browser_test_iphone_chrome.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/browser_test_iphone_safari.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/browser_test_mac_safari.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/browser_test_windows_10_firefox.png">

  * [Back to Contents](#contents)

  ### Automated Tests
  A total of 27 automated tests were written using Django's Unittest framework.
  The tests can be run by entering "python3 manage.py test" into the terminal.
  Tests covered 94% of the code and included tests on:
  - Pages
  - Errors
  - Contact
  - Dashboard functions
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/unittest_coverage_report.png">
  - <img src="https://github.com/rstan-dev/pp4-yoomoov/blob/main/documentation/testing/unittest_results_with_warnings.png">

  There were 4 naive date warnings left which have been added to Future Enhancements list to be addressed.
  The site does make use of timezone functionality in the models.

  * [Back to Contents](#contents)
