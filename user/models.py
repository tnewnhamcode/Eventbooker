from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings

# Create your models here.

class users (AbstractUser):
    username=models.CharField(max_length=30, unique=True)
    USERNAME_FIELD = 'username'
    email=models.CharField(max_length=40)
    mobile=models.IntegerField(unique=True, default='00') #have to add a default because its an integer and they need shit for the tables already made coz they cant be blank for integers for some reason
    groups = models.ManyToManyField(  #defining relationship to imported model 'group' which means which group users belong to (different groups get different permissions), through a groups field
        Group,
        verbose_name=('groups'),  #what the user will see on the form
        blank=True,     #saying it doesnt need to be filled in  by them. tbh it shouldnt even be on there i think, idk
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="customuser_set",  # Unique related_name. related name being how to access all the users in the group from group.   group.customuser_set   (django auto puts the one with loads of stuff in into a set when you set up the relationship
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="customuser_permissions_set",  # Unique related_name. basically the default has been overidden, because the default would have just been users_set (modelname_set) which causes a clash unless you manually set it to different ones
        related_query_name="user",
    )

class Paymentinfo (models.Model):
    fake_card_number=models.IntegerField()
    fake_sort_code=models.IntegerField()
    fake_name_on_card=models.CharField(max_length=255)
    payer=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #should be onetoone coz only one instance of model needed, unless i add cards. same for other time i used foreign key

class Purchase_history_class(models.Model):
    purchaser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='purchase_history1')
    purchase_history = models.CharField(max_length=380)


#    update_profile_picture=models.ImageField(default='default.jpg', upload_to='profile_pics') #i think this is coz the database cant store the image, s oinstead stores refereences to the folder on your poota which stores it
 #   owner=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='profile1') #it still doesnt automatically infer that the owner field should be set to the user associated  with it on views.. just that the picture should go into this that instance of the profile table, and its this users table.. you gotta overide the form's save method to specify it (which is the method forms use to create a model instance and save to  it)  

    #should i make these uninque in case someone uses somelses card? and how about saving cards?
    
