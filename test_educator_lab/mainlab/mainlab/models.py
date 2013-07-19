from django.db import models
from tinymce.models import HTMLField
import os
import datetime

from django.conf import settings
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

from djangoratings.fields import RatingField

class MyUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('Users must have an email address') 
        user = self.model(
            email=MyUserManager.normalize_email(email),
			name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, name, password):
        user = self.create_user(email,
            password=password,
			name=name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
 
 
class MyUser(AbstractBaseUser):
	email = models.EmailField(max_length=254, unique=True, db_index=True)
	name = models.CharField(max_length=255)
	
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
 
	is_manager = models.BooleanField(default=False)
 
	objects = MyUserManager()
 
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['name']
	
	def get_full_name(self):
		return self.name
	def get_short_name(self):
		return self.name
	def __unicode__(self):
		return self.name
	def has_perm(self, perm, obj=None):
		return True
	def has_module_perms(self, app_label):
		return True
	@property
	def is_staff(self):
		return self.is_admin
	class Meta:
		app_label = "mainlab"

class Curriculum(models.Model):
	title = models.CharField(max_length=200)
	titleTag = models.CharField(max_length=70, blank=True)
	hasResource = models.BooleanField(default=False)
	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name_plural = "curricula"	
	
class Grade(models.Model):
	Curriculum = models.ForeignKey(Curriculum)
	title = models.CharField(max_length=200)
	titleTag = models.CharField(max_length=70, blank=True)
	number = models.IntegerField()
	hasResource = models.BooleanField(default=False)
	def __unicode__(self):
		return self.title
	def related_label(self):
		return u"%s / %s" % (self.title, self.Curriculum)

class Subject(models.Model):
	grade = models.ForeignKey(Grade)
	title = models.CharField(max_length=200)
	titleTag = models.CharField(max_length=70, blank=True)
	hasResource = models.BooleanField(default=False)
	def __unicode__(self):
		return self.title
	def curriculum_name(self):
		return self.grade.Curriculum
	curriculum_name.short_description = 'Curriculum'
	def related_label(self):
		return u"%s / %s / %s" % (self.title, self.grade, self.grade.Curriculum)

class Chapter(models.Model):
	subject = models.ForeignKey(Subject)
	title = models.CharField(max_length=200)
	titleTag = models.CharField(max_length=70, blank=True)
	number = models.IntegerField()
	hasResource = models.BooleanField(default=False)
	def __unicode__(self):
		return self.title
	def grade_name(self):
		return self.subject.grade
	def curriculum_name(self):
		return self.subject.grade.Curriculum
	grade_name.short_description = 'Grade'
	curriculum_name.short_description = 'Curriculum'
	def related_label(self):
		return u"%s / %s / %s / %s" % (self.title, self.subject, self.subject.grade, self.subject.grade.Curriculum)
		
class File(models.Model):
	title = models.CharField(max_length=200)
	doc = models.FileField(upload_to='files/')
	description = HTMLField(blank=True)
	def __unicode__(self):
		return self.title
	def extension(self):
		name, extension = os.path.splitext(self.doc.name)
		if extension == '.pdf':
			return 'pdf'
		if extension == '.doc':
			return 'doc'
		return 'other'
	def delete(self, *args, **kwargs):
		storage, path = self.doc.storage, self.doc.path
		super(File, self).delete(*args, **kwargs)
		storage.delete(path)
		
class Activity(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
	manager = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='+')
	# contrib
	title = models.CharField(max_length=200)
	titleTag = models.CharField(max_length=70, blank=True)
	chapters = models.ManyToManyField(Chapter)
	# contrib
	goals = HTMLField()
	# contrib
	materials = HTMLField()
	# contrib
	lesson = HTMLField()
	# attachments: contrib
	files = models.ManyToManyField(File, blank=True)
	timeCreated = models.DateTimeField(editable=False)
	timeModified = models.DateTimeField(editable=False)
	userModified = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='+')
	rating = RatingField(range=5, allow_anonymous = True)
	
	publish = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.title
	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.timeCreated = datetime.datetime.today()
		self.timeModified = datetime.datetime.today()
		super(Activity, self).save(*args, **kwargs)
	class Meta:
		verbose_name_plural = "activities"
		
class Project(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
	manager = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='+')
	# contrib
	title = models.CharField(max_length=200)
	titleTag = models.CharField(max_length=70, blank=True)
	chapters = models.ManyToManyField(Chapter)
	# contrib
	goals = HTMLField()
	# contrib
	materials = HTMLField()
	# contrib
	instructions = HTMLField()
	# attachments: contrib
	files = models.ManyToManyField(File, blank=True)
	timeCreated = models.DateTimeField(editable=False)
	timeModified = models.DateTimeField(editable=False)
	userModified = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='+')
	
	rating = RatingField(range=5, allow_anonymous = True)
	
	publish = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.title
	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.timeCreated = datetime.datetime.today()
		self.timeModified = datetime.datetime.today()
		super(Project, self).save(*args, **kwargs)

class Worksheet(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
	manager = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='+')
	# contrib
	title = models.CharField(max_length=200)
	titleTag = models.CharField(max_length=70, blank=True)
	chapters = models.ManyToManyField(Chapter)
	# contrib
	description = HTMLField()
	# attachments: contrib
	files = models.ManyToManyField(File, blank=True)
	timeCreated = models.DateTimeField(editable=False)
	timeModified = models.DateTimeField(editable=False)
	userModified = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name='+')
	
	rating = RatingField(range=5, allow_anonymous = True)
	
	publish = models.BooleanField(default=False)
	
	def __unicode__(self):
		return self.title
	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.timeCreated = datetime.datetime.today()
		self.timeModified = datetime.datetime.today()
		super(Worksheet, self).save(*args, **kwargs)
		
# Comments Feature
class Comment(models.Model):
	activity = models.ForeignKey(Activity, null=True, blank=True)
	project = models.ForeignKey(Project, null=True, blank=True)
	#name = models.CharField(max_length=300)
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	comment = models.TextField()
	timeCreated = models.DateTimeField(editable=False)
	def __unicode__(self):
		return self.comment	
	def save(self, *args, **kwargs):
		''' On save, update timestamps '''
		if not self.id:
			self.timeCreated = datetime.datetime.today()
		super(Comment, self).save(*args, **kwargs)


class Draft(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
	resourceType = models.CharField(max_length=50, blank=True)
	title = models.CharField(max_length=200, blank=True)
	goals = HTMLField(blank=True)
	materials = HTMLField(blank=True)
	lesson = HTMLField(blank=True)