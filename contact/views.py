from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from yoomoov_app.models import Van
from yoomoov_app.forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from yoomoov_project.views import handler403, handler404, handler500


def contact(request, slug=None):
    """
    Renders Contact page form and submits user data via email to the
    administrator and to the user.

    Contact view is accessed directly via the Contact link in the menu bar,
    or via the van_detail page.

    If the contact form is accessed directly by the menu bar, the page
    redirects to the home page.

    If the contact form is accessed by the van_detail page, the email includes
    the van details and redirects the user back to the van_detail page
    """
    admin_user = User.objects.get(username='admin')
    van = None

    if slug is not None:
        van = get_object_or_404(Van, slug=slug)

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']

        subject = 'Van Enquiry'
        if van is not None:
            subject += ' ' + van.name

        send_mail(
            subject,
            'There has been an enquiry from: ' + name + ' from email: '
            + email + '. Their message is as follows: "' + message + '." '
            'An administrator will respond within 24 hours.',
            'yoomoovyoo@gmail.com',
            [email, admin_user.email],
            fail_silently=False
        )

        messages.success(request, "Your message has been sent! "
                                  "We will respond within 24 hours.")

        if van is not None:
            return redirect('van_detail', slug=slug)
        else:
            return redirect('home')

    else:
        contact_form = ContactForm()

    context = {
        'van': van,
        'contact_form': contact_form,
        'slug': slug
    }

    return render(request, 'contact/contact.html', context)
