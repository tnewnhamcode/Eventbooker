from django.shortcuts import render, redirect
from user.userforms.forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
import user.userforms.forms 

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  #*
            user.email = form.cleaned_data['Email'] #If email is  part of the form (it is). if not you could add it customise UserCreationForm (it's not in the default)
            user.mobile = form.cleaned_data['Mobile']
            user.save()
            return redirect('login')  # Redirect to login page. 
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration.html', {'form': form})

def login1(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)         #this  is different from the view function, its a utility function we a re importing (and django knwos not to muddle them up becasue they are used for different things apperently.)it offically logs in the user, meaning they can access locked parts of the site la.. form.get_user is required because it gets the user info that was authetnicated. (it gets the User instance that the form matches with). request has a session attribute, request is put as an argument (wait, is it?)because the session attribute has data like whether or not a user is logged in, this needs to be updated when auth_login() is called
            return redirect('home')
        else:
            return render(request, 'login.html', {'form': form})  # Render the form again with errors. errors come back attached to the form context now and you can access them in the html after an if conditional determining if there were errors. {%if form.password.errors%} and then <div class="error">{{ form.username.errors }}</div>`
    else:  # request.method == 'GET'
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})    #render usually takes request as the first argument, request is useful for loading a new page because it contains user info, which can be used like if user is autheniticated then say welcome adam or whatever
                                                                #can now say if user is authenticated (using html if statement) then display link to user page at top nav bar la)
def logout1(request):
    user=request.user
    logout(request)
    return redirect ('home')







def profile(request):
    #from user.userforms.forms import Add_Profile_Picture   #deferring the imort and waiting till function is called helps break circular import bug.. idk where the circular import is
    #if request.method == 'POST':
        #form = Add_Profile_Picture(request.POST, request.FILES, request.user)
        #specified related name which is needed for some reason)
#also last argument here apperently tells it to update the specified profile rather than make a new profile all together with the form.. or rather a new profile with just a picture on it. other forms add new instances to models sometimes. idk la
        #if form.is_valid():
       #     form.save() #saves data from a form onto the model the form is bound to if it is. 
      #      return redirect('profile')
     #   else:
    #        form.add_error('update_profile_picture', 'Make it jpeg, jdog')  #this is a form method. form inherits from the form object/class in a round about way so has access to the methods defined on it 
   #         return render(request, 'profile.html', {'form': form})
 #   else:
  #      form = Add_Profile_Picture()
        return render(request, 'profile.html') #{'form': form})
    



  

def change_number(request):
    from user.userforms.forms import Change_N
      #deferring the imort and waiting till function is called helps break circular import bug.. idk where the circular import is
    if request.method == 'POST':
        form = Change_N(request.POST)      
        if form.is_valid():
            new_number = form.cleaned_data['New_number']     #check snapchat you son  of a banshee
            current_user = request.user   #request.user automatically associates itself with the current auth user model (check settings) in django. therefore this line leads stright to the right instance of user model 
            if new_number != current_user.mobile:  # Check if the new number is different
                current_user.mobile = new_number
                current_user.save()
                return redirect('profile')
            else:
                form.add_error('New_number', 'New number must be different from the current number')  #this is a form method. form inherits from the form object/class in a round about way so has access to the methods defined on it 
        return render(request, 'change_number.html', {'form': form})
    else:
        form = Change_N()
    return render(request, 'change_number.html', {'form': form})

                                                                               #models can hold more than one value in certain fields,
                                      # like `ManyToManyField` or `JSONField`.
                                      #For regular fields like `CharField`, `IntegerField`, etc., Django's `save()`
                                      #method overwrites the existing value in the database with the new value you're assigning to the field.
            
    
    
    
    return render(request, 'change_number.html')



def change_email(request):
    from user.userforms.forms import Change_Email
      #deferring the imort and waiting till function is called helps break circular import bug.. idk where the circular import is
    if request.method == 'POST':
        form = Change_Email(request.POST)      
        if form.is_valid():
            new_email = form.cleaned_data['New_Email']     #check snapchat you son  of a banshee
            current_user = request.user   #request.user automatically associates itself with the current auth user model (check settings) in django. therefore this line leads stright to the right instance of user model 
            if new_email != current_user.email:  # Check if the new number is different
                current_user.email = new_email
                current_user.save()
                return redirect('profile')
            else:
                form.add_error('New_email', 'New email must be different from the current email')  #this is a form method. form inherits from the form object/class in a round about way so has access to the methods defined on it 
        return render(request, 'change_email.html', {'form': form})
    else:
        form = Change_Email()
    return render(request, 'change_email.html', {'form': form})




def login2(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)         #this  is different from the view function, its a utility function we a re importing (and django knwos not to muddle them up becasue they are used for different things apperently.)it offically logs in the user, meaning they can access locked parts of the site la.. form.get_user is required because it gets the user info that was authetnicated. (it gets the User instance that the form matches with). request has a session attribute, request is put as an argument (wait, is it?)because the session attribute has data like whether or not a user is logged in, this needs to be updated when auth_login() is called
            return redirect('change_number')
        else:
            return render(request, 'login.html', {'form': form})  # Render the form again with errors. errors come back attached to the form context now and you can access them in the html after an if conditional determining if there were errors. {%if form.password.errors%} and then <div class="error">{{ form.username.errors }}</div>`
    else:  # request.method == 'GET'
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


def login3(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)         #this shit is different from the view function, its a utility function we a re importing (and django knwos not to muddle them up becasue they are used for different things apperently.)it offically logs in the user, meaning they can access locked parts of the site la.. form.get_user is required because it gets the user info that was authetnicated. (it gets the User instance that the form matches with). request has a session attribute, request is put as an argument (wait, is it?)because the session attribute has data like whether or not a user is logged in, this needs to be updated when auth_login() is called
            return redirect('change_email')
        else:
            return render(request, 'login.html', {'form': form})  # Render the form again with errors. errors come back attached to the form context now and you can access them in the html after an if conditional determining if there were errors. {%if form.password.errors%} and then <div class="error">{{ form.username.errors }}</div>`
    else:  # request.method == 'GET'
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form}) 



    

    

    
    
    







# *This saves the user with the hashed password. user is an instance of the User model, and you can tell because user is lowercase (usually indicates instance of the uppercase
            #class. django knows its an instance because the UserCreationForm is set up to return an instance of User when you call form.save. in other more clear words, form.save creates the instance
            #adds it to the databse. and then your assigning it to user.
            #it basically sets the filled in form (filled in wirh rhe request.POST above) to an instance of the User model.
            #django knows that user means an instance of User because it knows that UserCreationForm is used it interacts with this
            #model. it also validates it. it also adds security like salt to it (this is why its better to do it this way) because form.save is a seperate method from save and thats all part of it.
            #its a seperate method because once its an instance, form of UserCreationForm, it gets its methods, and save as a method of that class is different
