"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'mainlab.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name

class CustomIndexDashboard(Dashboard):
	"""
	Custom index dashboard for www.
	"""
    
	def init_with_context(self, context):
		site_name = get_admin_site_name(context)
        
        
		# append an app list module for "Applications"
		self.children.append(modules.ModelList(
			title = "Classification",
			collapsible=True,
			column=1,
			models =('mainlab.models.Curriculum','mainlab.models.Grade','mainlab.models.Subject','mainlab.models.Chapter',),
		))
		
		
		# append an app list module for "Applications"
		self.children.append(modules.ModelList(
			title = "Teaching Material",
			collapsible=True,
			column=1,
			models =('mainlab.models.Activity','mainlab.models.Project','mainlab.models.Organizer'),
		))
		
		# append an app list module for "Applications"
		self.children.append(modules.ModelList(
			title = "Resources",
			collapsible=True,
			column=1,
			models =('mainlab.models.Link', 'mainlab.models.File', 'mainlab.models.Foldable', 'mainlab.models.GraphicOrganizer'),
		))
		
		# # append an app list module for "Applications"
		
		# self.children.append(modules.Group(
			# title="My group",
			# column=1,
			# collapsible=True,
			# children=[
				# modules.AppList(
					# title='Administration',
					# models=('django.contrib.*',)
				# ),
			# ]
		# ))
		
		self.children.append(modules.ModelList(
			title = "Users",
			collapsible=True,
			column=1,
			models =('mainlab.models.MyUser','mainlab.models.Comment',),
		))
		
		self.children.append(modules.ModelList(
			title = "Ratings",
			collapsible=True,
			column=1,
			models =('djangoratings.models.Vote','djangoratings.models.Score',),
		))
        
		
        # append a recent actions module
		self.children.append(modules.RecentActions(
			_('Recent Actions'),
			limit=5,
			collapsible=False,
			column=3,
		))


