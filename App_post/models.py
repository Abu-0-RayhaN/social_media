from django.db import models
from django.contrib.auth.models import User
class Posts(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post')
    image= models.ImageField(upload_to='post_images',blank=False)
    caption=models.CharField(max_length=264,blank=True)
    upload_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering =['-upload_date']
    def __str__(self):
        return self.caption+'@'+str(self.author)

class Like(models.Model):
    post=models.ForeignKey(Posts,on_delete=models.CASCADE,related_name='like_post')
    user= models.ForeignKey(User,on_delete=models.CASCADE,related_name='liker')
    date_created= models.DateTimeField(auto_now_add=True)
    def __st__(self):
        return str(self.user)+' liked '+str(self.post)

class Follow(models.Model):
    follower=models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower')
    following= models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')
    created_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.following)+' being followed by '+str(self.follower)