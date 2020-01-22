from django.db import models
from django.contrib.auth.models import User

# Credit: Corey Schafer https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=8

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #if user is deleted delete the profile but if the profile is deleted don't delete the user
    #1 2 1  a profile can only belong to 1 user
    image = models.ImageField(default='profile_default.jpg', upload_to='profile_images')#the directory profile pics will be uploaded to

    def __str__(self):
        return f'<Profile: {self.user.username}>' #corey doesn't use <> #don't know what user.username??


