from django import forms
from django.core import validators

# # como recive value Django lo identifca como validator
# def check_for_z(value):
#   if value[0].lower() != 'z':
#     raise forms.ValidationError('Name needs to start with Z')

class FormName(forms.Form):
  # name = forms.CharField(validators=[check_for_z])
  name = forms.CharField()
  email = forms.EmailField()
  verify_email = forms.EmailField(label='Enter your email again: ')
  text = forms.CharField(widget=forms.Textarea)

  # botcatcher = forms.CharField(required=False,
  #                              widget=forms.HiddenInput,
  #                              validators=[validators.MaxLengthValidator(0)])

  # Clean la forma entera
  def clean(self):
    all_clean_data = super().clean()
    email = all_clean_data['email']
    verify_email = all_clean_data['verify_email']

    if email != verify_email:
      raise forms.ValidationError('Maker sure emails match!')
