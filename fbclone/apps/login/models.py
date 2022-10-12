from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
	title=models.CharField(max_length=200)
	image =models.ImageField(upload_to ='images/')
	author =models.ForeignKey(User,on_delete= models.CASCADE,blank=True,related_name='author')
	description=models.TextField()
	updated_at=models.DateTimeField(auto_now= True)
	created_at=models.DateTimeField(auto_now_add=True)
	likes=models.ManyToManyField(User,blank=True, related_name='likes')
	def __str__(self):
		return self.title
	def likeuser(self):
		return ",".join(str(i) for i in self.likes.all())
	def likeusers(self):
		return self.likes.all().count()   
	

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)
class Like(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default="Like", max_length=50)
    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"


class Comment(models.Model): 
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='usercomments')
    body = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    def __str__(self):
    	return self.body
    # class Meta:
    #     ordering = ['-created']
    
   