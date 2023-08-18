from django.contrib import messages
from django.shortcuts import redirect


# Custom error handlers
def handler403(request, exception=None):
    """
    Error handler for 403 errors, redirects a user to the login page and
    displays an alert message to the user.
    """
    messages.error(request, '403 Error: Access Denied')
    return redirect('account_login')


def handler404(request, exception=None):
    """
    Error handler for 404 errors, redirects a user to the login page and
    displays an alert message to the user.
    """
    messages.error(request, '404 Error: Page Not Found')
    return redirect('account_login')


def handler500(request):
    """
    Error handler for 500 errors, redirects a user to the login page and
    displays an alert message to the user.
    """
    messages.error(request, '500 Error: Internal Server Error')
    return redirect('account_login')
