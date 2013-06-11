from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
from mainlab.models import MyUser, Curriculum, Grade, Subject, Chapter, Activity, Project, Organizer, File, Link, Comment
#from django.contrib.auth import get_user_model
from django.conf import settings

@dajaxice_register
def siteLogin(request, email, password):
	dajax = Dajax()
	user = authenticate(email=email, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			#dajax.assign('#testRes','innerHTML',"Worked")
			dajax.script("location.reload();")
	else:
		dajax.assign('#loginResult','innerHTML',"Invalid email/password")
		dajax.script("$('#loginResult').css('display', 'block');")
		dajax.assign('#passwordInput','value',"")
	return dajax.json()
	
@dajaxice_register
def siteLogout(request):
	dajax = Dajax()
	logout(request)
	dajax.script("location.reload();")
	return dajax.json()
	
@dajaxice_register
def register(request, name, email, password):
	dajax = Dajax()
	
	existing = MyUser.objects.filter(email__iexact=email)
	if existing.exists():
		dajax.assign('#registerResult','innerHTML',"An account with that email address already exists.")
		dajax.script("$('#registerResult').css('display', 'block');")
	else:
		user = MyUser.objects.create_user(email=email, name=name, password=password)
		
		user = authenticate(email=email, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
	
		dajax.script("location.reload();")
	
	#dajax.assign('#registerResult','innerHTML',user)
	
	return dajax.json()

@dajaxice_register
def curFind(request, id, big):
	dajax = Dajax()
	
	curriculum = Curriculum.objects.get(pk=id)
	
	htmlStr = ""
	for g in curriculum.grade_set.all():
		tempStr = "<li class='dropText' onClick='selGrade(%d, this)'> %s </li>" % (g.id, g.title)
		htmlStr += tempStr
	
	#dajax.assign('#curSelection','innerHTML',curriculum.title)
	dajax.assign('#graSelection','innerHTML',"Select Grade")
	dajax.assign('#subSelection','innerHTML',"<span class='faded'>Select Subject</span>")
	dajax.assign('#drop2','innerHTML',htmlStr)
	dajax.assign('#drop3','innerHTML',"")
	
	if big:
		dajax.assign('#findButton','innerHTML',"<a class='btn btn-large btn-danger disabled'>Find Resources</a>")
	else:
		dajax.assign('#findButton','innerHTML',"<a class='btn btn-small btn-danger disabled'>Find Resources</a>")
	return dajax.json()
	
	
@dajaxice_register
def graFind(request, id, big):
	dajax = Dajax()
	
	grade = Grade.objects.get(pk=id)
	
	htmlStr = ""
	for s in grade.subject_set.all():
		tempStr = "<li class='dropText' onClick='selSubject(%d, this)'> %s </li>" % (s.id, s.title)
		htmlStr += tempStr

	#dajax.assign('#graSelection','innerHTML',grade.title)
	dajax.assign('#subSelection','innerHTML',"Select Subject")
	dajax.assign('#drop3','innerHTML',htmlStr)
	if big:
		dajax.assign('#findButton','innerHTML',"<a class='btn btn-large btn-danger disabled'>Find Resources</a>")
	else:
		dajax.assign('#findButton','innerHTML',"<a class='btn btn-small btn-danger disabled'>Find Resources</a>")
	return dajax.json()
	
	
@dajaxice_register
def subFind(request, id, big):
	dajax = Dajax()
	
	subject = Subject.objects.get(pk=id)
	
	#dajax.assign('#subSelection','innerHTML',subject.title)
	if big:
		htmlStr = "<a href='/subject/i=%s/ ' class='btn btn-large btn-danger'>Find Resources</a>" % (id)
		dajax.assign('#findButton','innerHTML',htmlStr)
	else:
		htmlStr = "<a href='/subject/i=%s/ ' class='btn btn-small btn-danger'>Find Resources</a>" % (id)
		dajax.assign('#findButton','innerHTML',htmlStr)
	
	return dajax.json()
	
# @dajaxice_register
# def putResources(request, id, type):
	# dajax = Dajax()	
	
	# if type == "a":
		# resource = Activity.objects.get(pk=id)
	# elif type == "p":
		# resource = Project.objects.get(pk=id)
	# elif type == "o":
		# resource = Organizer.objects.get(pk=id)
	# files = resource.files.all()
	# htmlStr = ""
	# for f in files:
		# tempStr = "<a class='attachment' target='_blank' href='%s'><img class='attImage' src='/media/images/%s.png'><div class='attText'>%s</div></a>" % (f.doc.url, f.extension(), f.title)
		# htmlStr += tempStr
	# dajax.assign('#resourceFooter','innerHTML',htmlStr)
	# return dajax.json()

@dajaxice_register
def addComment(request, type, id, comment):
	dajax = Dajax()
	
	if type == "a":
		resource = Activity.objects.get(pk=id)
	elif type == "p":
		resource = Project.objects.get(pk=id)
	elif type == "o":
		resource = Organizer.objects.get(pk=id)

	c = resource.comment_set.create(user=request.user, comment=comment)
	
	commentCode = '<li class="media"><div class="media-body"><h5 class="media-heading">'+c.user.name+'</h5>'+comment+'</div></li>'
	dajax.append('#commentsList','innerHTML',commentCode)
	
	noOfComments = resource.comment_set.count()
	if noOfComments == 1:
		dajax.assign('#noOfComments', 'innerHTML', '<h5>1 Comment</h5>')
	else:
		dajax.assign('#noOfComments', 'innerHTML', '<h5>' + str(noOfComments) + ' Comments</h5>')
		
	dajax.assign('#commentBox', 'value', '')

	return dajax.json()	

@dajaxice_register
def rateResource(request, type, id, rating):
	dajax = Dajax()
	
	if type == "a":
		resource = Activity.objects.get(pk=id)
	elif type == "p":
		resource = Project.objects.get(pk=id)
	elif type == "o":
		resource = Organizer.objects.get(pk=id)
	#resource.rating.add(rating, request.user, request.META['REMOTE_ADDR'], request.COOKIES)
	
	if request.user.is_authenticated():
		resource.rating.add(rating, request.user, request.META['REMOTE_ADDR'])
	else:
		resource.rating.add(rating, None, request.META['REMOTE_ADDR'])
	dajax.script("$('#starRead').raty('readOnly', false);")
	scriptStr = "$('#starRead').raty('score', " + str(resource.rating.get_real_rating()) + ");"
	dajax.script(scriptStr)
	dajax.script("$('#starRead').raty('readOnly', true);")
	dajax.script("$('#star').raty('readOnly', true);")
	dajax.assign('#numVotes','innerHTML',"("+str(resource.rating.votes)+")")
	
	return dajax.json()