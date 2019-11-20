from django.db import models

# Create your models here.

class Students(models.Model):
	s_name = models.CharField(max_length=255, null=False)
	s_address = models.CharField(max_length=255, null=False)

	def __str__(self):
		return "{} - {}".format(self.s_name, self.s_address)
