from django import forms
from django.forms.util import ErrorList

from tinymce.widgets import TinyMCE

from mainlab.models import Curriculum, Grade, Subject, Chapter, Activity

class CurrModelChoiceField(forms.ModelChoiceField):
	widget = forms.Select(attrs={
			'onchange':'selectCurric()',
		})
	
class GradeModelChoiceField(forms.ModelChoiceField):
        widget = forms.Select(attrs={
                        'onchange':'selectGrade()',
                })

class SubjectModelChoiceField(forms.ModelChoiceField):
        widget = forms.Select(attrs={
                        'onchange':'selectSubject()',
                })


class SubmitResourceForm(forms.Form):

	TYPE = (('Activity','Activity'), ('Project','Project'))
	resourceType = forms.ChoiceField(choices=TYPE)
	curriculum = CurrModelChoiceField(queryset=Curriculum.objects.all(), empty_label="None")
	grade = GradeModelChoiceField(queryset=Grade.objects.all(), empty_label="None")
    	subject = SubjectModelChoiceField(queryset=Subject.objects.all(), empty_label="None")
	chapter = forms.ModelChoiceField(queryset=Chapter.objects.all(), empty_label="None")
    	goals = forms.CharField(widget=TinyMCE(attrs={'rows':1, 'cols':20, 'class':'textarea span8'}))
	title = forms.CharField(widget=forms.TextInput)
	materials = forms.CharField(widget=TinyMCE(attrs={'rows':1, 'cols':20, 'class':'textarea span8'}))
	lesson = forms.CharField(widget=TinyMCE(attrs={'rows':6, 'cols':50, 'class':'textarea span8'}))
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
