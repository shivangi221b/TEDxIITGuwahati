from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import Attendee


class AttendeeModelForm(forms.ModelForm):
    class Meta:
        model = Attendee
        fields = {'name', 'email', 'phone'}

    def __init__(self, *args, **kwargs):
        super(AttendeeModelForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'name',
            'email',
            'phone',
            Submit('submit', 'Submit', css_class='btn-success')
        )
