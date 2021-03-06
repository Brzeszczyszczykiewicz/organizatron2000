from django.db import models
from django.urls import reverse


class Appeal(models.Model):
	auto_park 	 				=	models.CharField(max_length=50, default=None, null = True, blank=True)
	bsk_number  				=	models.CharField(max_length=50)
	appeal_num	 				=	models.IntegerField(default = None, unique=True)
	appeal_create_date  		=	models.DateField(default = None, null = True)	
	appeal_code  				=	models.CharField(max_length=50, default=None, null = True, blank=True)
	appeal_method  	 			=	models.CharField(max_length=50, default=None, null = True, blank=True)	
	appeal_owner_name  			=	models.CharField(max_length=50, default=None, null = True)
	appeal_owner_phone_number	= 	models.CharField(max_length=50, default=None, null = True, blank=True)	
	district  					=	models.CharField(max_length=50, default=None, null = True, blank=True)
	incident_date  				=	models.DateField(default = None, null = True, blank=True)
	incident_time  				=	models.DateField(default = None, null = True, blank=True)
	route_number  				=	models.IntegerField(default = None, null = True, blank=True)
	stop_name  					=	models.CharField(max_length=50, default=None, null = True, blank=True)
	route_direction  			=	models.CharField(max_length=50, default=None, null = True, blank=True)
	auto_number  				=	models.CharField(max_length=50, default=None, null = True, blank=True)
	answer_method	  			=	models.CharField(max_length=50, default=None, null = True, blank=True)
	answer  					=	models.TextField(max_length=1500, default=None, null = True, blank=True)
	accepted  					=	models.BooleanField(default = False)
	generated  					=	models.BooleanField(default = False)
	archivated 					=	models.BooleanField(default = False)

	def __str__(self):
		return self.bsk_number


