from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import Speaker


class SpeakerModelForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = {'name', 'email', 'comment'}

    def __init__(self, *args, **kwargs):
        super(SpeakerModelForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'name',
            'email',
            'comment',
            Submit('submit', 'Submit', css_class='btn-success')
        )
