from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
from mainlab.models import MyUser, Curriculum, Grade, Subject, Chapter, Activity, Project, Organizer, File, Link, Comment
#from django.contrib.auth import get_user_model
from django.conf import settings

import logging

@dajaxice_register
def siteLogin(request, email, password):
	dajax = Dajax()
	user = authenticate(email=email, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
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
	
	return dajax.json()

@dajaxice_register
def curFind(request, id, big):
	dajax = Dajax()
	
	curriculum = Curriculum.objects.get(pk=id)
	
	htmlStr = ""
	for g in curriculum.grade_set.filter(hasResource=True).order_by('number'):
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
	for s in grade.subject_set.filter(hasResource=True).order_by('title'):
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

#@dajaxice_register
def gradeResFind(request, id):
        dajax = Dajax()

        grade = Grade.objects.get(pk=id)

        htmlStr = ""
        for s in grade.subject_set.all():
                tempStr = "<li class='dropText' onClick='selSubject(%d, this)'> %s <" % (s.id, s.title)
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
def curricFind(request, id):
        dajax = Dajax()

        curriculum = Curriculum.objects.get(pk=id)

        htmlStr = "<option value='None'> None </option>"
        for g in curriculum.grade_set.order_by('number'):
                tempStr = "<option value='%d'> %s </option>" % (g.id, g.title)
                htmlStr += tempStr
	dajax.assign('#id_grade', 'innerHTML', '')
	dajax.assign('#id_grade','innerHTML',htmlStr)
	dajax.assign('#id_grade', 'disabled', '')
		
        return dajax.json()

@dajaxice_register
def gradeFind(request, id):
        dajax = Dajax()

        grade = Grade.objects.get(pk=id)

	htmlStr = "<option value='None'> None </option>"
        for s in grade.subject_set.order_by('title'):
                tempStr = "<option value='%d'> %s </option>" % (s.id, s.title)
                htmlStr += tempStr
        dajax.assign('#id_subject','innerHTML','')
        dajax.assign('#id_subject','innerHTML',htmlStr)
        dajax.assign('#id_subject', 'disabled', '')
 
	return dajax.json()


@dajaxice_register
def subjectFind(request, id):
        dajax = Dajax()

        subject = Subject.objects.get(pk=id)

        htmlStr = "<option value='None'> None </option>"
        for c in subject.chapter_set.order_by('number'):
                tempStr = "<option value='%d'> %s </option>" % (c.id, c.title)
                htmlStr += tempStr
        dajax.assign('#id_chapter','innerHTML','')
        dajax.assign('#id_chapter','innerHTML',htmlStr)
	dajax.assign('#id_chapter', 'disabled', '')

        return dajax.json()



@dajaxice_register
def addComment(request, type, id, comment):
	dajax = Dajax()
	
	if type == "a":
		resource = Activity.objects.get(pk=id)
	elif type == "p":
		resource = Project.objects.get(pk=id)

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
	
@dajaxice_register
def assignActManager(request, aid, mid):
	dajax = Dajax()
	
	manager = MyUser.objects.get(pk=mid)
	activity = Activity.objects.get(pk=aid)
	activity.manager = manager
	activity.save()
	
	return dajax.json()
	
@dajaxice_register
def assignProManager(request, pid, mid):
	dajax = Dajax()
	
	manager = MyUser.objects.get(pk=mid)
	project = Project.objects.get(pk=pid)
	project.manager = manager
	project.save()
	
	return dajax.json()
	
@dajaxice_register
def removeAtt(request, type, rid, fid):
	dajax = Dajax()
	if type == "a":
		resource = Activity.objects.get(pk=rid)
	elif type == "p":
		resource = Project.objects.get(pk=rid)
	file = File.objects.get(pk=fid)
	resource.files.remove(file)
	return dajax.json()
	
	
