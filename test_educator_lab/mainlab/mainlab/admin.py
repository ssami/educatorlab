from mainlab.models import MyUser, Curriculum, Grade, Subject, Chapter, Activity, Project, File, Comment
from django.contrib import admin

# Tabular Inlines
class GradeInline(admin.TabularInline):
    model = Grade

class SubjectInline(admin.TabularInline):
    model = Subject

class ChapterInline(admin.TabularInline):
    model = Chapter

class ActivityInline(admin.TabularInline):
    model = Activity.chapters.through
	
class ProjectInline(admin.TabularInline):
    model = Project.chapters.through
	
class FileActivityInline(admin.TabularInline):
    model = Activity.files.through
	
class FileProjectInline(admin.TabularInline):
    model = Project.files.through

	
# Model Admins
	
class CurriculumAdmin(admin.ModelAdmin):
	inlines = [
        GradeInline,
	]
	search_fields = ('title',)

class GradeAdmin(admin.ModelAdmin):
	inlines = [
        SubjectInline,
	]
	list_display = ('title', 'Curriculum')
	search_fields = ('title', 'Curriculum__title')
class SubjectAdmin(admin.ModelAdmin):
	inlines = [
        ChapterInline,
	]
	list_display = ('title', 'grade', 'curriculum_name')
	raw_id_fields = ("grade",)
	related_lookup_fields = {
        'fk': ['grade'],
	}
	search_fields = ['title', 'grade__title', 'grade__Curriculum__title']
class ChapterAdmin(admin.ModelAdmin):
	inlines = [
        ActivityInline, ProjectInline,
	]
	list_display = ('title', 'subject', 'grade_name', 'curriculum_name')
	raw_id_fields = ("subject",)
	related_lookup_fields = {
        'fk': ['subject'],
	}
	search_fields = ['title', 'subject__title', 'subject__grade__title', 'subject__grade__Curriculum__title']


class ActivityAdmin(admin.ModelAdmin):
	readonly_fields=('timeCreated','timeModified',)
	list_display = ('title', 'timeCreated', 'timeModified',)
	search_fields = ('title',)
	filter_horizontal = ('chapters','files',)
	
class ProjectAdmin(admin.ModelAdmin):
	readonly_fields=('timeCreated','timeModified',)
	list_display = ('title', 'timeCreated', 'timeModified',)
	search_fields = ('title',)
	filter_horizontal = ('chapters','files',)


class FileAdmin(admin.ModelAdmin):
	search_fields = ('title',)
	inlines = [
        FileActivityInline, FileProjectInline,
	]
	

# Registering Admin for Models
	
admin.site.register(Curriculum, CurriculumAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Subject, SubjectAdmin)


admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Project, ProjectAdmin)

admin.site.register(File, FileAdmin)

admin.site.register(MyUser)
admin.site.register(Comment)
