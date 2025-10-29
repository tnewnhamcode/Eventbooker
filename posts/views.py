from django.shortcuts import render, redirect
from django.contrib import messages
from posts.postsforms.forms import PaymentForm
from user.models import Paymentinfo
from django.http import HttpResponseRedirect
from django.urls import reverse
from posts.postsforms.forms import SecurityCodeForm
from user.models import Purchase_history_class
from posts.models import funtime_disco_ticket
from django.core.mail import EmailMessage
import os




def payscreen(request):
    
    if not request.user.is_authenticated:
        return redirect('login')
    if Paymentinfo.objects.filter(payer=request.user).exists() and request.method=='GET':
        existing_payment_info = Paymentinfo.objects.get(payer=request.user)
        form = PaymentForm(instance=existing_payment_info)
        form1=SecurityCodeForm   # ----> #do the button name method geezer (check snapchat) <----
        context1={'form': form}
        context2={'form1': form1}
        merged_context={**context1,**context2}
        return render(request, 'payscreen.html', merged_context)
    elif request.method=='GET':
        form = PaymentForm(request.POST)
        form1=SecurityCodeForm
        context1={'form': form}
        context2={'form1': form1}
        merged_context={**context1,**context2}
        return render(request, 'payscreen.html', merged_context)
    else:
        form = PaymentForm(request.POST)
        form1=SecurityCodeForm(request.POST)
        context1={'form': form}
        context2={'form1': form1}
        merged_context={**context1,**context2}
        if form.is_valid() and not Paymentinfo.objects.filter(payer=request.user).exists() and not form1==None:
            thingy=request.path.split("/")
            purchase_history_instance=Purchase_history_class(purchaser=request.user, purchase_history=thingy[1])
            purchase_history_instance.save() #you gotta save the instance to the table using .save when done initalizing it
            payment_info = form.save(commit=False)  #using a form.save to a model creates an instance of the model. form.save is a method belonging to forms. and thats what it does
            payment_info.payer=request.user
            payment_info.save()
            if thingy[1]=='Funtime Disco':
                file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Funtime_Disco_Ticket.pdf')    #finds the current set directory of this file (coz it may not actually be what you think)
                email_message = EmailMessage('Funtime Disco reciept','Thank you for purchasing! Attached is your e-ticket for Funtime Disco. Please do not show it to any real bouncer. Enjoy!', to=[request.user.email])
                email_message.attach_file(file_path) 
                email_message.send()        #this and the one above are instance methods on the class EmailMessage. So it requires to first create an instance (such as email_message)
                
            
            messages.success(request, 'Payment successful! (not for real...) Check your profile page (top right of home) for purchase confirmation')
            return redirect('successcreen')
        elif form.is_valid() and Paymentinfo.objects.filter(payer=request.user).exists() and not form1==None:
            thing=request.path.split("/")
            purchase_history_instance=Purchase_history_class(purchaser=request.user, purchase_history=thing[1])
            purchase_history_instance.save()
            messages.success(request, 'Payment successful! (not for real...) Check your email for ticket(s)! Check your profile page, linked just below Logout at the top right of the Homepage, for purchase confirmation.') #send more if more ordered.. shit.
            if thing[1]=='Funtime Disco':
                file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Funtime_Disco_Ticket.pdf')
                email_message = EmailMessage('Funtime Disco reciept','Thank you for purchasing! Attached is your e-ticket for Funtime Disco. Please do not show it to any real bouncer. Enjoy!', to=[request.user.email])
                email_message.attach_file(file_path) 
                email_message.send() 
                
            return redirect('successcreen')
        else:
            return render(request, 'payscreen.html', merged_context)
    


        #'In Python, the order in which you *define* functions in your script doesn't strictly dictate when they can be called. What matters is
        #that the function is defined before it's actually *executed* during the program's runtime. javascript also 'hoists' function defnitions to the top, but not function expressions
