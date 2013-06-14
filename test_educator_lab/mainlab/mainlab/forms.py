from django import forms
from django.forms.util import ErrorList

from tinymce.widgets import TinyMCE

class SubmitResourceForm(forms.Form):
    GRADES = (('0','None'), ('1', '1',), ('2', '2',), ('3', '3',), ('4', '4',), ('5', '5',), ('6', '6',), ('7', '7',), ('8', '8',), ('9', '9',), ('10', '10',), ('11', '11',), ('12', '12',))
    curriculum = forms.CharField(max_length=100)
    grade = forms.ChoiceField(choices=GRADES)
    subject = forms.CharField(max_length=100)
    chapter = forms.CharField(max_length=100)
    activityGoals = forms.CharField(widget=TinyMCE(attrs={'rows':1, 'cols':50, 'class':'textarea span10'}), required=False)
    resourceDetails = forms.CharField(widget=TinyMCE(attrs={'rows':6, 'cols':50, 'class':'textarea span10'}))
    attachment = forms.Field(widget=forms.FileInput, required=False)
    attachment = forms.Field(widget=forms.FileInput, required=False)


class SuggestForm(forms.Form):
	name = forms.CharField(max_length=100, required=False)
	email = forms.EmailField(max_length=100, required=False)
	suggestion = forms.CharField(widget=forms.Textarea(attrs={'rows':7, 'cols':50, 'class':'textarea span6'}))	

class DivErrorList(ErrorList): 
	def __unicode__(self): 
		return self.as_divs()
	def as_divs(self): 
		if not self: return u''
		return u'%s' % ''.join([u'%s' % e for e in self])


