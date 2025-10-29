from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
import os
from django.db import models
from django.conf import settings


class CustomUserCreationForm(UserCreationForm):
    Email = forms.EmailField(max_length=40, help_text="Required. Add a valid email address.")
    Mobile = forms.IntegerField(help_text="Required. Add a valid Mobile number.")

    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + ('Email',) + ('Mobile',) 


    def clean_mobile(self):
        mobile = str(self.cleaned_data.get('Mobile'))  # Convert to string
        if len(mobile) != 11:
            raise forms.ValidationError("The mobile number given should be 11 numbers long.")
        return mobile


    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['Email']
        user.mobile = self.cleaned_data['Mobile']
        if commit:
            user.save()
        return user
                                                    #brain book buddy boss?
    

class Change_N (forms.Form):
        New_number=forms.IntegerField(min_value=10000000, max_value=999999999)
        

class Change_Email (forms.Form):
        New_Email=forms.EmailField(max_length=60)

#class Add_Profile_Picture(forms.ModelForm):
 #   class Meta:
 #       model = Profile
 #       fields = ['update_profile_picture', 'owner']

  #  def save(self, commit=True):
   #     instance = super().save(commit=False)  # Get the instance, but don't save yet
    #    try:
     #       old_instance = Profile.objects.get(pk=instance.pk)
      #      # Check if the image has changed
       #     if 'update_profile_picture' in self.cleaned_data:
        #        new_image = self.cleaned_data['update_profile_picture']
         #       if old_instance.update_profile_picture != new_image:
          #          # Delete the old image if it's not the default one
           #         if old_instance.update_profile_picture and 'default.jpg' not in old_instance.update_profile_picture.name:
            #            old_image_path = old_instance.update_profile_picture.path
             #           if os.path.exists(old_image_path):
              #              os.remove(old_image_path)
        #except Profile.DoesNotExist:
         #   pass  # If it's a new object, no old image to delete

       # if commit:
        #    instance.save()
        #return instance
        
