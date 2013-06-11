from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import redirect


from mainlab.models import Curriculum, Grade, Subject, Chapter, Activity, Project, Organizer, File, Link, Foldable, GraphicOrganizer
from format import FormatEmail
from forms import EmailForm, DivErrorList

def base(context):								# function to handle code that is common to most views
	curricula = []
	for c in Curriculum.objects.all():
		attributes = {}
		attributes['title'] = c.title
		attributes['id'] = c.id		
		curricula.append(attributes)
	context['curricula'] = curricula
	context['site_url'] = settings.SITE_URL
	return context

def index(request):
	context = RequestContext(request)
	context = base(context)	
	return render_to_response('index.html',{},context)
	
def about(request):
	context = RequestContext(request)
	context = base(context)
	return render_to_response('about.html', {}, context)

def contrib(request):
	context = RequestContext(request)
	context = base(context)
	return render_to_response('contrib_form.html', {}, context)


def browse(request):
	context = RequestContext(request)
	context = base(context)
	return render_to_response('browse.html',{},context)
	
def curriculum( request, id):
	context = RequestContext(request)
	context = base(context)
	
	curriculum = Curriculum.objects.get(pk=id)
	context['titleTag'] = curriculum.titleTag
	context['curriculum'] = curriculum.title
	context['grades'] = curriculum.grade_set.all()
	return render_to_response('curriculum.html',{},context)	

	
def grade( request, id):
	context = RequestContext(request)
	context = base(context)
	
	grade = Grade.objects.get(pk=id)
	context['titleTag'] = grade.titleTag
	
	context['curriculum'] = grade.Curriculum
	context['curID'] = grade.Curriculum.id
	context['grade'] = grade.title
	context['subjects'] = grade.subject_set.all()
	return render_to_response('grade.html',{},context)	
	
def subject( request, id):
	context = RequestContext(request)
	context = base(context)
	
	subject = Subject.objects.get(pk=id)
	context['titleTag'] = subject.titleTag
	
	context['curriculum'] = subject.grade.Curriculum
	context['curID'] = subject.grade.Curriculum.id
	context['grade'] = subject.grade
	context['graID'] = subject.grade.id
	context['subject'] = subject.title
	context['chapters'] = subject.chapter_set.all()
	
	return render_to_response('subject.html',{},context)
	
def chapter( request, id ):
	context = RequestContext(request)
	context = base(context)
	
	chapter = Chapter.objects.get(pk=id)
	context['titleTag'] = chapter.titleTag
	
	context['curriculum'] = chapter.subject.grade.Curriculum
	context['curID'] = chapter.subject.grade.Curriculum.id
	context['grade'] = chapter.subject.grade
	context['graID'] = chapter.subject.grade.id
	context['subject'] = chapter.subject
	context['subID'] = chapter.subject.id
	context['chapter'] = chapter.title
	context['chaID'] = chapter.id
	
	activities = []
	for a in chapter.activity_set.all():
		attributes = {}
		attributes['title'] = a.title
		attributes['id'] = a.id	
		attributes['starRate'] = a.rating.get_real_rating()
		attributes['votes'] = a.rating.votes
		activities.append(attributes)
	context['activities'] = activities
	
	projects = []
	for p in chapter.project_set.all():
		attributes = {}
		attributes['title'] = p.title
		attributes['id'] = p.id	
		attributes['starRate'] = p.rating.get_real_rating()
		attributes['votes'] = p.rating.votes
		projects.append(attributes)
	context['projects'] = projects
	
	organizers = []
	for o in chapter.organizer_set.all():
		attributes = {}
		attributes['title'] = o.title
		attributes['id'] = o.id	
		attributes['starRate'] = o.rating.get_real_rating()
		attributes['votes'] = o.rating.votes
		organizers.append(attributes)
	context['organizers'] = organizers
	return render_to_response('chapter.html',{},context)
	
def activity( request, id, cid ):
	context = RequestContext(request)
	context = base(context)
	
	activity = Activity.objects.get(pk=id)
	context['titleTag'] = activity.titleTag
	
	context['starRate'] = activity.rating.get_real_rating()
	if request.user.is_authenticated():
		context['voteValue'] = activity.rating.get_rating_for_user(request.user, request.META['REMOTE_ADDR'])  
	else:
		context['voteValue'] = activity.rating.get_rating_for_user(None, request.META['REMOTE_ADDR'])
		
	context['files'] = activity.files.all()
	context['foldables'] = activity.foldables.all()
	context['graphicOrgs'] = activity.graphicOrgs.all()
	context['comments'] = activity.comment_set.all().order_by('timeCreated')
	context['noOfComments'] = activity.comment_set.count()
	
	chapter = Chapter.objects.get(pk=cid)							#Details for the breadcrumbs
	context['curriculum'] = chapter.subject.grade.Curriculum
	context['curID'] = chapter.subject.grade.Curriculum.id
	context['grade'] = chapter.subject.grade
	context['graID'] = chapter.subject.grade.id
	context['subject'] = chapter.subject
	context['subID'] = chapter.subject.id
	context['chapter'] = chapter.title
	context['chaID'] = chapter.id
	
	activities = []													# For easy navigation to other activities
	for a in chapter.activity_set.all():
		if a != activity:											# To skip the current activity
			attributes = {}
			attributes['title'] = a.title
			attributes['id'] = a.id	
			activities.append(attributes)
	context['activities'] = activities
	return render_to_response('activity.html',{'activity':activity},context)
	
def project( request, id, cid ):
	context = RequestContext(request)
	context = base(context)
	
	project = Project.objects.get(pk=id)
	context['titleTag'] = project.titleTag
	
	context['starRate'] = project.rating.get_real_rating()
	if request.user.is_authenticated():
		context['voteValue'] = project.rating.get_rating_for_user(request.user, request.META['REMOTE_ADDR'])  
	else:
		context['voteValue'] = project.rating.get_rating_for_user(None, request.META['REMOTE_ADDR'])
	
	context['files'] = project.files.all()
	context['foldables'] = project.foldables.all()
	context['graphicOrgs'] = project.graphicOrgs.all()
	context['comments'] = project.comment_set.all().order_by('timeCreated')
	context['noOfComments'] = project.comment_set.count()
	
	chapter = Chapter.objects.get(pk=cid)								#Details for the breadcrumbs
	context['curriculum'] = chapter.subject.grade.Curriculum
	context['curID'] = chapter.subject.grade.Curriculum.id
	context['grade'] = chapter.subject.grade
	context['graID'] = chapter.subject.grade.id
	context['subject'] = chapter.subject
	context['subID'] = chapter.subject.id
	context['chapter'] = chapter.title
	context['chaID'] = chapter.id
	
	projects = []													# For easy navigation to other projects
	for p in chapter.project_set.all():
		if p != project:											# To skip the current project
			attributes = {}
			attributes['title'] = p.title
			attributes['id'] = p.id	
			projects.append(attributes)
	context['projects'] = projects

	return render_to_response('project.html',{'project':project},context)
	
def organizer( request, id, cid ):
	context = RequestContext(request)
	context = base(context)
	
	organizer = Organizer.objects.get(pk=id)
	context['titleTag'] = organizer.titleTag
	
	context['starRate'] = organizer.rating.get_real_rating()
	if request.user.is_authenticated():
		context['voteValue'] = organizer.rating.get_rating_for_user(request.user, request.META['REMOTE_ADDR'])  
	else:
		context['voteValue'] = organizer.rating.get_rating_for_user(None, request.META['REMOTE_ADDR'])
	
	context['files'] = organizer.files.all()
	context['foldables'] = organizer.foldables.all()
	context['graphicOrgs'] = organizer.graphicOrgs.all()
	context['comments'] = organizer.comment_set.all().order_by('timeCreated')
	context['noOfComments'] = organizer.comment_set.count()
	
	chapter = Chapter.objects.get(pk=cid)							#Details for the breadcrumbs
	context['curriculum'] = chapter.subject.grade.Curriculum
	context['curID'] = chapter.subject.grade.Curriculum.id
	context['grade'] = chapter.subject.grade
	context['graID'] = chapter.subject.grade.id
	context['subject'] = chapter.subject
	context['subID'] = chapter.subject.id
	context['chapter'] = chapter.title
	context['chaID'] = chapter.id
	
	organizers = []													# For easy navigation to other organizers
	for o in chapter.organizer_set.all():
		if o != organizer:											# To skip the current organizer
			attributes = {}
			attributes['title'] = o.title
			attributes['id'] = o.id	
			organizers.append(attributes)
	context['organizers'] = organizers
	return render_to_response('organizer.html',{'organizer':organizer},context)

def foldable( request, id ):
	context = RequestContext(request)
	context = base(context)
	foldable = Foldable.objects.get(pk=id)
	context['titleTag'] = foldable.titleTag
	return render_to_response('foldable.html', {'foldable':foldable}, context)


def graphicOrganizer ( request, id ):
	context = RequestContext(request)
	context = base(context)
	graphOrg = GraphicOrganizer.objects.get(pk=id)
	context['titleTag'] = graphOrg.titleTag
	return render_to_response('graphicorganizer.html', {'graphOrg':graphOrg}, context)

def submit_resource(request):
	context = RequestContext(request)
	context = base(context)

	if not request.user.is_authenticated(): 
		return redirect('/')

	if request.method != 'POST':
		form = EmailForm()
		return render_to_response('submit_resource.html', {'email_form': form}, context)

	form = EmailForm(request.POST, request.FILES, error_class=DivErrorList)
	sendMailList = [settings.EMAIL_HOST_USER, 'vidsps@gmail.com']
	if form.is_valid():
		messageContent = FormatEmail(form, request)
		attachments = []
		if request.FILES:
			attachments = request.FILES.getlist('attachment')
		try:
			mail = EmailMessage("New resource submission", messageContent, settings.EMAIL_HOST_USER, sendMailList)
			if attachments:
				for attach in attachments: 
					mail.attach(attach.name, attach.read(), attach.content_type)
			mail.send()
			form = EmailForm()
			return render_to_response('submit_resource.html', {'message': 'Thanks for your submission!', 'email_form':form}, context)
		except:
			form = EmailForm()
			return render_to_response('submit_resource.html', {'message': 'Failed to send email, attachment might be too large or corrupt', 'email_form':form}, context)
	else :
		return render_to_response('submit_resource.html', {'email_form' : form}, context)
