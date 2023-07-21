from django import forms
from .models import Booking, Van


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'van',
            'date_required',
        ]

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'type': 'email'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['van'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_required'].widget.attrs.update({'class': 'form-control'})
