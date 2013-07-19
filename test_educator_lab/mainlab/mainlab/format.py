
#Formats all content submission emails

def FormatEmail(form, request):
	fromEmail = request.user.email
	fromPerson = request.user.name
	message = 'From:' + fromPerson + '\n' + 'Email: ' + fromEmail + '\n' + 'Curriculum: ' + form.cleaned_data['curriculum'] + '\n' + 'Grade: ' + form.cleaned_data['grade'] + '\n' + 'Goals:' + form.cleaned_data['activityGoals'] + '\n' + 'Resource: ' + form.cleaned_data['resourceDetails']
	return message


def FormatSuggest(form, request):
	if request.user.is_authenticated():
		fromEmail = request.user.email
		fromPerson = request.user.name
	else:
		fromEmail = 'Unknown'
		fromPerson = 'Anonymous'
	message = 'From:' + fromPerson + '\n' + 'Email: ' + fromEmail + '\n' + 'Feedback:' + form.cleaned_data['suggestion'] + '\n'
	return message 
