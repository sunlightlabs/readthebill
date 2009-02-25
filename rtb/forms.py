from django import forms

AFFILIATION_CHOICES = (
    ('',''),
    ('c','Conservative'),
    ('i','Independent'),
    ('l','Liberal'),
    ('x','Private'),
)

class SignupForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=64)
    last_name = forms.CharField(label="Last name", max_length=64)
    email = forms.CharField(label="Your email", max_length=128)
    zipcode = forms.CharField(label="Your zipcode", max_length=5, widget=forms.TextInput(attrs={'size':'5','maxlength':'5'}))
    #affiliation = forms.ChoiceField(label="Your affiliation", choices=AFFILIATION_CHOICES)
    #message = forms.CharField(label="Your message", widget=forms.Textarea, required=False)