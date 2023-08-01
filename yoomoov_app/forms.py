from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Booking, Feedback
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit


class DateInput(forms.DateInput):
    input_type = 'date'

    def __init__(self, **kwargs):
        kwargs['attrs'] = {'min': timezone.localdate().isoformat()}
        super().__init__(**kwargs)


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['first_name', 'last_name', 'email', 'phone', 'van', 'date_required']
        widgets = {
            'date_required': DateInput(),
        }

    def clean_date_required(self):
        date_required = self.cleaned_data.get('date_required')
        if date_required and date_required < timezone.localdate():
            raise ValidationError("Please select a future date")
        return date_required


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['title', 'comment', 'rating']
        labels = {
            'title': 'Title (enter a short headline for your feedback)',
            'rating': 'Rating (choose between 1 for poor and 5 for excellent)',
        }


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'email',
            'message',
        )
