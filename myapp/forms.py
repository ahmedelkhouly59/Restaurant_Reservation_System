from .models import Booking,Rating,Reporting,Cancel
from .widgets import DatePickerInput
from django.forms import ModelForm

class BookingForm(ModelForm):
    class Meta:
        model=Booking    
        fields='__all__'
        widgets={
            'date' : DatePickerInput(),
        }
        labels = {
            'bill' : '',
        }

class ReportingForm(ModelForm):
    class Meta:
        model=Reporting
        fields='__all__'


class RatingForm(ModelForm):
    class Meta:
        model=Rating
        fields='__all__'

class CancelForm(ModelForm):
    class Meta:
        model=Cancel
        fields='__all__'



