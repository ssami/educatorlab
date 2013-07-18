from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import redirect

from django.views.decorators.csrf import csrf_exempt

from mainlab.models import MyUser, Draft, Curriculum, Grade, Subject, Chapter, Activity, Project, File
from format import FormatEmail, FormatSuggest
from forms import SuggestForm, SubmitResourceForm,  DivErrorList
#UploadFileForm


def base(context):								# function to handle code that is common to most views
	curricula = []
	for c in Curriculum.objects.filter(hasResource=True):
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
	return render_to_response(settings.INDEX_FILE,{},context)
	
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
	context['grades'] = curriculum.grade_set.filter(hasResource=True)
	return render_to_response('curriculum.html',{},context)	

	
def grade( request, id):
	context = RequestContext(request)
	context = base(context)
	
	grade = Grade.objects.get(pk=id)
	context['titleTag'] = grade.titleTag
	
	context['curriculum'] = grade.Curriculum
	context['curID'] = grade.Curriculum.id
	context['grade'] = grade.title
	context['subjects'] = grade.subject_set.filter(hasResource=True)
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
	context['chapters'] = subject.chapter_set.filter(hasResource=True).order_by('number')
	
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
		if a.publish:
			attributes = {}
			attributes['title'] = a.title
			attributes['id'] = a.id	
			attributes['starRate'] = a.rating.get_real_rating()
			attributes['votes'] = a.rating.votes
			activities.append(attributes)
	context['activities'] = activities
	
	projects = []
	for p in chapter.project_set.all():
		if p.publish:
			attributes = {}
			attributes['title'] = p.title
			attributes['id'] = p.id	
			attributes['starRate'] = p.rating.get_real_rating()
			attributes['votes'] = p.rating.votes
			projects.append(attributes)
	context['projects'] = projects
	
	return render_to_response('chapter.html',{},context)
	
def activity( request, id, cid ):
	context = RequestContext(request)
	context = base(context)
	
	activity = Activity.objects.get(pk=id)
	if not activity.publish:
		return render_to_response('noPermission.html', {}, context)
	
	context['titleTag'] = activity.titleTag
	
	context['starRate'] = activity.rating.get_real_rating()
	if request.user.is_authenticated():
		context['voteValue'] = activity.rating.get_rating_for_user(request.user, request.META['REMOTE_ADDR'])  
	else:
		context['voteValue'] = activity.rating.get_rating_for_user(None, request.META['REMOTE_ADDR'])
		
	context['files'] = activity.files.all()
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
		if a.publish and a != activity:											# To skip the current activity
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
	if not project.publish:
		return render_to_response('noPermission.html', {}, context)
	
	
	context['titleTag'] = project.titleTag
	
	context['starRate'] = project.rating.get_real_rating()
	if request.user.is_authenticated():
		context['voteValue'] = project.rating.get_rating_for_user(request.user, request.META['REMOTE_ADDR'])  
	else:
		context['voteValue'] = project.rating.get_rating_for_user(None, request.META['REMOTE_ADDR'])
	
	context['files'] = project.files.all()
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
		if p.publish and p != project:											# To skip the current project
			attributes = {}
			attributes['title'] = p.title
			attributes['id'] = p.id	
			projects.append(attributes)
	context['projects'] = projects

	return render_to_response('project.html',{'project':project},context)


def submit_resource(request):
	context = RequestContext(request)
	context = base(context)
        
	if not request.user.is_authenticated():
		return render_to_response('login.html', {}, context)
        
	if request.method == 'POST': 
		form = SubmitResourceForm(request.POST, error_class=DivErrorList)
		
		if 'save' in request.POST:
			try:
				d = request.user.draft
			except:
				d = Draft(user=request.user)
			
			d.resourceType = request.POST['resourceType']
			d.title = request.POST['title']
			d.lesson = request.POST['lesson']
			d.goals = request.POST['goals']
			d.materials = request.POST['materials']
			d.save()
				
			form = SubmitResourceForm(initial={'resourceType':d.resourceType, 'title':d.title, 'goals': d.goals, 'materials':d.materials, 'lesson':d.lesson}, error_class=DivErrorList)
			return render_to_response('submit_resource.html', {'message' : 'Your changes have been saved', 'submit_resource_form': form}, context)
		
		if form.is_valid():
			try:
				resourceType = form.cleaned_data['resourceType']
				if resourceType =="Activity":
					activity = Activity()
					activity.title = form.cleaned_data['title']
					activity.lesson = form.cleaned_data['lesson']
					activity.goals = form.cleaned_data['goals']
					activity.materials = form.cleaned_data['materials']
					activity.author = request.user
					activity.save()
					activity.chapters.add(form.cleaned_data['chapter'])
					if request.FILES:
						attachments = request.FILES.getlist('attachment')
					try:
						if attachments:
							for attach in attachments:
								file = File.objects.create(title=attach.name, doc=attach)
								activity.files.add(file)
								activity.save()
					except:
						activity.save()
                    
				else:
					project = Project()
					project.title = form.cleaned_data['title']
					project.instructions = form.cleaned_data['lesson']
					project.goals = form.cleaned_data['goals']
					project.materials = form.cleaned_data['materials']
					project.author = request.user
					project.save()
					project.chapters.add(form.cleaned_data['chapter'])
					if request.FILES:
						attachments = request.FILES.getlist('attachment')
					try:
						if attachments:
							for attach in attachments:
								file = File.objects.create(title=attach.name, doc=attach)
								project.files.add(file)
								project.save()
					except:
						project.save()

				form = SubmitResourceForm(error_class=DivErrorList)
				return render_to_response('submit_resource.html', {'message' : 'Thank you for your submission!', 'submit_resource_form': form}, context)
			except Exception as exp: 
				form = SubmitResourceForm(request.POST, error_class=DivErrorList)
				return render_to_response('submit_resource.html', {'message': exp, 'submit_resource_form':form}, context)
		else:
			form = SubmitResourceForm(request.POST, error_class=DivErrorList)
			return render_to_response('submit_resource.html', {'message' : 'Form data is invalid! Please try again', 'submit_resource_form' : form}, context)
            
	else:
		try:
			d = request.user.draft
			form = SubmitResourceForm(initial={'resourceType':d.resourceType, 'title':d.title, 'goals': d.goals, 'materials':d.materials, 'lesson':d.lesson}, error_class=DivErrorList)
		except:
			form = SubmitResourceForm(error_class=DivErrorList)
		return render_to_response('submit_resource.html', {'message' : 'We loaded your last saved resource', 'submit_resource_form': form}, context)
                   
	
def suggest(request):
	context = RequestContext(request)
	context = base(context)

	if request.method != 'POST':
		if request.user.is_authenticated():
			form = SuggestForm(initial={'name':request.user.name, 'email':request.user.email})
		else:
			form = SuggestForm()
		return render_to_response('suggest.html', {'suggest_form': form}, context)

	form = SuggestForm(request.POST, error_class=DivErrorList)
	if form.is_valid(): 
		try: 
			messageContent = FormatSuggest(form, request)
			mail = EmailMessage("Suggestion", messageContent, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
			mail.content_subtype = "html"
			mail.send()
			if request.user.is_authenticated():
				form = SuggestForm(initial={'name':request.user.name, 'email':request.user.email})
			else: 
				form = SuggestForm()
			return render_to_response('suggest.html', {'message' : 'Thank you for your feedback!', 'suggest_form': form}, context)
		except: 
			form = SuggestForm()
			return render_to_response('suggest.html', {'message': 'Something went wrong, please try again', 'suggest_form' : form}, context)

	else : 
		return render_to_response('suggest.html', {'message': 'Please check the form for errors and try again','suggest_form' : form}, context)

def managerAdmin(request):
	context = RequestContext(request)
	context = base(context)

	if not request.user.is_authenticated():
		return render_to_response('login.html', {}, context)
	if not request.user.is_admin:
		return render_to_response('noPermission.html', {}, context)
	
	activityList = Activity.objects.filter().order_by('timeCreated')
	pendingActivities = []
	publishedActivities = []
	for a in activityList:
		attributes = {}
		attributes['id'] = a.id
		attributes['title'] = a.title
		attributes['author'] = a.author
		attributes['manager'] = a.manager
		attributes['timeCreated'] = a.timeCreated
		
		subjects = ""
		grades = ""
		curricula = ""
		for c in a.chapters.all():
			subjects += c.subject.title
			grades += c.subject.grade.title
			curricula += c.subject.grade.Curriculum.title
		attributes['subjects'] = subjects
		attributes['grades'] = grades
		attributes['curricula'] = curricula
		if a.publish:
			publishedActivities.append(attributes)
		else:
			pendingActivities.append(attributes)
	context['pendingActivities'] = pendingActivities
	context['publishedActivities'] = publishedActivities
	
	projectList = Project.objects.filter().order_by('timeCreated')
	pendingProjects = []
	publishedProjects = []
	for p in projectList:
		attributes = {}
		attributes['id'] = p.id
		attributes['title'] = p.title
		attributes['author'] = p.author
		attributes['manager'] = p.manager
		attributes['timeCreated'] = p.timeCreated
		
		subjects = ""
		grades = ""
		curricula = ""
		for c in p.chapters.all():
			subjects += c.subject.title
			grades += c.subject.grade.title
			curricula += c.subject.grade.Curriculum.title
		attributes['subjects'] = subjects
		attributes['grades'] = grades
		attributes['curricula'] = curricula
		if p.publish:
			publishedProjects.append(attributes)
		else:
			pendingProjects.append(attributes)
	context['pendingProjects'] = pendingProjects
	context['publishedProjects'] = publishedProjects

	context['managers'] = MyUser.objects.filter(is_manager=True)
	
	return render_to_response('managerAdmin.html',{},context)
		
def manager(request):
	context = RequestContext(request)
	context = base(context)

	if not request.user.is_authenticated():
		return render_to_response('login.html', {}, context)
	if not request.user.is_manager:
		return render_to_response('noPermission.html', {}, context)
	
	activityList = Activity.objects.filter(manager=request.user).order_by('timeCreated')
	pendingActivities = []
	publishedActivities = []
	for a in activityList:
		attributes = {}
		attributes['id'] = a.id
		attributes['title'] = a.title
		if a.author:
			attributes['author'] = a.author.name
		attributes['timeCreated'] = a.timeCreated
		
		subjects = ""
		grades = ""
		curricula = ""
		for c in a.chapters.all():
			subjects += c.subject.title
			grades += c.subject.grade.title
			curricula += c.subject.grade.Curriculum.title
		attributes['subjects'] = subjects
		attributes['grades'] = grades
		attributes['curricula'] = curricula
		if a.publish:
			publishedActivities.append(attributes)
		else:
			pendingActivities.append(attributes)
	context['pendingActivities'] = pendingActivities
	context['publishedActivities'] = publishedActivities
	
	
	
	projectList = Project.objects.filter(manager=request.user).order_by('timeCreated')
	pendingProjects = []
	publishedProjects = []
	for p in projectList:
		attributes = {}
		attributes['id'] = p.id
		attributes['title'] = p.title
		if p.author:
			attributes['author'] = p.author.name
		attributes['timeCreated'] = p.timeCreated
		
		subjects = ""
		grades = ""
		curricula = ""
		for c in p.chapters.all():
			subjects += c.subject.title
			grades += c.subject.grade.title
			curricula += c.subject.grade.Curriculum.title
		attributes['subjects'] = subjects
		attributes['grades'] = grades
		attributes['curricula'] = curricula
		if p.publish:
			publishedProjects.append(attributes)
		else:
			pendingProjects.append(attributes)
	context['pendingProjects'] = pendingProjects
	context['publishedProjects'] = publishedProjects

	return render_to_response('manager.html',{},context)
	
def activityEdit( request, id ):
	context = RequestContext(request)
	context = base(context)
	
	if not request.user.is_authenticated():
		return render_to_response('login.html', {}, context)
	if not request.user.is_admin:
		if not request.user.is_manager:
			return render_to_response('noPermission.html', {}, context)
	
	activity = Activity.objects.get(pk=id)
			
	context['files'] = activity.files.all()
	
	chaptersList = activity.chapters.all()
	chaptersRes = ""
	subjectsRes = ""
	gradesRes = ""
	curriculaRes = ""
	
	for c in chaptersList:
		chaptersRes += c.title
		subjectsRes += c.subject.title
		gradesRes += c.subject.grade.title
		curriculaRes += c.subject.grade.Curriculum.title
	
	context['chaptersRes'] = chaptersRes
	context['subjectsRes'] = subjectsRes
	context['gradesRes'] = gradesRes
	context['curriculaRes'] = curriculaRes
	
	return render_to_response('activityEdit.html',{'activity':activity},context)
	
def projectEdit( request, id):
	context = RequestContext(request)
	context = base(context)
	
	if not request.user.is_authenticated():
		return render_to_response('login.html', {}, context)
	if not request.user.is_admin:
		if not request.user.is_manager:
			return render_to_response('noPermission.html', {}, context)
	
	project = Project.objects.get(pk=id)
	
	context['files'] = project.files.all()
	
	chaptersList = project.chapters.all()
	chaptersRes = ""
	subjectsRes = ""
	gradesRes = ""
	curriculaRes = ""
	
	for c in chaptersList:
		chaptersRes += c.title
		subjectsRes += c.subject.title
		gradesRes += c.subject.grade.title
		curriculaRes += c.subject.grade.Curriculum.title
	
	context['chaptersRes'] = chaptersRes
	context['subjectsRes'] = subjectsRes
	context['gradesRes'] = gradesRes
	context['curriculaRes'] = curriculaRes
	
	return render_to_response('projectEdit.html',{'project':project},context)
	
@csrf_exempt
def saveActivity(request):
	context = RequestContext(request)
	context = base(context)

	activity = Activity.objects.get(pk=request.POST['id'])
	
	activity.title = request.POST['title']
	activity.goals = request.POST['goals']
	activity.materials = request.POST['materials']
	activity.lesson = request.POST['lesson']
	activity.userModified = request.user
	activity.save()

	if request.FILES:
		attachments = request.FILES.getlist('attachment')
		try:
			if attachments:
				for attach in attachments: 
					file = File.objects.create(title=attach.name, doc=attach)
					activity.files.add(file)
					activity.save()
		except:
			activity.save()
	
	if 'publish' in request.POST:
		activity.publish = True
		activity.save()
		for c in activity.chapters.all():
			c.hasResource = True
			c.save()
			c.subject.hasResource = True
			c.subject.save()
			c.subject.grade.hasResource = True
			c.subject.grade.save()
			c.subject.grade.Curriculum.hasResource = True
			c.subject.grade.Curriculum.save()
			cid = c.id
		if activity.author:	
			context['email'] = activity.author.email
			context['personName'] = activity.author.name
			context['url'] = settings.SITE_URL + "activity/i=" + str(activity.id) + "&c=" + str(cid)
			if activity.manager:
				context['managerName'] = activity.manager.name
			context['publish'] = True
			return render_to_response('emailTemplate.html',{},context)
		
	if 'unpublish' in request.POST:
		activity.publish = False
		activity.save()
	
	return redirect('/manager/')
	
@csrf_exempt
def saveProject(request):
	context = RequestContext(request)
	context = base(context)

	project = Project.objects.get(pk=request.POST['id'])
	
	project.title = request.POST['title']
	project.goals = request.POST['goals']
	project.materials = request.POST['materials']
	project.instructions = request.POST['instructions']
	project.userModified = request.user
	project.save()
	
	if request.FILES:
		attachments = request.FILES.getlist('attachment')
		try:
			if attachments:
				for attach in attachments: 
					file = File.objects.create(title=attach.name, doc=attach)
					project.files.add(file)
					project.save()
		except:
			project.save()
	
	if 'publish' in request.POST:
		project.publish = True
		project.save()
		for c in project.chapters.all():
			c.hasResource = True
			c.save()
			c.subject.hasResource = True
			c.subject.save()
			c.subject.grade.hasResource = True
			c.subject.grade.save()
			c.subject.grade.Curriculum.hasResource = True
			c.subject.grade.Curriculum.save()
			cid = c.id
		if project.author:	
			context['email'] = project.author.email
			context['personName'] = project.author.name
			context['url'] = settings.SITE_URL + "project/i=" + str(project.id) + "&c=" + str(cid)
			if project.manager:
				context['managerName'] = project.manager.name
			context['publish'] = True
			return render_to_response('emailTemplate.html',{},context)
	
	if 'unpublish' in request.POST:
		project.publish = False
		project.save()
	
	return redirect('/manager/')
	
@csrf_exempt
def deleteActivity(request):
	context = RequestContext(request)
	context = base(context)

	activity = Activity.objects.get(pk=request.POST['id'])
	if activity.author:
		context['email'] = activity.author.email
		context['personName'] = activity.author.name
		if activity.manager:
			context['managerName'] = activity.manager.name
		context['publish'] = False
		activity.delete()
		return render_to_response('emailTemplate.html',{},context)
	else:
		activity.delete()
		return redirect('/manager/')

@csrf_exempt
def deleteProject(request):
	context = RequestContext(request)
	context = base(context)

	project = Project.objects.get(pk=request.POST['id'])
	if project.author:
		context['email'] = project.author.email
		context['personName'] = project.author.name
		if project.manager:
			context['managerName'] = project.manager.name
		context['publish'] = False
		project.delete()
		return render_to_response('emailTemplate.html',{},context)
	else:
		project.delete()
		return redirect('/manager/')
	
@csrf_exempt
def sendEmail(request):
	mail = EmailMessage(request.POST['subject'], request.POST['message'], settings.EMAIL_HOST_USER, [request.POST['email']])
	mail.content_subtype = "html"
	mail.send()
	return redirect('/manager/')
