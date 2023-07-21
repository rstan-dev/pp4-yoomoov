from django import forms
from. models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'van_id',
            'date_required',
        ]

    def __init__(self, *args, **kwargs):
        super().__init(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['van_id'].widget.attrs.update({'class': 'form-control'})
        self.fields['date_required'].widget.attrs.update({'class': 'form-control'})
