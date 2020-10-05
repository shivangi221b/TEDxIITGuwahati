from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from .models import Speaker


class SpeakerModelForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = {'nominator_name', 'nominee_name', 'email', 'nominee_about', 'talk_about', 'social_links',
                  'know_speaker_description', 'spoken_publicly_links'}

    def __init__(self, *args, **kwargs):
        super(SpeakerModelForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'nominator_name',
            'nominee_name',
            'email',
            'nominee_about',
            'talk_about',
            'social_links',
            'know_speaker_description',
            'spoken_publicly_links',
            Submit('submit', 'Submit', css_class='btn-success'),
        )
