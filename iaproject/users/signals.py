from django.db.models.signals import post_save #signal gets fired after an object gets saved
from django.contrib.auth.models import User
# import built in user model - this is the sender - sending the signal
from django.dispatch import receiver
# receiver - functio that gets the signal and performs some task
from .models import Profile

#credit: Corey https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=8

#want a user function to create profile every time create new user

@receiver(post_save, sender=User) #when a user is saved send this signal
#signal is received by the receiver
#receiver is the create profile function
def create_profile(sender, instance, created, **kwargs): #instance of the User
    if created: #if the user was created then..
        Profile.objects.create(user=instance) #create a profile object(record) with the user equal to...

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs): #don't need created.
    instance.profile.save() #save that users profile when user is saved
    