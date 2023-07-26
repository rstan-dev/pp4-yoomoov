from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Booking, Feedback


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
        fields = ['van', 'title', 'comment', 'rating']




