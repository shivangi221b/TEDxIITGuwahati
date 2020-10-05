# coding=utf-8
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, ButtonHolder, Div
from django import forms
from .models import Speaker
from django.utils.translation import ugettext_lazy as _


class SpeakerModelForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = {'nominee_name', 'nominator_name', 'email', 'nominee_about', 'talk_about', 'social_links',
                  'know_speaker_description', 'spoken_publicly_links'}
        labels = {
            'nominee_name': _('Nominee’s Name:'),
            'nominator_name': _('Your Name:'),
            'email': _('Your Email address:'),
            'nominee_about': _('Tell us briefly about the nominee. What’s their occupation? Any honors or '
                               'distinctions? Their recent work? Why are you recommending them?'),
            'talk_about': _('What might their TEDxIITGuwahati talk be about? Focus on the idea - this is the most '
                            'important section.'),
            'social_links': 'Please provide links to any social media handles/articles/web pages about the nominee:',
            'know_speaker_description': _('Do you know this person personally? (It’s okay if you do not) If yes, '
                                          'please describe how'),
            'spoken_publicly_links': _('Has this person spoken publicly before? If so, where? Please provide video '
                                       'links if possible'),
        }

    def __init__(self, *args, **kwargs):
        super(SpeakerModelForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Div(
                'nominee_name',
                'nominator_name',
                'email',
                'nominee_about',
                'talk_about',
                'social_links',
                'know_speaker_description',
                'spoken_publicly_links'
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn-success')
            ),
        )
