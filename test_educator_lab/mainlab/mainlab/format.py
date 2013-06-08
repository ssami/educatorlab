
#Formats all content submission emails

def FormatEmail(form, request):
	
	fromEmail = request.user.email
	fromPerson = request.user.name
	message = 'From:' + fromPerson + '\n' + 'Email: ' + fromEmail + '\n' + 'Curriculum: ' + form.cleaned_data['curriculum'] + '\n' + 'Grade: ' + form.cleaned_data['grade'] + '\n' + 'Goals:' + form.cleaned_data['goals'] + '\n' + 'Resource: ' + form.cleaned_data['resource']

	
	
	return message
