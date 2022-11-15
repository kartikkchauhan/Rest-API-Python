from django.db import models

class CompanyDetails(models.Model):
	company_name=models.CharField(max_length=100, null=False, blank=False)
	company_abn=models.CharField(max_length=100, unique=True, null=False, blank=False)
	intersected=models.IntegerField(default=0)
	contacted=models.IntegerField(default=0)
	data_from=models.CharField(max_length=100, null=False, blank=False)

	def __str__(self):
		return f"{self.company_abn} - {self.company_name}"

class KinawayData(models.Model):
	name=models.CharField(max_length=100, null=False, blank=False)
	address=models.CharField(max_length=1000, null=True, blank=True)
	contact_no=models.CharField(max_length=1000, null=True, blank=True)
	main_contact=models.CharField(max_length=1000, null=True, blank=True)
	operating_region=models.CharField(max_length=1000, null=True, blank=True)
	company_abn=models.CharField(max_length=100, unique=True, null=False, blank=False)
	email=models.CharField(max_length=100, null=True, blank=True)
	website=models.CharField(max_length=100, null=True, blank=True)
	service_type=models.CharField(max_length=1000, null=True, blank=True)
	description=models.CharField(max_length=2000, null=True, blank=True)

	def __str__(self):
		return f"{self.company_abn} - {self.name}"

class BbfData(models.Model):
	name=models.CharField(max_length=100, null=False, blank=False)
	address=models.CharField(max_length=1000, null=True, blank=True)
	company_abn=models.CharField(max_length=100, unique=True, null=False, blank=False)
	summary=models.CharField(max_length=4000, null=True, blank=True)
	products_services=models.CharField(max_length=4000, null=True, blank=True)

	def __str__(self):
		return f"{self.company_abn} - {self.name}"