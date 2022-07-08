from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
from django.core.files.storage import FileSystemStorage
from PIL import Image as PILImage

class Account(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	plan = models.ForeignKey('Plan',on_delete=models.PROTECT)

	def __str__(self):
		return self.user.username + " on plan: " + self.plan.name

class ThumbnailSize(models.Model):
	name=models.CharField(max_length=100)
	height=models.PositiveSmallIntegerField(default=200)

	def __str__(self):
		return self.name

class Plan(models.Model):
	name=models.CharField(max_length=100)
	description=models.TextField()
	has_original_link=models.BooleanField(default=False)
	has_temporal_link=models.BooleanField()
	thumbnail_size=models.ManyToManyField(ThumbnailSize)

	def __str__(self):
		return self.name 

class Image(models.Model):
	originalimage=models.ImageField(upload_to ='uploads/',validators=[FileExtensionValidator(['png','jpg','jpeg'],"invalid file type")])
	author=models.ForeignKey(Account,on_delete=models.CASCADE)

	def save(self,*args,**kwargs):
		super().save(*args,**kwargs)
		#Also save all thumbnails
		planname=Account.objects.get(user=self.author.user).plan
		plan=Plan.objects.get(name=planname)
		for thumbs in plan.thumbnail_size.all():
			size=thumbs.height,thumbs.height
			thumbnail=PILImage.open(self.originalimage).thumbnail(size)
			thumbnailfile=Thumbnail.objects.create(image=self,thumbnail_size=thumbs,thumbnail_image=thumbnail,author=self.author)
			thumbnailfile.save()

class Thumbnail(models.Model):
	image=models.ForeignKey(Image,on_delete=models.CASCADE)
	thumbnail_size=models.ForeignKey(ThumbnailSize,on_delete=models.CASCADE)
	thumbnail_image=models.ImageField(upload_to ='uploads/thumbnails/')
	author=models.ForeignKey(Account,on_delete=models.CASCADE)

class TemporalLink(models.Model):
	image=models.ForeignKey(Image,on_delete=models.CASCADE)
	author=models.ForeignKey(Account,on_delete=models.CASCADE)
	instance_created=models.DateTimeField(auto_now_add=True)
	duration=models.PositiveSmallIntegerField(default=300,validators=[MinValueValidator(300),MaxValueValidator(30000)])
