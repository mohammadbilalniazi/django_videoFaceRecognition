from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_video2.face import encode_face,handle_face_db

# Create your models here.

class Profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='photos',blank=True)
    bio=models.TextField()
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Profile of {self.user.username}'
    

@receiver(post_save,sender=Profile)
def create_image(sender,instance,created,**kwargs):
    if created or not created: # not created updated
        username=instance.user.username
        try:
            encodings=encode_face(instance.photo.path)
            if len(encodings)>0:
                encoding=encodings[0]
                data=handle_face_db("INSERT",encoding,username)
                print("username ",username,"encodings ",encodings,"data ",data," instance ",instance," sender ",sender)
        except:
            print("e ")